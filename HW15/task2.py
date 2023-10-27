class Dog:
    age_factor=7
    def human_age(self):
        print(f"The age of the dog is {self.age} years in the human equivalent of {self.age*Dog.age_factor} years")
    def __init__(self, age):
        self.age=age


dalmatian=Dog(10)

dalmatian.human_age()