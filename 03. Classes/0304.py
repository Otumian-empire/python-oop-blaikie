from random import randint


# Instance attributes/state
class MyClass:

    def dothis(self):
        # print('do this')
        self.rand_val = randint(1, 10)

    def print_rand_val(self):
        print(self.rand_val)


myinst = MyClass()
myinst.dothis()
myinst.print_rand_val()
