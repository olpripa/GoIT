# Приклад Декоратора без args, kwargs

def decorator_name(func):
    def wrapper(name, surname):
        result = func(name, surname)
        print('Good bye!')
        return result
    return wrapper


def prefix_decorator_name(func):
    def wrapper(name, surname):
        print('Prefix!!!!!!!')
        name = f'Mr. {name}'
        result = func(name, surname)
        print('Prefix end----------')
        return result
    return wrapper

@prefix_decorator_name
@decorator_name
def full_name(name, surname):
    print(f'Hello {name} {surname}!')



full_name('Микола', 'Петрович')