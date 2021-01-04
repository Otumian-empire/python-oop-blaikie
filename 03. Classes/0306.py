# __init__ constructor
# The constructor set values for attributes at the time the instance is created


class MyInteger:

    def __init__(self, val):
        print('calling __init__')
        try:
            val = int(val)
        except ValueError:
            val = 0
        self.value = val

    def increment_val(self):
        self.value = self.value + 1


# the `__` indicates its a private or magic method

i = MyInteger()
i.increment_val()
i.increment_val()
print(i.value)
