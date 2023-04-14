def sanitize_phone_number(phone):
    new_phone = phone.replace('+', '').replace('-', '').replace('(', '').replace(')', '').replace(' ', '')
    print(new_phone)
    return new_phone

phones = ["    +38(050)123-32-34", "     0503451234", "(050)8889900", "38050-111-22-22", "38050 111 22 11   "]

for ph in phones:
    sanitize_phone_number(ph)