import os
import shutil

TEMP_FOLDERS = [
    os.environ.get("TEMP"),        # %TEMP%
    os.environ.get("TMP"),         # %TMP%
    r"C:\Windows\Temp",            # TEMP
    r"C:\Windows\Prefetch"         # Prefetch
]

def cleanup(path):
    if not path or not os.path.exists(path):
        print(f"Path does not exist: {path}")
        return 0, 0  # files deleted, bytes freed

    files_deleted = 0
    bytes_freed = 0

    try:
        for root, dirs, files in os.walk(path):
            for name in files:
                file_path = os.path.join(root, name)
                try:
                    size = os.path.getsize(file_path)
                    os.remove(file_path)
                    files_deleted += 1
                    bytes_freed += size
                except Exception as e:
                    print(f"Failed to delete file {file_path}: {e}")

            for name in dirs:
                dir_path = os.path.join(root, name)
                try:
                    # Calculate folder size before deleting
                    folder_size = sum(
                        os.path.getsize(os.path.join(dp, f))
                        for dp, dn, filenames in os.walk(dir_path)
                        for f in filenames
                    )
                    shutil.rmtree(dir_path)
                    files_deleted += 1  # counting folder as one item deleted
                    bytes_freed += folder_size
                except Exception as e:
                    print(f"Failed to delete directory {dir_path}: {e}")
    except Exception as e:
        print(f"Error while cleaning up {path}: {e}")

    return files_deleted, bytes_freed

if __name__ == "__main__":
    total_files_deleted = 0
    total_bytes_freed = 0

    print("🚀 Starting system cleanup...\n")
    for folder in TEMP_FOLDERS:
        files, freed = cleanup(folder)
        total_files_deleted += files
        total_bytes_freed += freed

    print("\n✅ Cleanup complete!")
    print(f"Total items deleted: {total_files_deleted}")
    print(f"Total space freed: {total_bytes_freed / (1024**2):.2f} MB")  # Convert bytes to MB
