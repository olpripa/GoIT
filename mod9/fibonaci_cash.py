from functools import cache


@cache
def fibonacci_nocache(n):
    if n <= 1:
        return n
    return fibonacci_nocache(n - 1) + fibonacci_nocache(n - 2)


print(fibonacci_nocache(10))

print(fibonacci_nocache(15))


def fibonacci_cache():
    cache = {0: 0, 1: 1, 2: 3, }

    def fibonacci(n):
        if n in cache:
            return cache[n]
        else:
            cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
            return cache[n]
    return fibonacci


print(fibonacci_cache(90))
print(fibonacci_cache(100))
