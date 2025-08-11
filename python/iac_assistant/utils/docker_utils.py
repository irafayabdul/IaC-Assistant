from __future__ import annotations

import subprocess

from .environment import Environment


def build_and_push_docker_image(
    context_path: str, dockerfile_path: str, image_name: str
) -> None:
    print("\n🔐 Logging in to Docker Hub ...")
    username = Environment.get_docker_username()
    password = Environment.get_docker_password()

    if not username or not password:
        raise ValueError("DOCKER_USERNAME and DOCKER_PASSWORD must be set")

    subprocess.run(
        ["docker", "login", "-u", username, "--password-stdin"],
        input=password,
        text=True,
        check=True,
    )

    print(f"\n🐳 Building Docker image: {image_name} ...")
    subprocess.run(
        ["docker", "build", "-t", image_name, "-f", dockerfile_path, context_path],
        check=True,
    )

    print(f"\n📦 Pushing Docker image to Docker Hub: {image_name} ...")
    subprocess.run(["docker", "push", image_name], check=True)
