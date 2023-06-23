import re
from collections import UserDict
from datetime import datetime

class AddressBook(UserDict):
    def add(self, record):
        self.data[record.name.value] = record

    def iterator(self, item_number):
        counter = 0
        result = ''
        for item, record in self.data.items():
            result += f'{item}: {str(record)}'
            counter += 1
            if counter >= item_number:
                yield result
                counter = 0
                result = ''

class Field:
    def __init__(self, value):
        self.__value = None
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value

    def __str__(self):
        return f'...'

class Birthday(Field):
    @Field.value.setter
    def value(self, value):
        self.__value = datetime.strptime(value, '%d%m%Y').date()

class Record:
    def __init__(self, name, phones, birthday=None):
        self.name = name
        self.birthday: Birthday = birthday

    def days_to_birthday(self):
        if not self.birthday:
            return
        now = datetime.now()
        if (self.birthday.value.replace(year=now.year) - now).days > 0:
            return (self.birthday.value.replace(year=now.year) - now).days
        return (self.birthday.value.replace(year=now.year + 1) - now).days

    def __str__(self):
        return f''


class Phone(Field):

    def __init__(self, value):
        super().__init__(value)
        self.phone_number = ''

    @Field.value.setter
    def set_value(self, value):
        if not re.match(r'^\+38\d{10}$', value):
            raise ValueError("Phone number should be in the format +380XXXXXXXXX")
        self.phone_number = value