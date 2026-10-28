# Program: File Management and Directory Navigation Utility

import os
import sys


def show_current_directory():
    print("\n========== CURRENT DIRECTORY ==========")
    print("Current Working Directory:", os.getcwd())


def list_directory():
    path = input("Enter directory path (press Enter for current directory): ").strip()

    if not path:
        path = os.getcwd()

    if os.path.isdir(path):
        print("\n========== DIRECTORY CONTENTS ==========")

        for item in os.listdir(path):
            full_path = os.path.join(path, item)

            if os.path.isdir(full_path):
                print("[DIR] ", item)
            else:
                print("[FILE]", item)
    else:
        print("Error: Directory does not exist!")


def navigate_directory():
    path = input("Enter directory path to navigate to: ").strip()

    if os.path.isdir(path):
        try:
            os.chdir(path)
            print("Directory changed successfully!")
            print("Current Directory:", os.getcwd())
        except OSError as error:
            print("Unable to change directory:", error)
    else:
        print("Error: Invalid directory path!")


def create_workspace():
    folder_name = input("Enter workspace folder name: ").strip()

    if not folder_name:
        print("Folder name cannot be empty!")
        return

    # Prevent directory traversal and absolute paths
    if os.path.basename(folder_name) != folder_name:
        print("Enter a folder name, not a directory path!")
        return

    workspace_path = os.path.join(os.getcwd(), folder_name)

    try:
        os.makedirs(workspace_path, exist_ok=True)
        print("Workspace created successfully!")
        print("Workspace Path:", workspace_path)
    except OSError as error:
        print("Error creating workspace:", error)


def filter_files():
    path = input("Enter directory path (press Enter for current directory): ").strip()
    extension = input("Enter file extension (e.g., .txt, .py): ").strip()

    if not path:
        path = os.getcwd()

    if not extension:
        print("File extension cannot be empty!")
        return

    if not extension.startswith("."):
        extension = "." + extension

    if not os.path.isdir(path):
        print("Error: Directory does not exist!")
        return

    print(f"\n========== FILES WITH {extension} EXTENSION ==========")

    files = [
        item for item in os.listdir(path)
        if os.path.isfile(os.path.join(path, item))
        and item.lower().endswith(extension.lower())
    ]

    if files:
        for file in files:
            print(file)
        print("Total matching files:", len(files))
    else:
        print("No matching files found.")


def manage_text_log():
    print("\n1. Read a text log")
    print("2. Create or append to a text log")

    choice = input("Enter your choice: ").strip()
    filename = input("Enter text log filename: ").strip()

    if not filename:
        print("Filename cannot be empty!")
        return

    # Restrict operations to a filename in the current directory
    if os.path.basename(filename) != filename or filename in (".", ".."):
        print("Enter a filename without a directory path!")
        return

    if not filename.lower().endswith(".txt"):
        print("Only .txt files are allowed!")
        return

    filepath = os.path.join(os.getcwd(), filename)

    if choice == "1":
        try:
            # Safe reading with a context manager
            with open(filepath, "r", encoding="utf-8") as file:
                print("\n========== LOG CONTENTS ==========")
                print(file.read())

        except FileNotFoundError:
            print("Error: Log file does not exist!")
        except OSError as error:
            print("Error reading log:", error)

    elif choice == "2":
        message = input("Enter log message: ")

        try:
            # Append text without overwriting existing contents
            with open(filepath, "a", encoding="utf-8") as file:
                file.write(message + "\n")

            print("Log entry saved successfully!")

        except OSError as error:
            print("Error writing log:", error)

    else:
        print("Invalid choice!")


def process_command_line_arguments():
    print("\n========== COMMAND-LINE ARGUMENTS ==========")

    print("Script Name:", os.path.basename(sys.argv[0]))

    if len(sys.argv) > 1:
        print("Arguments Provided:")

        for index, argument in enumerate(sys.argv[1:], start=1):
            print(f"Argument {index}: {argument}")
    else:
        print("No command-line arguments provided.")


def main():
    while True:
        print("\n====== FILE MANAGEMENT UTILITY ======")
        print("1. Show Current Directory")
        print("2. List Directory Contents")
        print("3. Navigate to Directory")
        print("4. Create Workspace Folder")
        print("5. Filter Files by Extension")
        print("6. Read or Create Text Log")
        print("7. Display Command-Line Arguments")
        print("8. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            show_current_directory()

        elif choice == "2":
            list_directory()

        elif choice == "3":
            navigate_directory()

        elif choice == "4":
            create_workspace()

        elif choice == "5":
            filter_files()

        elif choice == "6":
            manage_text_log()

        elif choice == "7":
            process_command_line_arguments()

        elif choice == "8":
            print("Exiting File Management Utility. Goodbye!")
            break

        else:
            print("Invalid choice! Please select from 1 to 8.")


if __name__ == "__main__":
    main()
