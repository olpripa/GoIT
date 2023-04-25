"""
Іменовані кортежі
Клас collections.namedtuple дозволяє створити тип даних, що поводиться як кортеж з можливістю привласнити кожному
елементу ім'я, яким надалі можна отримати доступ
"""

import collections

Point = collections.namedtuple('Point', ['x', 'y', 'z'])

p = Point(1, 2, 3)
print(p.x)
print(p.y)
print(p.z)

Cat = collections.namedtuple('Cat', ['nickname', 'age', 'owner'])

cat = Cat('Pyshok', 3, 'Ivan')
print(Cat.__name__)
print(cat)
print(type(cat))
print(f'Цей кіт: {cat.nickname}, його вік: {cat.age} і його власник: {cat.owner}')