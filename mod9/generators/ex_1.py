# Найпростіший генератор
def simple_gen():
    yield 'First'
    yield 'Second'


for element in simple_gen():
    print(element)