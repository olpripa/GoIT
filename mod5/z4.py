def is_check_name(fullname, first_name):
    if fullname == fullname.removeprefix(first_name):
        return False
    else:
        return True

print(is_check_name('Oleksandr Pripa', 'Oleksandr'))