'''
Запис у файл байтових рядків. Робота з різними кодуваннями
'''

from pathlib import Path

message = 'Привіт світ! Hello world!'

print(message.encode())

print(message.encode('utf-16'))
print(message.encode('cp1251'))  # кодування windows

a = b'\xcf\xf0\xe8\xe2\xb3\xf2 \xf1\xe2\xb3\xf2! Hello world!'
# print(a.decode('utf-16'))

folder = Path('Test')
# folder.write_bytes()

with open(folder / 'utf-8.txt', 'wb') as file:
    file.write(message.encode())

with open(folder / 'utf-16.txt', 'wb') as file:
    file.write(message.encode('utf-16'))

with open(folder / 'cp1251.txt', 'wb') as file:
    file.write(message.encode('cp1251'))


with open(folder / 'utf-8.txt', 'rb') as file:
    print(file.read().decode('utf-8'))  # utf-8 використовується за замовчуванням

with open(folder / 'utf-16.txt', 'rb') as file:
    print(file.read().decode('utf-16'))

with open(folder / 'cp1251.txt', 'rb') as file:
    print(file.read().decode('cp1251'))