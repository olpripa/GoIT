# def greeting(name):
#     def message(msg):
#         return f'{name} - {msg}'
#     return message
# msg_1 = greeting('1')
# msg_2 = greeting('2')

# print(msg_1('Go to home'))


# def taxer(base_tax):
#     def calculate(money):
#         nonlocal base_tax
#         if money > 10000:
#             base_tax = 1.5 * base_tax
#         return money - base_tax * money
#     return calculate

# ukr = taxer(0.1)
# swd = taxer(0.55)
# m_u = ukr(5000)
# m_s = swd(25000)
# print(m_u, m_s)

# словник з функціями
calc = {
    "plus": lambda x,  y:  x + y,
    "minus": lambda x,  y:  x - y,
    "division": lambda x,  y:  x / y,
    # як значення можна використовувати
    # вбудовану функцію pow() або будь-яку
    # функцію користувача
    "power":  pow
}


def action(match,  dictionary,  default="NO CALC"):
    "" "шаблон фабрики функцій"""
    if match in dictionary:
        return dictionary[match]
    return lambda * x:  default


plus = action('plus',  calc)
minus = action('minus',  calc)
# power  =  action ( 'power' ,  calc )
square = action('square',  calc)

print(plus(3, 7))
print(minus(10, 2))
print(square(1, 2))
