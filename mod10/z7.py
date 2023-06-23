class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight


class Cat(Animal):
    def say(self):
        return "Meow"


class Owner:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def info(self):
        return {"name": self.name, "age": self.age, "adres": self.address}


class Dog(Animal):

    def __init__(self, nickname, weight, breed, owner):
        super().__init__(nickname, weight)

        self.breed = breed
        self.owner = owner

    def say(self):
        return "Woof"

    def who_is_owner(self):
        return self.owner.info()


cat = Cat("lucky", 10)
owner = Owner("Sherlock", 24, "London, 221B Baker Street")
dog = Dog("Barbos", 23, "labrador", owner)

print(dog.nickname)  # Simon
print(dog.breed)  # british
print(dog.weight)  # 10
# print(owner.info())
print(dog.who_is_owner())
