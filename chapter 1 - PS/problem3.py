import os

def print_directory_contents(path):
    try:
        # Get the list of all files and directories
        entries = os.listdir(path)
        
        print(f"Contents of the directory '{path}':")
        for entry in entries:
            print(entry)
    except FileNotFoundError:
        print(f"The directory '{path}' does not exist.")
    except PermissionError:
        print(f"Permission denied to access the directory '{path}'.")

# Example usage:
directory_path = "."  # You can change this to any directory path you want to list
print_directory_contents(directory_path)
