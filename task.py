import os
import shutil

# Path to your Downloads folder (customize this!)
downloads_folder = os.path.expanduser("~/Downloads")

# File type categories
file_mappings = {
    "Images": ['.jpg', '.jpeg', '.png', '.gif'],
    "Documents": ['.pdf', '.docx', '.doc', '.txt', '.xlsx'],
    "Videos": ['.mp4', '.mov', '.avi'],
    "Audio": ['.mp3', '.wav'],
    "Archives": ['.zip', '.rar', '.tar', '.gz'],
    "Installers": ['.exe', '.msi', '.dmg'],
    "Scripts": ['.py', '.js', '.sh'],
}

# Loop through files in the folder
for filename in os.listdir(downloads_folder):
    file_path = os.path.join(downloads_folder, filename)
    
    # Skip directories
    if os.path.isdir(file_path):
        continue

    # Get file extension
    _, ext = os.path.splitext(filename)

    moved = False
    for folder_name, extensions in file_mappings.items():
        if ext.lower() in extensions:
            destination_folder = os.path.join(downloads_folder, folder_name)
            os.makedirs(destination_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(destination_folder, filename))
            print(f"Moved: {filename} → {folder_name}/")
            moved = True
            break

    if not moved:
        print(f"Skipped: {filename} (Unknown type)")

print("✅ File organization complete!")
