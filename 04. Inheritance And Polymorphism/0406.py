# Decorators, static and class methods

# Instance methods takes self (an instance of the class) as the
# first argument


class Animal:

    # class attribute
    count = 0

    def __init__(self, name):
        self.name = self.scan_name(name)
        Animal.count = Animal.count + 1

    def eat(self, food):
        print(f"{self.name} is eating {food}")

    # this is an instance method because of self
    # but the function does not make use of the self
    # as such it woeks with the class and we can make it
    #  a class method instead
    # def get_count(self):
    #     return Animal.count

    # change self to some name like, cls then annotate the
    # method with, @classmethod and use cls to access/get
    # the class attributes

    # Decorators are special functions that can modify functions
    # @classmethod cause method to pass the class to the method
    # when called instead of the instance

    @classmethod
    def get_count(cls):
        return cls.count

    # class and static methods are not bound to the instance
    # class methods for working with the class
    # static methods for working independently of either the class or
    # the instance

    # __init__, eat and get are instacce methods because they take the instance
    # as first argument

    # static method, annotate with @staticmethod, implement this function as
    # one would implement a normal function
    # one can say that a static method is a utility method

    @staticmethod
    def scan_name(name):
        if type(name) != str:
            name = str(name)

        return name

    # this method is called in the __init__ method to make sure that the name
    # is a string


a = Animal('Ant')
b = Animal('Bear')
c = Animal('Cat')
number = Animal(123)

for animal in [a, b, c, number]:
    print(f"{animal.name}")
    print(f"count: {animal.get_count()}")
