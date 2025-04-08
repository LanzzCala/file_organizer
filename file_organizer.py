import os
import shutil
from pathlib import Path

directory = Path.home()/ "Downloads" #Specify directory path

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
    ".exe": "Executables",
}
#Iterate through each file in the specified directory
for file in os.listdir(directory):
    file_path = os.path.join(directory, file) #Create an object that joins the path of the directory to the current file
    
    if os.path.isfile(file_path): #Check if current file object is an actual file and not a directory
        extension = os.path.splitext(file_path)[1].lower() #Separate file object from extension name to specify folder
        
        if extension in extensions: #Check if current file object's extension is in dictionary of extensions
            new_folder = extensions[extension] #Create new directory based on extension

            folder_path = os.path.join(directory, new_folder) #Create new path to new directory
            os.makedirs(folder_path, exist_ok=True) #Create new directory & check if already exists, if so, doesn't dupe
            shutil.move(file_path, folder_path) #Move current file object to new directory

            print (f"Moved {file} into {folder_path}.")
        else:
            print(f"Sorry, {extension} is not a valid extension.")
    else:
        print(f"Sorry {file} is a directory not a file.")

