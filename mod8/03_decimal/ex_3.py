# Створення Decimal із дійсних чисел

from decimal import Decimal

num1 = 1.37
num2 = 1.5

first = Decimal.from_float(num1)
second = Decimal.from_float(num2)
print(first, second)

first = Decimal(num1)
second = Decimal(num2)
third = Decimal(1.37)
print(first, second, third)

first = Decimal(str(num1))
second = Decimal(str(num2))
third = Decimal(str(1.37))
print(first, second, third)