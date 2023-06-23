# Методи __repr__ и __str__

class Car:
    store_name = 'GoIT'

    def __init__(self, year, mark, model, color):
        self.year = year
        self.mark = mark
        self.model = model
        self.color = color

    def __str__(self):
        return f'{self.store_name} - {self.mark}.{self.model}: {self.year}, {self.color}'

    def __repr__(self):
        return f'Car({self.year}, "{self.mark}", "{self.model}")'


car = Car(2016, 'Tesla', 'Model X', 'White')
print(car)
print(repr(car))