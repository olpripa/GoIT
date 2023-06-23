# Написати функцію для визначення, чи є число простим?
def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    for item in range(2, n):
        if n % item == 0:
            return False
    return True


def main():
    value = int(input('Введіть число: '))
    if is_prime(value):
        print(f'{value} - просте число')
    else:
        print(f'{value} - не є простим числом')

if __name__ == "__main__":
    main()