'''
Прочитати хвіст файлу останні N рядків файлу.
Ім'я файлу для читання передаємо як аргумент командного рядка
'''

import sys
NUMBER_LINES = 2

if len(sys.argv) != 2:
    print('Потрібно передати тільки імя файлу')
    quit()

try:
    lines = []
    with open(sys.argv[1], 'r', encoding='utf-8') as file:
        for line in file:  # те саме що і file.readline()
            lines.append(line)
            if len(lines) > NUMBER_LINES:
                lines.pop(0)
    print(lines)

except OSError as error:
    print(f'Помилка доступу до файла: {error}')
