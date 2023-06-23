"""
Інтерпретатор Python лінивий і якщо його явно не попросити створити копію об'єкта,
він створить новий показник на той же об'єкт. Не завжди така поведінка вітається.
Для створення копії об'єкта у пакеті copy є функції:
- copy - поверхнева копія
- Deepcopy - глибока копія.
"""
from copy import copy, deepcopy

l = [1, 2, 3, ['a', 'b', 'c']]

test_l = l[:]
l_copy = copy(l)
l_deep = deepcopy(l)
print(l == l_copy, l is l_copy, l is l_deep)

l[0] = 9
print(l, test_l, l_copy, l_deep, sep='; ')
l[3][0] = 'd'
print(l, test_l, l_copy, l_deep, sep='; ')
l_deep[3][2] = 'f'
print(l, test_l, l_copy, l_deep, sep='; ')
