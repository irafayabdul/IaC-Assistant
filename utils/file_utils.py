import os

def read_folder_structure(path):
    output = ""
    for root, dirs, files in os.walk(path):
        level = root.replace(path, "").count(os.sep)
        indent = "  " * level
        output += f"{indent}{os.path.basename(root)}/\n"
        for file in files:
            sub_indent = "  " * (level + 1)
            output += f"{sub_indent}{file}\n"
    return output

def read_file(filepath):
    with open(filepath, "r") as file:
        return file.read()
