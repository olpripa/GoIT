import sys
from pathlib import Path

path = Path(sys.argv[1])

def parse_folder_recurs(path):
    for element in path.iterdir():
        if element.is_dir():
            print(f'parse_folder: This is folder - {element.name}')
            parse_folder_recurs(element)
        else:
            print(f'parse_folder: This is file - {element.name}')

if __name__ == "__main__":
    parse_folder_recurs(path)