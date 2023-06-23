# Функція як об'єкт першого класу
# Перша вимога - Функція може бути збережена у змінній чи структурі даних

def mul(a, b):
    return a * b

f = mul  # збереження ф-ції у змінній
result = f(5, 3)  # Викликаємо ф-цію через змінну
# print(result)

field = {
    'x': 5,
    'y': 10,
    'operation': f
}

n = field.get('operation')
print(n)

result = field.get('operation')(field.get('x'), field['y'])  # field.get('operation') -> mul (field.get('x'), field['y'])
print(result)

result = field.get('operation')(3, 5)
print(result)