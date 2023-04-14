'''
Метод: split

Напишемо універсальну функцію get_parameters, яка повертатиме словник з даними.
Оскільки в першому рядку розділювач символ `;` а на другий `&`,
тому тут вдало підійде випадок (a|b - відповідає a або b)
'''

import re

url_query = "20850=ot-25-mp-do-47-mp;23777=6-6-5;38435=8-gb;41404=16gb"  # ;

url_search = "q=Cat+and+dog&ie=utf-8&oe=utf-8&aq=t"  # &

url = 'data=value*data_1=value_2'
url_test = 'data=value%data_1=value_2*ddd=qwerty'


def get_parameters(data: list) -> dict:
    obj_query = {}
    for el in data:
        key, value = el.split('=')
        obj_query.update({key: value.replace('+', ' ')})
    return obj_query


# temp = url_query.split(';')
# print(get_parameters(temp))


data = re.split(r';|&', url_query)
print(data)
data = re.split(r';|&', url_search)
print(data)
data = re.split(r'\*|&|;|%', url_test)
print(data)
