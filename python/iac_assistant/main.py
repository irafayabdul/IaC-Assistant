from __future__ import annotations

import datetime
import os

from dotenv import load_dotenv
from utils.docker_utils import build_and_push_docker_image
from utils.environment import Environment
from utils.file_utils import read_file
from utils.file_utils import read_folder_structure
from utils.terraform_utils import run_terraform_apply
from utils.terraform_utils import run_terraform_init
from utils.terraform_utils import run_terraform_plan

# === Load .env variables ===
load_dotenv()

# === Get values from .env ===
app_path = Environment.get_app_path()
dockerfile_name = Environment.get_dockerfile_name()
terraform_file_name = Environment.get_terraform_file_name()
docker_image_name = Environment.get_docker_image_name()

if not app_path or not dockerfile_name:
    raise ValueError(
        "MERN_APP_PATH and DOCKERFILE_NAME must be set for this operation."
    )

dockerfile_path = os.path.join(app_path, dockerfile_name)
tf_file_path = terraform_file_name

# === Prompt message ===
user_prompt = f"""
Hello, there is a folder at {app_path}. There is a Dockerized app.
Deploy it to AWS using the existing Terraform file. First build and push
the Docker image to Docker Hub.
"""


def main() -> None:
    # === Step 1: Read folder and terraform file ===
    if not tf_file_path:
        raise ValueError("TERRAFORM_FILE must be set for this operation.")

    folder_structure = read_folder_structure(app_path)
    tf_file_content = read_file(tf_file_path)

    print("\n📁 Folder Structure:\n", folder_structure)
    print("\n📝 Terraform File Preview:\n", tf_file_content[:500], "...")

    # === Step 2: Build and push Docker image ===
    if not docker_image_name:
        raise ValueError("DOCKER_IMAGE_NAME must be set")

    build_and_push_docker_image(app_path, dockerfile_path, docker_image_name)

    # === Step 3: Run terraform ===
    run_terraform_init(os.path.dirname(tf_file_path))
    plan_output = run_terraform_plan(os.path.dirname(tf_file_path))

    print("\n📋 Terraform Plan Output (Preview):\n", plan_output[:1000], "...")

    # === Step 4: Confirm apply ===
    confirm = input("\n🚀 Proceed with terraform apply? (y/n): ")
    if confirm.lower() == "y":
        run_terraform_apply(os.path.dirname(tf_file_path))
        print("\n✅ Terraform Apply Completed.\n")
    else:
        print("\n❌ Terraform Apply Cancelled.\n")

    # === Step 5: Save logs ===
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    log_dir = f"logs/deploy_{timestamp}"
    os.makedirs(log_dir, exist_ok=True)

    with open(os.path.join(log_dir, "prompt.txt"), "w") as f:
        f.write(user_prompt)

    with open(os.path.join(log_dir, terraform_file_name), "w") as f:
        f.write(tf_file_content)

    with open(os.path.join(log_dir, "plan.txt"), "w") as f:
        f.write(plan_output)

    print(f"\n🗂️ Logs saved at: {log_dir}\n")


if __name__ == "__main__":
    main()
