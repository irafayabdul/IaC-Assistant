from __future__ import annotations

import os
from typing import Optional

from dotenv import load_dotenv

load_dotenv()


class Environment:
    """Handles loading and validation of environment variables for the IaC Assistant."""

    @staticmethod
    def load_env_variable(name: str, fallback: Optional[str] = None) -> Optional[str]:
        return os.getenv(name, fallback)

    # --- Path Variables ---
    @staticmethod
    def get_app_path() -> Optional[str]:
        return Environment.load_env_variable("MERN_APP_PATH")

    @staticmethod
    def get_dockerfile_name() -> Optional[str]:
        return Environment.load_env_variable("DOCKERFILE_NAME")

    @staticmethod
    def get_terraform_file_name() -> Optional[str]:
        return Environment.load_env_variable("TERRAFORM_FILE")

    # --- Docker Variables ---
    @staticmethod
    def get_docker_image_name() -> Optional[str]:
        return Environment.load_env_variable("DOCKER_IMAGE_NAME")

    @staticmethod
    def get_docker_username() -> Optional[str]:
        return Environment.load_env_variable("DOCKER_USERNAME")

    @staticmethod
    def get_docker_password() -> Optional[str]:
        return Environment.load_env_variable("DOCKER_PASSWORD")
