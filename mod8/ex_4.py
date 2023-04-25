"""
Напишіть функцію, яка приймає на вхід три
цілих числа: день, місяць та рік. Функція має повертати порядковий
номер заданого дня у вказаному році.

Результат функції: номер року та порядковий номер дня у цьому
році - обидва у цілісному форматі.
"""
from datetime import datetime, date

def transfer_to_date(day, month, year):
    d = date(year, month, day).toordinal()
    diff = d - date(year, 1, 1).toordinal() + 1
    return year, diff

print(transfer_to_date(20, 4, 2023))
print(transfer_to_date(31, 12, 2022))


"""
Розробіть функцію, яка приймає як єдиний параметр порядкову дату, що включає в себе рік і день
по порядку. Як результат функція повинна повертати день і місяць, що відповідають переданій порядковій даті.
"""

def transform_to_date(ordinal, year):
    d = date(year, 1, 1).toordinal()
    d = datetime.fromordinal(d - 1 + ordinal)
    return d

print(transform_to_date(110, 2023))
print(transform_to_date(365, 2022))