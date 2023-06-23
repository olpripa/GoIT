class Singleton:
    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance

    def __init__(self, value):
        self.value = value



foo = Singleton(10)
baz = Singleton(20)
bar = Singleton(100)
bar1 = Singleton(1000)

print(foo.value)
print(baz.value)
print(bar.value)
print(bar1.value)

print(foo, baz, bar, bar1)