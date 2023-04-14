def sanitize_phone_number(phone):
    new_phone = (
        phone.strip()
        .removeprefix("+")
        .replace("(", "")
        .replace(")", "")
        .replace("-", "")
        .replace(" ", "")
    )
    return new_phone


def get_phone_numbers_for_countries(list_phones):
    dict_phones = {'UA': [],
                   'JP': [],
                   'TW': [],
                   'SG': []}
    UA_phones = []
    JP_phones = []
    TW_phones = []
    SG_phones = []

    list_phones_g = list(map(sanitize_phone_number, list_phones))
    for ph in list_phones_g:
        if ph.startswith('38'):
            UA_phones.append(ph)
        elif ph.startswith('81'):
            JP_phones.append(ph)
        elif ph.startswith('886'):
            TW_phones.append(ph)
        elif ph.startswith('65'):
            SG_phones.append(ph)
        else:
            UA_phones.append(ph)

    dict_phones.update([('UA', UA_phones), ('JP', JP_phones),
                       ('TW', TW_phones), ('SG', SG_phones)])
    return dict_phones

phones = ['+38 095083 57-67', '    097 8503797',
          '+39 050 434 07 09', '+81 050 4340709']
print(get_phone_numbers_for_countries(phones))