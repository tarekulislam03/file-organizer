import os
import shutil

# 👉 Change this to your Downloads folder
DOWNLOADS_FOLDER = os.path.join(os.path.expanduser("~"), "Downloads")

# File type categories
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "PDFs": [".pdf"],
    "Videos": [".mp4", ".mkv", ".flv", ".avi", ".mov"],
    "Music": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Programs": [".exe", ".msi"],
    "Scripts": [".py", ".js", ".html", ".css"],
    "Others": []  # Everything else
}

def organize_files():
    for filename in os.listdir(DOWNLOADS_FOLDER):
        file_path = os.path.join(DOWNLOADS_FOLDER, filename)

        # Skip folders
        if os.path.isdir(file_path):
            continue

        _, ext = os.path.splitext(filename)
        ext = ext.lower()

        moved = False
        for folder, extensions in FILE_TYPES.items():
            if ext in extensions:
                folder_path = os.path.join(DOWNLOADS_FOLDER, folder)
                os.makedirs(folder_path, exist_ok=True)
                shutil.move(file_path, os.path.join(folder_path, filename))
                print(f"Moved: {filename} → {folder}")
                moved = True
                break

        if not moved:  # If extension not found, move to "Others"
            folder_path = os.path.join(DOWNLOADS_FOLDER, "Others")
            os.makedirs(folder_path, exist_ok=True)
            shutil.move(file_path, os.path.join(folder_path, filename))
            print(f"Moved: {filename} → Others")

if __name__ == "__main__":
    organize_files()
    print("✅ Files organized successfully!")
