class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


prod = Product('Book', 155)
print(prod)
print(f'{prod.name} : {prod.price}')


class Foo:  # клас наслідується від Foo(Object)
    def __new__(cls, * args):
        print('Метод ')
        print(args)
        # cls - екземпляр нашог окласу
        isinstance = super(Foo, cls).__new__(cls)

        return isinstance

    def __init__(self, value):
        print('Construktor')
        self.value = value


class Baz(Foo):
    def __init__(self, value):
        super().__init__(value)


class FileWrite:
    def __init__(self, filename):
        self.file = None
        self.opened = False
        self.filename = filename

    def __enter__(self):
        self.vile = open(self.filename, 'W')
        self.opened = True
        return self.file
    
    def __exit__(self, exc_type, exc_val? exc_tb):
        if self.opened:
            self.file.close()
            self.opened = False

if __name__ = "__main__":
