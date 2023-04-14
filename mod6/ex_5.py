'''
Читаємо файл за допомогою бібліотеки pathlib
'''

from pathlib import Path
folder = Path('./Temp')

filename = folder / 'temp.txt'

try:
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            print(line, end='')
except OSError as error:
    print(f'Помилка доступу до файла: {error}')
finally:
    print('\nРобота з файлом завершена')
