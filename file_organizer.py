import os
import pathlib as path

list_of_directories = {
    "Images_Folder": [".jpeg", ".jpg", ".gif", ".png"],
    "Videos_Folder": [".wmv", ".mov", ".mp4", "mpg", ".mpeg", ".mkv"],
    "Zips_Folder": [".iso", ".tar", ".gz", ".rz", ".7z", ".dmg", ".rar", ".zip"],
    "Music_Folder": [".mp3", ".msv", ".wav", ".wma"],
    "PDF_Folder": [".pdf"],
}

file_format_dictionary = {
    final_file_format: directory
    for directory, file_format_stored in list_of_directories.items()
    for final_file_format in file_format_stored
}

def organizer():
    for entry in os.scandir():
        if entry.is_dir():
            continue
        file_path = path(entry)
        final_file_format = file_path.suffix.lower()
        if final_file_format in file_format_dictionary:
            directory_path = path(file_format_dictionary[final_file_format])