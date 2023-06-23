# Зробити декоратор, який повертає кортеж з результатом функції обчислення факторіал та часом її виконання

from time import time, sleep

def time_counter(func):
    def interval(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        passed = time() - start
        return result, passed
    return interval

# @time_counter
# def test_func(a, b):
#     sleep(b)
#     return a + b
#
# print(test_func(2, 1))
# print(test_func(4, 2))


@time_counter
def factorial_with_cache(n, cache={}):
    if n < 0:
        raise ValueError("Number cant be negative")

    def calc(n):
        result = 1
        for val in range(1, n + 1):
            if val in cache:
                result = cache[val]
                print(f'{val} in cache {result}')
            else:
                result = val * cache.get(val - 1, 1)
                cache[val] = result
                print(f'{val} not in cache {result}')
        return result

    return calc

f3 = factorial_with_cache(3)

print(f'f3: {f3}')
