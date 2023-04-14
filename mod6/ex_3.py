'''
Прочитати перші N рядків файлу.
Ім'я файлу для читання передаємо як аргумент командного рядка
'''

import sys
NUMBER_LINES = 5

if len(sys.argv) != 2:
    print('Потрібно передати тільки імя файлу')
    quit()

try:
    file = open(sys.argv[1], 'r', encoding='utf-8')
    line = file.readline()
    count = 0
    while count < NUMBER_LINES and line != '':
        line = line.strip()
        count += 1
        print(line)
        line = file.readline()
    file.close()
except OSError as error:
    print(f'Помилка доступу до файла: {error}')
