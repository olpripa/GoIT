'''
Завдання: Сортування файлів у папці.
Копіювати файли із зазначеної папки та покласти в нову папку з розширенням цього файлу.
'''

from pathlib import Path
from shutil import copyfile

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
output_folder = Path('dist')
path = Path('picture')
read_folder(path)
