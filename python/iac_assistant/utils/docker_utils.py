import os
import subprocess

def build_and_push_docker_image(context_path, dockerfile_path, image_name):
    print("\n🔐 Logging in to Docker Hub ...")
    username = os.getenv("DOCKER_USERNAME")
    password = os.getenv("DOCKER_PASSWORD")
    subprocess.run(["docker", "login", "-u", username, "--password-stdin"], input=password, text=True, check=True)

    print(f"\n🐳 Building Docker image: {image_name} ...")
    subprocess.run(["docker", "build", "-t", image_name, "-f", dockerfile_path, context_path], check=True)

    print(f"\n📦 Pushing Docker image to Docker Hub: {image_name} ...")
    subprocess.run(["docker", "push", image_name], check=True)
