class Foo:  # class Foo(object)
    def __new__(cls, * args):
        print('Метод new Foo')
        print(args)
        instance = super(Foo, cls).__new__(cls)  # cls - екземплря нашого класу

        return instance

    def __init__(self, value):
        print('Конструктор')
        self.value = value


class Baz(Foo):
    def __init__(self, value):
        super(Baz, self).__init__(value)


baz = Baz(10)
foo = Baz(20)

print(baz.value, foo.value)
print(baz, foo)



