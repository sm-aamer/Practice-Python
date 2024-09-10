import os

def list_directory_contents(directory_path):
    try:
        contents = os.listdir(directory_path)
        for item in contents:
            print(item)
    except FileNotFoundError:
        print(f"The directory {directory_path} does not exist.")
    except PermissionError:
        print(f"Permission denied for accessing {directory_path}.")
    except Exception as e:
        print(f"An error occurred: {e}")
# This program is used to find out files and folder at the specific loc or path
# Example usage: change the directory_path to a valid path on your system
directory_path = "/Misc Docus"
list_directory_contents(directory_path)

