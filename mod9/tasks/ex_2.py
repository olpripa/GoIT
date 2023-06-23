"""
Генератор повернення, який повертає ціле число між min_val та max_val у нескінченному циклі
"""

from random import randint, seed

def cycle_random_generator(min_val, max_val):
    seed()
    while True:
        yield randint(min_val, max_val)


rand_generator = cycle_random_generator(5, 15)  # вічний генератор
result = []

for _ in range(200):
    result.append(next(rand_generator))

print(result)



