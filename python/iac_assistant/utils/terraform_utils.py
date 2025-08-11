from __future__ import annotations

import subprocess


def run_terraform_init(path: str) -> None:
    print("\n🔧 Running terraform init ...")
    subprocess.run(["terraform", "init"], cwd=path, check=True)


def run_terraform_plan(path: str) -> str:
    print("\n📋 Running terraform plan ...")
    result = subprocess.run(
        ["terraform", "plan"], cwd=path, check=True, capture_output=True, text=True
    )
    return result.stdout


def run_terraform_apply(path: str) -> str:
    print("\n🚀 Running terraform apply ...")
    result = subprocess.run(
        ["terraform", "apply", "-auto-approve"],
        cwd=path,
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout
