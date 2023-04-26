# Importing the necessary libraries
import os
import argparse

# Using the ARGPARSE module for the command line parsing
parser = argparse.ArgumentParser(description='How to use this Program - Sample input "python filename.py Operation to be performed Path of the directory"')
parser.add_argument('arg1', help='Please enter the operation you want to perform on the directory such as add, remove, fetch, update, print')
parser.add_argument('folderPath', help='Path of the directory on which you want to perform operation the path should be conclosed in double quotes')

args = parser.parse_args()

# For various operations seperate function is defined

# function to add a new folder at a particular path in the directory tree
def addFolder(path, folderName):
    newFolderPath = os.path.join(path, folderName)
    if not os.path.exists(newFolderPath):
        os.makedirs(newFolderPath)
        print(f"New folder {folderName} created at {path}")
    else:
        print(f"Folder {folderName} already exists at {path}")

# function to remove a folder from a particular path in the directory tree
def removeFolder(path, folderName):
    folderPath = os.path.join(path, folderName)
    if os.path.exists(folderPath):
        os.rmdir(folderPath)
        print(f"Folder {folderName} removed from {path}")
    else:
        print(f"Folder {folderName} does not exist at {path}")


# function to fetch the path of the given folder and all folders with the same name in subfolders
def fetchFolderPath(rootPath, folderName):
    folderPaths = []
    for path, dirs, files in os.walk(rootPath):
        if folderName in dirs:
            folderPaths.append(os.path.join(path, folderName))
        for dir in dirs:
            if dir.startswith(folderName):
                folderPaths.extend(fetchFolderPath(os.path.join(path, dir), folderName))
    return folderPaths




# function to update the name of the folder
def updateFolderName(path, oldFolderName, newFolderName):
    oldFolderPath = os.path.join(path, oldFolderName)
    newFolderPath = os.path.join(path, newFolderName)
    if os.path.exists(oldFolderPath):
        os.rename(oldFolderPath, newFolderPath)
        print(f"{oldFolderName} renamed to {newFolderName} at {path}")
    else:
        print(f"Folder {oldFolderName} does not exist at {path}")

# function to print a directory structure
def printDirectoryStructure(path):
    print(f"Directory structure of {path} is :")
    for root, dirs, files in os.walk(path):
        level = root.replace(path, '').count(os.sep)
        indent = ' ' * 4 * level
        print(f"{indent}{os.path.basename(root)}/")
        subindent = ' ' * 4 * (level + 1)
        for file in files:
            print(f"{subindent}{file}")

# Main Function
def main():

    rootPath = args.folderPath.strip()
    operation = args.arg1.strip()
    
    if os.path.exists(rootPath):

        if operation == "add":
            folderName = input("Enter the folder name to be added: ")
            addFolder(rootPath, folderName)
        elif operation == "remove":
            folderName = input("Enter the folder name to be removed: ")
            removeFolder(rootPath, folderName)
        elif operation == "fetch":
            folderName = input("Enter the folder name to be fetched: ")
            folderPaths = fetchFolderPath(rootPath, folderName)
            if folderPaths:
                for path in folderPaths:
                    path = path.replace("\\", "/")
                    print(path)
            else:
                print(f"Folder {folderName} not found in {rootPath}")
        elif operation == "update":
            oldFolderName = input("Enter the old folder name: ")
            newFolderName = input("Enter the new folder name: ")
            updateFolderName(rootPath, oldFolderName, newFolderName)
        elif operation == "print":
            printDirectoryStructure(rootPath)
        else:
            print("Invalid operation entered. Please try again.")
    else:
        print("Invalid path provided")

if __name__ == "__main__":
    main()