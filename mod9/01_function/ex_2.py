# Функція як об'єкт першого класу
# Друга вимога - Функція може бути передана в іншу функцію як аргумент

def mul(a, b):
    return a * b

def add(a, b):
    return a + b

def ops(a, b, func):  # func - передаємо якусь ф-цію як параметр
    return func(a, b)


result = ops(2, 3, mul)
print(result)

result = ops(2, 3, add)
print(result)