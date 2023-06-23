# Замикання

# Особливість існування вкладених локальних просторів імен і той факт, що вони створюються динамічно,
# дає можливість використати механізм замикань у Python.

def greeting(name):  # зовнішня ф-ція
    def message(msg):  # внутрішня ф-ція
        return f'{name} - {msg}'
    return message  # повернення внутрішньої ф-ції



msg_for_ivan = greeting('Ivan')  # msg_for_ivan матиме достпу до name через замикання
msg_for_petro = greeting('Petro')
print(msg_for_ivan)
print(type(msg_for_petro))
print(msg_for_ivan('Go to work!'))
print(msg_for_ivan('Go to home!'))


print(msg_for_petro('Go to work!'))
print(msg_for_petro('Go to home!'))

