def fibonacci(n, i=2, Fn_1=1, Fn_2=0):
    if n < 2:
        return n
    if n == i:
        return Fn_1 + Fn_2
    return fibonacci(n, i+1, Fn_1 + Fn_2, Fn_1)


print(f"F = {fibonacci(55)}")
