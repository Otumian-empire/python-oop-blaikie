# Attribute encapsulation

class ThisClass:
    pass


this = ThisClass()
this.x = 3
this.y = 5
this.z = "I am zee"

# print(this.x, this.y, this.z)

# with this approach the user can add and modify attributes

# Solution will be to use getter and setters


class ThisNewClass:

    def set_val(self, val):
        self.val = val

    def get_val(self):
        return self.val


a = ThisNewClass()
b = ThisNewClass()

a.set_val(3)
b.set_val(9)

# print(a.get_val(), b.get_val())


# Instance attributes can be chnaged anywhere to any value, breaking encapsulation
# getter and setter encourage encapsulation but depends on the users coooperation
# python by design does not enforce privacy

# @property is a decorator that designates an instance attribute as encapsulate-able
# through methods
# Getting and setting and deleting methods can de defined, called automaically when
# the user accesses the attribute
# The name are linked to the attribute name  - the methods, and methods, and setters
# and delete method, must use it
# @property offers some control, but don't try to force the user into certain behaviors
# - it is not pythonic


class GetSet(object):

    def __init__(self, name):
        self.name = name

    @property
    def var(self):
        print("Getter")
        return self.name

    @var.setter
    def var(self, name):
        print("Setter")
        self.name = name

    @var.deleter
    def var(self):
        print("Deleter")
        self.name = None


gs = GetSet('Sam')
gs.var = "Peter"
print(gs.var)

del gs.var

# print(gs.var)
