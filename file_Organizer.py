"""
📌 Problem Statement:
Create a Python script that automatically organizes files in a folder by file type,
putting images, documents, videos, etc., into separate subfolders.
"""

import os
import shutil

def organize_folder(folder_path):
    # Define file type categories
    file_types = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif'],
        'Documents': ['.pdf', '.docx', '.txt', '.xlsx','.pptx'],
        'Videos': ['.mp4', '.avi', '.mkv'],
        'Audio': ['.mp3', '.wav'],
        'Archives': ['.zip', '.rar',],
        'Scripts': ['.py', '.js','.md'],
        'Config': ['.ini'],
        'Applications': ['.exe']
    }

    print(f"📂 Organizing files in: {folder_path}\n")

    files_moved = 0

    # Loop through all files in the folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path):
            _, ext = os.path.splitext(filename)
            moved = False

            # Match file extension with category
            for folder, extensions in file_types.items():
                if ext.lower() in extensions:
                    target_folder = os.path.join(folder_path, folder)
                    os.makedirs(target_folder, exist_ok=True)  # Create if not exists
                    shutil.move(file_path, os.path.join(target_folder, filename))
                    print(f"✅ Moved: {filename} → {folder}/")
                    files_moved += 1
                    moved = True
                    break   # Stop checking other categories

            if not moved:
                print(f"⚠️ Skipped (Unknown type): {filename}")

    print(f"\n✨ Done! Total files moved: {files_moved}")


# ✅ Run the function
organize_folder(r"path/to/your/folder")
