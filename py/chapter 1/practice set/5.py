import os

# Get the directory path (you can change this to any path you want)
directory_path = input("Enter directory path: ")

try:
    # List all files and folders in the directory
    contents = os.listdir(directory_path)
    
    print(f"\nContents of '{directory_path}':")
    for item in contents:
        print(item)

except FileNotFoundError:
    print("The specified directory does not exist.")
except PermissionError:
    print("You do not have permission to access this directory.")
