# Polymorphism
# Polymorphism implies many shapes
# two classes with the same interface (i.e method name)
# methods are different but conceptually the same
# methods have the same name but different implementations


class Animal:

    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print(f"{self.name} is eating {food}")


class Dog(Animal):

    def fetch(self, thing):
        print(f"{self.name} goes after the {thing}")

    def show_affection(self):
        print(f"{self.name} wags tail")


class Cat(Animal):

    def swatstring(self):
        print(f"{self.name} shreds the string")

    def show_affection(self):
        print(f"{self.name} purrs")


thomas = Dog('Thomas')
patrick = Cat('Patrick')

thomas.fetch('paper')
patrick.swatstring()

thomas.eat('Pizza and Sliced cheese')
patrick.eat('Baked beans and Potato stew with banana toppings')

thomas.show_affection()
patrick.show_affection()
