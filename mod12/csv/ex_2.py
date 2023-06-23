import csv

FILENAME = 'users.csv'

users = [
    {'name': 'Микола', 'age': 22, 'sex': 'male'},
    {'name': 'Марія', 'age': 22, 'sex': 'female'},
    {'name': 'Назар', 'age': 22, 'sex': 'male'}
]

with open(FILENAME, 'w', newline='', encoding='utf-8') as file:
    columns = ['name', 'age', 'sex']
    writer = csv.DictWriter(file, delimiter=',', fieldnames=columns)
    writer.writeheader()
    for row in users:
        writer.writerow(row)


with open(FILENAME, 'r', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)
        # print(row['name'], row['age'])

