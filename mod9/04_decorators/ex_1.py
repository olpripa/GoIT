# Декоратори
# Шаблон проектування, який полягає в тому, щоб розширювати існуючий функціонал,
# не вносячи змін у код цього самого функціоналу.


def greeting(value):
    print(f'My name is {value}!')


def greeting_decorator(func):
    def wrapper(*args, **kwargs):
        print('Hello!')
        result = func(*args, **kwargs)
        print('Bye Bye')
        return result
    return wrapper

greeting('Bob')

change_greeting = greeting_decorator(greeting)  # обгортаємо ф-цію greeting
change_greeting('Alex')