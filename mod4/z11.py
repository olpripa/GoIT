# Завдання 11

def is_valid_password(password):
    if len(password) < 8:
        return False  # print("Password is short")
    elif password.lower() == password or password.upper() == password:
        return False  # print ('no Upper or lower char')
    for ch in password:
        if ch.isdigit():
            return True
    return False


print(is_valid_password(''))
