import os
import yaml

def getYamlData():
    try:
        with open("D:/Web/Final Assignment/first/config.yaml", "r") as f:
            data = yaml.safe_load(f)

        for k,v in data.items():
            if v is None:
                data = os.getcwd()
            elif k == "dir":
                data = list(data.values())
                data = data[0].replace("\\", "/")

        return data
    except Exception as e:
        print(f"An error occurred: {e}")

# function to add a new folder at a particular path in the directory tree
def add_folder(path, folder_name):
    new_folder_path = os.path.join(path, folder_name)
    if not os.path.exists(new_folder_path):
        os.makedirs(new_folder_path)
        path = path.replace("/", "\\")
        print(f"New folder {folder_name} created at {path}")
    else:
        print(f"Folder {folder_name} already exists at {path}")

# function to remove a folder from a particular path in the directory tree
def remove_folder(path, folder_name):
    folder_path = os.path.join(path, folder_name)
    if os.path.exists(folder_path):
        os.rmdir(folder_path)
        print(f"Folder {folder_name} removed from {path}")
    else:
        print(f"Folder {folder_name} does not exist at {path}")


# function to fetch the path of the given folder and all folders with the same name in subfolders
def fetch_folder_path(root_path, folder_name):
    folder_paths = []
    for path, dirs, files in os.walk(root_path):
        if folder_name in dirs:
            folder_paths.append(os.path.join(path, folder_name))
        for dir in dirs:
            if dir.startswith(folder_name):
                folder_paths.extend(fetch_folder_path(os.path.join(path, dir), folder_name))
    return folder_paths

# function to update the name of the folder
def update_folder_name(path, old_folder_name, new_folder_name):
    old_folder_path = os.path.join(path, old_folder_name)
    new_folder_path = os.path.join(path, new_folder_name)
    if os.path.exists(old_folder_path):
        os.rename(old_folder_path, new_folder_path)
        print(f"{old_folder_name} renamed to {new_folder_name} at {path}")
    else:
        print(f"Folder {old_folder_name} does not exist at {path}")

# function to print a directory structure
def print_directory_structure(path):
    print(f"Directory structure of {path}:")
    for root, dirs, files in os.walk(path):
        level = root.replace(path, '').count(os.sep)
        indent = ' ' * 4 * level
        print(f"{indent}{os.path.basename(root)}/")
        subindent = ' ' * 4 * (level + 1)
        for file in files:
            print(f"{subindent}{file}")

# example usage of the above functions with switch-case-like structure
def main():

    root_path = getYamlData()

    if root_path is None:
        print("No valid path provided please add a the correct path in Yaml file")
    elif os.path.exists(root_path):

        operation = ""

        while(operation != "quit" or operation != "Quit" or operation != "QUIT" or operation != "q" or operation != "Q"):
            operation1 = input("Enter the operation to perform (add, remove, fetch, update, print): ")
            operation = operation1.strip()
            if operation == "add":
                folder_name = input("Enter the folder name to be added: ")
                add_folder(root_path, folder_name)
            elif operation == "remove":
                folder_name = input("Enter the folder name to be removed: ")
                remove_folder(root_path, folder_name)
            elif operation == "fetch":
                folder_name = input("Enter the folder name to be fetched: ")
                folder_paths = fetch_folder_path(root_path, folder_name)
                if folder_paths:
                    for path in folder_paths:
                        print(path)
                else:
                    print(f"Folder {folder_name} not found in {root_path}")
            elif operation == "update":
                old_folder_name = input("Enter the old folder name: ")
                new_folder_name = input("Enter the new folder name: ")
                update_folder_name(root_path, old_folder_name, new_folder_name)
            elif operation == "print":
                print_directory_structure(root_path)
            else:
                print("Invalid operation entered. Please try again.")
    else:
        print("Invalid path provided please add a the correct path in Yaml file")
            

if __name__ == "__main__":
    main()
