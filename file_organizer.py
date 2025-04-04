import os
import shutil
from pathlib import Path

directory = Path.home()/ "Downloads"

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
}

for file in os.listdir(directory):
    file_path = os.path.join(directory, file)
    
    if os.path.isfile(file_path):
        extension = os.path.splitext(file_path)[1].lower()
        
        if extension in extensions:
            file_name = extensions[extension]

