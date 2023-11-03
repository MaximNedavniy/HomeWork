class Animal:

    def talk(self):
        return "The animal says something..."


class Dog(Animal):
    def talk(self):
        return "woof woof"


class Cat(Animal):
    def talk(self):
        return "meow"


def talk(object):
    if isinstance(object, Animal):
        return object.talk()
    else:
        return "This animal can't talk."


dog = Dog()
cat = Cat()
print(cat.talk())
print(talk(cat))
print(talk(dog))
print(dog.talk())
