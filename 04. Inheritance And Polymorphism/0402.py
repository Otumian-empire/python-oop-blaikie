# Example of inheritance


class Animal:

    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print(f"{self.name} is eating {food}")


class Dog(Animal):

    def fetch(self, thing):
        print(f"{self.name} goes after the {thing}")


class Cat(Animal):

    def swatstring(self):
        print(f"{self.name} shreds the string")


thomas = Dog('Thomas')
patrick = Cat('Patrick')

thomas.fetch('paper')
patrick.swatstring()

thomas.eat('Pizza and Sliced cheese')
patrick.eat('Baked beans and Potato stew with banana toppings')

thomas.swatstring()
