# Порахувати суму всіх чисел через рекурсію
sum = 0

# for num in range(1, 11):
#     sum += num


def sum_numbers(max_num: int) -> int:
    if max_num <= 0:
        return 0
    if max_num == 1:
        return 1
    return max_num + sum_numbers(max_num - 1)


print(sum_numbers(10))
# sum_numbers(10) -> 10 + sum_numbers(9)
# sum_numbers(9) -> 9 + sum_numbers(8)
# sum_numbers(8) -> 8 + sum_numbers(7)
# sum_numbers(7) -> 7 + sum_numbers(6)
# sum_numbers(6) -> 6 + sum_numbers(5)
# sum_numbers(5) -> 5 + sum_numbers(4)
# sum_numbers(4) -> 4 + sum_numbers(3)
# sum_numbers(3) -> 3 + sum_numbers(2)
# sum_numbers(2) -> 2 + sum_numbers(1)
# sum_numbers(1) -> 1
