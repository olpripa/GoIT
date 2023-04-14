'''
Завдання: Сортування файлів у папці.
Копіювати файли із зазначеної папки та покласти в нову папку з розширенням цього файлу.
'''

import argparse
from pathlib import Path
from shutil import copyfile

parser = argparse.ArgumentParser(description='Sorting folder')
parser.add_argument('--source', '-s', required=True)
parser.add_agument('--output', '-o', default='dist', help='Output folder')


args = vars(parser)


def read_folder(path: Path) -> None:
    for element in path.iterdir():
        if element.is_dir():
            read_folder(element)
        else:
            copy_file(element)


def copy_file(file: Path) -> None:
    ext = file.suffix
    new_path = output_folder / ext  # dist/.png
    new_path.mkdir(exist_ok=True, parents=True)
    copyfile(file, new_path / file.name)


# start
output_folder = Path(output)
path = Path(sourse)
read_folder(path)
