import sys
from pathlib import Path

dict_groups = {"images": ['jpeg', 'jpg', 'bmp', 'gif', 'tiff'],
               "documents": ['csv', 'doc', 'docx', 'pdf', 'ppt', 'pptx', 'rtf', 'xls', 'xlsx'],
               "audio": ['aac', 'amr', 'mp3', 'wav', 'wma'],
               "video": ['avi', 'mov', 'mp4', 'mpeg', 'mkv'],
               "archives": ['zip', 'gz', 'tar'],
               "oter": []}

list_images = []
list_documents = []
list_audio = []
list_video = []
list_archives = []
list_other = []

ext_unknown = []
ext_no_unknown = []


path = Path(sys.argv[1])  # sys.argv[1] == test


def parse_folder_recursion(path):
    for element in path.iterdir():
        if element.is_dir():
            print(f'parse_folder: This is folder - {element.name}')
            parse_folder_recursion(element)  # рекурсія
        else:
            print(
                f'parse_folder: This is file - {element.name} ext: {element.suffix}')


if __name__ == "__main__":
    parse_folder_recursion(path)
