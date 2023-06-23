#  Іменовані декоратори

def greeting_decorator(name):
    def wrapper(func):
        def inner(x, y):
        # def inner(*args, **kwargs):
            print(f'Decorator: {name}')
            return func( x, y, name)
        return inner
    return wrapper


# @greeting_decorator('My named decorator!!!!!')
def add(x, y, name=None):
    print(f'!!!{name}')
    return x + y


print(add(3, 5))