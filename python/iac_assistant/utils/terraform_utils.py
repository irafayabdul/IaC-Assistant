import subprocess

def run_terraform_init(path):
    print("\n🔧 Running terraform init ...")
    subprocess.run(["terraform", "init"], cwd=path, check=True)

def run_terraform_plan(path):
    print("\n📋 Running terraform plan ...")
    result = subprocess.run(["terraform", "plan"], cwd=path, check=True, capture_output=True, text=True)
    return result.stdout

def run_terraform_apply(path):
    print("\n🚀 Running terraform apply ...")
    result = subprocess.run(["terraform", "apply", "-auto-approve"], cwd=path, check=True, capture_output=True, text=True)
    return result.stdout
