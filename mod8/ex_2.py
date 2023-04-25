"""
LIFO (англ. last in, first out, "останнім прийшов - першим пішов") - спосіб організації даних або іншими словами
Стек (Stack). У структурованому лінійному списку, організованому за принципом LIFO,
елементи можуть додаватися та вибиратися з одного кінця, званого «вершиною списку».
"""

from collections import deque

MAX_LEN = 5
lifo = deque(maxlen=MAX_LEN)

def push(el):
    lifo.appendleft(el)


def pop():
    return lifo.popleft()


push('Vova')
push('Maria')
push('Ivan')
push('Petro')
push('Oxana')
print(lifo)
name = pop()
print(name)
print(lifo)