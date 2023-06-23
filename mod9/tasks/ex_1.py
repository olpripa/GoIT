"""
Напишіть decorator, який записує в консоль два повідомлення журналу:

: call [номер_виклику_функції]: [ім'я функції][її аргументи]\n
: result: [ім'я функції][результат]\n
"""
import sys
# test = {
#     func.__name__: call_count
# }

# decorator
def logger(func):
    call_count = 0
    def inner(*args, **kwargs):
        nonlocal call_count
        call_count += 1
        sys.stdout.write(f"call: [{call_count}]: [{func.__name__}][{args}]\n")
        result = func(*args, **kwargs)
        sys.stdout.write(f"result: [{func.__name__}][{result}]\n")
        # return result
    return inner

@logger
def mul(a, b):
    return a * b

@logger
def add(a, b, c):
    return a + b + c

mul(4, 8)
mul(5, 8)
mul(3, 3)
add(4, 8, 15)