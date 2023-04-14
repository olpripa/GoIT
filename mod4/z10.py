# Завдання 10
from random import randint


def get_random_password():
    ascii_st = 40
    ascii_end = 126
    pass_list = []

    while len(pass_list) < 8:
        pass_list.append(chr(randint(ascii_st, ascii_end)))
    return "".join(map(str, pass_list))

def is_valid_password(password):
    if len(password) < 8:
        return False  # print("Password is short")
    elif password.lower() == password or password.upper() == password:
        return False  # print ('no Upper or lower char')
    for ch in password:
        if ch.isdigit():
            return True
    return False

def get_password():
    n = 100
    for i in range(n):
        password = get_random_password()
        if is_valid_password(password):
            return password
    else:
        print (f'за {n} ітерацій надійний пароль не згенеровано')
        
print(get_password())
