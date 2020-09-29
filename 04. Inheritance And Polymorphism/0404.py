# Inheriting the constructor of a class

import random


class Animal:

    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print(f"{self.name} is eating {food}")


class Dog(Animal):

    def __init__(self, name):
        # super(Dog, self).__init__(name)
        super().__init__(name)
        self.breed = random.choice(['Wallel', 'Dutghert', 'Plumng'])

    def fetch(self, thing):
        print(f"{self.name} goes after the {thing}")


d = Dog('Thomas')

print(d.name)
print(d.breed)
