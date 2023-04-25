"""
Реалізувати функцію, яка повертає n чисел, що найчастіше зустрічаються і n які найменш часто зустрічаються, у файлі
"""
from collections import Counter

filename = 'numbers.txt'

def num_counter(filename, n):
    with open(filename, 'r', encoding='utf-8') as file:
        data = file.read()

    counter = Counter([int(i) for i in data.split(',')])
    print(counter)
    ordered = counter.most_common(len(counter))
    print(ordered)
    return [item for item, _ in ordered[:n]], [item for item, _ in ordered[-n:]]

result = num_counter(filename, 10)
print(result)

item, _ = (65, 128)
print(item)
print(_)