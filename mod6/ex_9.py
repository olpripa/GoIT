'''
Запис до файлу pathlib
'''

from pathlib import Path
list_data = ['First line\n', 'Hello world\n', 'Aloha guys\t', 'Last line']
folder = Path('Temp')

with open(folder / 'data.txt', 'w', encoding='utf-8') as f:
    for line in list_data:
        f.write(line)


with open(folder / 'data-all.txt', 'w', encoding='utf-8') as f:
    f.writelines(list_data)

