import os
import shutil

TEMP_FOLDERS = [
    os.environ.get("TEMP"), # %TEMP%
    os.environ.get("TMP"),  # %TMP%
    r"C:\Windows\Temp",     # TEMP
    r"C:\Windows\Prefetch"  # Prefetch
]

def cleanup(path):                                                          # Defining a Function
    if not path or not os.path.exists(path):                                # If wrong PATH or not exist
        print(f"Path does not exist: {path}")                               # Print message
        return                                                              # return

    try:
        for root, dirs, files in os.walk(path):
            for name in files:
                file_path = os.path.join(root, name)
                try:
                    os.remove(file_path)                                    # Remove file
                    print(f"Deleted file: {file_path}")
                except Exception as e:                                      # If error
                    print(f"Failed to delete file {file_path}: {e}")

            for name in dirs:
                dir_path = os.path.join(root, name)
                try:
                    shutil.rmtree(dir_path)                                 # Remove whole directory
                    print(f"Deleted directory: {dir_path}")
                except Exception as e:                                      # If error
                    print(f"Failed to delete directory {dir_path}: {e}")
    except Exception as e:                                                  # If error
        print(f"Error while cleaning up {path}: {e}")

if __name__ == "__main__":
    print("🚀 Starting system cleanup...\n")
    for folder in TEMP_FOLDERS:                                             # Iterate through Folders
        cleanup(folder)                                                     # Call the Function
    print("\n✅ Cleanup complete!")
