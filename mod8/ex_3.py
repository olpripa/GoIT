"""
FIFO (англ. first in, first out - "першим прийшов - першим пішов") - спосіб організації даних або іншими словами черга.
Цей вислів описує принцип технічної обробки черги або обслуговування
конфліктних вимог шляхом упорядкування процесу за принципом: "першим прийшов - першим обслужений".
Той, хто приходить першим, той і обслуговується першим, хто прийде наступним чекає,
поки обслуговування першого не буде закінчено, і так далі.
"""

from collections import deque

MAX_LEN = 10
fifo = deque(maxlen=MAX_LEN)

def push(el):
    fifo.append(el)

def pop():
    return fifo.popleft()


push('Vova')
push('Maria')
push('Ivan')
push('Petro')
push('Oxana')
push('Katia')
push('Oleg')
print(fifo)
name = pop()
print(name)
print(fifo)

