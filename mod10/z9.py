from collections import UserString
from collections import UserDict, UserList


class LookUpKeyDict(UserDict):
    def lookup_key(self, value):
        keys = []
        for key in self:
            if self[key] == value:
                keys.append(key)
        return keys


class AmountPaymentList(UserList):
    def amount_payment(self):
        sum = 0
        for value in self:
            if value > 0:
                sum = sum + value
        return sum


d = AmountPaymentList([-5, 5, 8, 10, 12])
# d = [-5, 5, 8, 10, 12]
print(d)
print(d.amount_payment())


class NumberString(UserString):
    def number_count(self):
        return len(list(filter(str.isdigit, str(self))))


str_d = NumberString("123fadss4dfaasee5678jjj9")
print(str_d.number_count())
