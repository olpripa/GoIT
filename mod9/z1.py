# 1 функція в змінну 

def mul(a, b):
    return a * b

f = mul #збереження ф-ції у змінній

result = f(5, 3) #викликаємо фуцію через змінну
print(result)

field = {
    'x': 5,
    'y': 10,
    'op': f
}

n = field.get('op')

print(n)

result = field.get('op') (2, 5)
print(result)


# 2 Функція у функцію

def add (a, b):
    return a + b

def ops(a, b, func):
    return func(a, b)


result = ops(4, 4, mul)
print(result)