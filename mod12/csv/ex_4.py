# Зберегти у файлі таблицю квадратів та кубів цілих чисел від 1 до 20

import csv
filename = 'table.csv'

with open(filename, 'w') as file:
    writer = csv.writer(file)
    for i in range(1, 21):
        writer.writerow([i, i**2, i**3])

with open(filename, 'r') as file:
    r = csv.reader(file)
    res = []
    for line in r:
        res.append(line)

print(res)

