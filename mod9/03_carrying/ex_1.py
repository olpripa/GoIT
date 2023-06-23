# Каррінг - це перетворення функції від багатьох аргументів на набір функцій,
# кожна з яких є функцією від одного аргументу.
# Ми можемо передати частину аргументів у функцію та отримати назад функцію, чекає на інші аргументи.

# def greeting_simple(name, msg):
#     return f'{name} - {msg}'
#
# print(greeting_simple('Ivan', 'Go to Home!'))

def greeting(name):
    def message(msg):
        return f'{name} - {msg}'
    return message

msg_for_ivan = greeting('Ivan')
print(msg_for_ivan('Go to home!'))
print(msg_for_ivan('Go to work!'))

msg_for_oksana = greeting('Oksana')
print(msg_for_oksana('Go to home!'))
print(msg_for_oksana('Go to work!'))