"""
Яку мінімальну кількість разів ви повинні підкинути монетку, щоб тричі поспіль
випав чи орел, чи решка?
random.randint(A, B) - випадкове ціле число N, A ≤ N ≤ B.
"""

import random

d = {
    1: 'Орел',
    2: 'Решка'
}
count_O = 0  # лічильник для Орел
count_P = 0  # лічильник для Решка

sequence = []

while count_O < 3 and count_P < 3:
    trial = random.randint(1, 2)
    if trial == 1:
        count_O += 1
        count_P = 0
    else:
        count_P += 1
        count_O = 0
    sequence.append(d[trial])


print(f'Отримана послідовність: {sequence}')
if count_O == 3:
    print("Випало три Орли поспіль")
else:
    print("Випало три Решки поспіль")

print(f'Кількість спроб {len(sequence)}')