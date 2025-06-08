import os
import shutil

directory = r"C:\Users\Asus\z_test"  # Change this to your directory path
if not os.path.exists(directory):
    print(f"The directory {directory} does not exist.")
    exit(1)

type_paths = {
    'images': r"C:\Users\Asus\Pictures\Downloaded_pictures",
    'documents': r"C:\Users\Asus\Documents\Downloads",
    'audio': r"C:\Users\Asus\Music\Downloaded_audios",
    'videos': r"C:\Users\Asus\Videos\Downloaded_videos",
    'archives': r"C:\Users\Asus\Downloads\Archives",
    'scripts': r"C:\Users\Asus\Downloads\Scripts",
    'others': r"C:\Users\Asus\Downloads\Others",
    'books': r"C:\Users\Asus\Documents\e-BOOKS\Random"
    }

extensions = {
    'images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    'documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx', '.csv'],
    'audio': ['.mp3', '.wav', '.aac', '.flac'],
    'videos': ['.mp4', '.avi', '.mov', '.mkv'],
    'archives': ['.zip', '.rar', '.tar', '.gz'],
    'scripts': ['.py', '.js', '.sh', '.bat'],
    'books' : ['.epub', '.mobi'],
    'others': []
    }


def main():
    files = list_files_os_listdir(directory)
    for file in files:
        organize_file(file)


def file_type(file):
    file_extension = os.path.splitext(file)[1].lower()
    for category, exts in extensions.items():
        if file_extension in exts:
            return category
    return 'others'


def list_files_os_listdir(directory):
    files = os.listdir(directory)
    file_list = []
    for file in files:
        if os.path.isfile(os.path.join(directory, file)):
            file_list.append(file)
    return file_list


def organize_file(file):
    file_category = file_type(file)
    shutil.move(
        os.path.join(directory, file),
        os.path.join(type_paths[file_category], file)
    )

if __name__ == "__main__":
    main()