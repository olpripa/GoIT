# Написати калькулятор
# fn('+') -> sum  fn('*') -> mul

def calc(operation: str):
    result = None
    if operation == "+":
        result = 0
    if operation == "*":
        result = 1
    if result is None:
        return 'Функція не підтримує операцію'

    value = input('Введіть ціле число: ')

    while True:
        if value == '':
            break
        elif operation == "+":
            result += int(value)  # 0 + 2 + 3 + 4
        elif operation == "*":
            result *= int(value)
        value = input('Введіть ціле число: ')
    return result


result = calc('*')
print(result)
