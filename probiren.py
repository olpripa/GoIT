class IsNotTitleException(Exception):
    pass


try:
    rooms = ['Kitchen', 'study', 'Hall', 'Bathroom']
    for room in rooms:
        if room.title() != room:
            raise IsNotTitleException('Fault!')

except IsNotTitleException as exc:
    print(exc)


def logged_func(func):
    def inner(x, y):
        print(f'called with {x}, {y}')
        result = func(x, y)
        print(f'result: {result}')
        return result
    return inner


@logged_func
def complicated(x, y):
    return x / y


complicated(6, 2)


def interval_generator(x, y):
    while x <= y:
        yield x
        x += 1


five_to_ten_generator = interval_generator(5, 10)

next(five_to_ten_generator)  # 5
next(five_to_ten_generator)  # 6
next(five_to_ten_generator)  # 7
next(five_to_ten_generator)  # 8
next(five_to_ten_generator)  # 9
next(five_to_ten_generator)  # 10
