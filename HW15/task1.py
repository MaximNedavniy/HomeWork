class Person:
    def talk(self):
        print(f"Hello, my name is {self.first_name} {self.last_name} and I’m {self.age} years old")

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


person1 = Person("Carl", "Johnson", 26)

person1.talk()