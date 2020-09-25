# class attribute vs instance attribute


class MyClass:
    VAL = 10

    def set_val(self):
        self.val = 100


# inst = MyClass()
# inst.set_val()
# print(inst.val)
# print(inst.VAL)



class MyVal:
    VAL = 10

v = MyVal()
print(v.VAL)

v.VAL = 21
print(v.VAL)

del v.VAL
print(v.VAL)

# this indicates there is an attribute look order
# first in the instance then the class
