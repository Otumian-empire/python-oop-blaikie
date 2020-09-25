# encapsulation
class MyClass:

    def set_val(self, val):
        self.value = val

    def get_val(self):
        return self.value


a = MyClass()
b = MyClass()

a.set_val(23)
b.set_val(100)

# we could have done instance.value = some_value
# since there is no restriction but using the set_val and get_val
# ensures the integrity of the instances state

# print(a.get_val())
# print(b.get_val())


# Consider another example
class MyInteger:

    def set_val(self, val):
        try:
            val = int(val)
        except ValueError:
            return

        self.value = val

    def get_val(self):
        return self.value

    def increment_val(self):
        self.value += 1


# i = MyInteger()
# i.set_val(8)
# print(i.get_val())
# i.set_val('Hi')
# print(i.get_val())

# encapsulate is a voluntary restriction in python but
# do not implemented data hiding
