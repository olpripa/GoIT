phone = "+1-234-567-89-10"

edited_phone = phone.replace('-', ' ')
print(edited_phone)

edited_phone = phone.replace('-', '')
print(edited_phone)

edited_phone = phone.replace('-' or '+', ' ', 1)
print(edited_phone)