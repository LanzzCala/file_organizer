import os
import shutil

directory = os.path.join(os.path.expanduser("~"), "Downloads")

extensions = {
    ".jpg" : "Images",
    ".png" : "Images",
    ".jpeg": "Images",
    ".gif": "Images",
    ".wmv": "Videos",
    ".mov": "Videos",
    ".mp4": "Videos",
    ".mpg": "Videos",
    ".mpeg": "Videos",
    ".mkv": "Videos",
    ".iso": "Zips",
    ".tar": "Zips",
    ".gz": "Zips",
    ".7z": "Zips",
    ".dmg": "Zips",
    ".rar": "Zips",
    ".zip": "Zips",
    ".mp3": "Music",
    ".msv": "Music",
    ".wave": "Music",
    ".wma": "Music",
    ".pdf": "Documents",
    ".doc": "Documents",
    ".txt": "Documents",
}

for filename in os.listdir(directory):
    file_path = os.path.join(directory, filename)

    if os.path.isfile(file_path):
        extension = os.path.splitext(filename)[1].lower()

        if extension in extensions:
            folder_name = extensions[extension]

            folder_path = os.path.join(directory, folder_name)
            os.makedirs(folder_path, exist_ok=True)

            destination_path = os.path.join(folder_path, filename)
            shutil.move(file_path, destination_path)

            print(f"Moved {filename} to {folder_name} folder.")
        else:
            print(f"Skipped {filename}. Unknown file extension.")
    else:
        print(f"Skipped {filename}. It is a directory.")

print("File organization completed.")

