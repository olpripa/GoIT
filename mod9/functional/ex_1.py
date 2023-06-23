# Лямбда функція

def normal(x):
    return x ** 2


sq = lambda x: x ** 2
print(normal(5))
print(sq(5))
print((lambda x: x ** 2)(5))
print((lambda: 'TODO: Fix me')())