# Порахувати суму всіх аргументів
def sum(start, *args):
    sum = start
    for element in args:
        sum = sum + element
        # sum += element
    return sum


result = sum(2, 3, 5, 8, 15)
print(result)