# usb_script.py
import os
import shutil

# Variable Section
# ----------------

# Specify the base folder name for the archive
ARCHIVE_FOLDER_NAME = "Archive"

# Specify the subfolder names for different operating systems
WINDOWS_SUBFOLDER = "Windows_Destination"
MACOS_SUBFOLDER = "macOS_Destination"
LINUX_SUBFOLDER = "Linux_Destination"

# Specify whether to delete files after copying
DELETE_AFTER_COPY = True  # Set to True to delete files, False to move them to Archive

# Function to get the OS-specific destination path
def get_os_specific_path(base_path, os_type):
    if os_type == "Windows":
        return os.path.join(base_path, WINDOWS_SUBFOLDER)
    elif os_type == "macOS":
        return os.path.join(base_path, MACOS_SUBFOLDER)
    elif os_type == "Linux":
        return os.path.join(base_path, LINUX_SUBFOLDER)
    else:
        raise ValueError("Invalid OS type")

# ----------------

def copy_files(source_directory, destination_directory, delete_after_copy=DELETE_AFTER_COPY, os_type="Windows"):
    try:
        # List all files in the source directory
        files = os.listdir(source_directory)

        # Create or ensure the existence of the "Archive" folder on the USB stick
        archive_folder = os.path.join(source_directory, ARCHIVE_FOLDER_NAME)
        if not os.path.exists(archive_folder):
            os.makedirs(archive_folder)

        # Adjust the computer destination directory based on the operating system
        adjusted_destination_directory = get_os_specific_path(destination_directory, os_type)

        # Ensure the adjusted destination directory exists, create if not
        if not os.path.exists(adjusted_destination_directory):
            os.makedirs(adjusted_destination_directory)

        # Copy each file to the adjusted destination directory
        for file in files:
            source_path = os.path.join(source_directory, file)
            destination_path = os.path.join(adjusted_destination_directory, file)
            shutil.copy2(source_path, destination_path)

        # Move files to the "Archive" folder if not deleting
        if not delete_after_copy:
            for file in files:
                source_path = os.path.join(source_directory, file)
                archive_path = os.path.join(archive_folder, file)
                shutil.move(source_path, archive_path)
            print(f"Files moved to {archive_folder}")

        print(f"Files copied from {source_directory} to {adjusted_destination_directory}")

        # Delete files from the source directory if specified
        if delete_after_copy:
            for file in files:
                file_path = os.path.join(source_directory, file)
                os.remove(file_path)
            print(f"Files deleted from {source_directory}")
    except Exception as e:
        print(f"Error: {e}")

def main():
    # Set default source and destination directories
    usb_source_directory = os.path.join(os.getcwd(), "USB_Source")
    computer_destination_directory = os.path.join(os.getcwd(), "Computer_Destination")

    # Specify operating system type
    os_type = input("Enter the operating system type (Windows, macOS, Linux): ")

    print(f"Default USB Source Directory: {usb_source_directory}")
    print(f"Default Computer Destination Directory: {computer_destination_directory}")

    # Allow the user to confirm or modify directories
    user_confirmation = input("Do you want to use the default directories? (y/n): ").lower()

    if user_confirmation == 'n':
        usb_source_directory = input("Enter the source directory on the USB stick: ")
        computer_destination_directory = input("Enter the base destination directory on the computer: ")

    # Call the function to copy files
    copy_files(usb_source_directory, computer_destination_directory, os_type=os_type)

if __name__ == "__main__":
    main()
