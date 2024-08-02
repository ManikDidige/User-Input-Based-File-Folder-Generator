import os

def create_file_or_folder():
    # Ask user if they want to create a file or a folder
    choice = input("Do you want to create a file or a folder? (Enter 'file' or 'folder'): ").strip().lower()

    # Get the desired location from the user
    location = input("Please enter the full path where you want to create the file/folder: ").strip()

    if choice == 'file':
        # Get the file name
        file_name = input("Please enter the name of the file (with extension): ").strip()
        full_path = os.path.join(location, file_name)

        try:
            with open(full_path, 'w') as file:
                print(f"File '{file_name}' created successfully at {location}.")
        except Exception as e:
            print(f"An error occurred while creating the file: {e}")

    elif choice == 'folder':
        # Get the folder name
        folder_name = input("Please enter the name of the folder: ").strip()
        full_path = os.path.join(location, folder_name)

        try:
            os.makedirs(full_path)
            print(f"Folder '{folder_name}' created successfully at {location}.")
        except Exception as e:
            print(f"An error occurred while creating the folder: {e}")

    else:
        print("Invalid choice. Please enter 'file' or 'folder'.")

# Run the function
create_file_or_folder()
