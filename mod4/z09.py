def is_valid_pin_codes(pin_codes):
    plur = set(pin_codes)
    if len(pin_codes) == 0:
        return False # Список порожній
    elif len(plur) != len(pin_codes):
        return False #Список не валідний, має дублікати
    for pin in pin_codes:
        try:
            if len(pin)  != 4:
                return False # Список не валідний, містить елементи відмінні від 4х символів
            elif not pin.isdigit():
                print('це не цифри')
                return False  # Список не валідний, містить не цифрофі елементи
        except TypeError:
            return False #Список не валідний, містить не рядки
    return True


# is_valid_pin_codes(['1101', '9034', '0011', '0011'])
# is_valid_pin_codes([])
is_valid_pin_codes(['1101', 3, '0903', '0011', 'tttt', '3333'])
