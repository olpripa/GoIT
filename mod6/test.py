from pathlib import Path
folder = Path('./Test')

filename = folder / 'temp.txt'

try:
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            print(line, end='')
except OSError as error:
    print('File not found')
finally:
    print('Робота із файлом завершено')

current_path = Path('.')

print(current_path)
print(current_path.cwd())

import shutil

print(shutil.get_archive_formats())