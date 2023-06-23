# Filter

payments = [100, -3, 3, -35, -5]


def is_negative_number(num: int) -> bool:
    if num < 0:
        return True
    return False

p_values = filter(is_negative_number, payments)
print(list(p_values))

p_values = filter(lambda num: num < 0, payments)
print(list(p_values))