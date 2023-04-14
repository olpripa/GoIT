pool = 1000
try:
    quantity = int(input("Enter the number of mailings: "))
    chunk = pool / quantity
except ZeroDivisionError:
    print('Divide by zero completed!')
except ValueError:
    print('Your input not number ')