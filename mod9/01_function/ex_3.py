# Функція як об'єкт першого класу
# Третя вимога - функція може бути повернена з функції як результат

def mul(a, b):
    return a * b

def add(a, b):
    return a + b

def ops(operator: str):
    if operator == '*':
        return mul
    elif operator == '+':
        return add
    else:
        raise ValueError('Operator not supported')


try:
    func_mul = ops('*')  # func_mul = mul
    print(func_mul)
    result = func_mul(2, 4)
    print(result)
except ValueError:
    print('Operator "*" failed')

try:
    func_add = ops('+')  # func_mul = mul
    print(func_add)
    result = func_add(2, 4)
    print(result)
except ValueError:
    print('Operator "+" failed')

try:
    func_div = ops('/')  # func_mul = mul
    print(func_div)
    result = func_div(2, 4)
    print(result)
except ValueError:
    print('Operator "/" failed')