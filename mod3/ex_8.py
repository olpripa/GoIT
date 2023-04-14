# Потрібно написати функцію для вгадування числа
from random import randint

# Потрібно вгадати число від 0 до n

def game(n):
    count = 0  # лічильник (спроб)
    goal = randint(0, n)  # отримуємо ціле число від 0 до n
    while True:
        answer = int(input(f'Вгадайте задумане число від 0 до {n}: '))
        count += 1
        if answer > goal:
            print('Ваше число більше задуманого')
        elif answer < goal:
            print('Ваше число менше задуманого')
        else:
            print(f'Вітаємо! Ви вгадали число за {count} кроків')
            break

if __name__ == "__main__":
    game(10)