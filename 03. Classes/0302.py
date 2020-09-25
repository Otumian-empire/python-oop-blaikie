# defining a class
class MyClass:
    pass


# An instance of the empty class
my_class_instant = MyClass()
print(my_class_instant)

# Another instance of the empty class
another_my_class_instant = MyClass()
print(another_my_class_instant)

# the address of both insatnce change


# a class with a class variable (all instances of the class can access it)
class MyClassVar:
    var = 10

var_class_1 = MyClassVar()
print(var_class_1.var)

var_class_2 = MyClassVar()
print(var_class_2.var)


# 6 point in understanding classes
# - an instance of a class know what class it belongs to
# - variables/attributes defined in the class are available to all instances
# - a method on an instance passes the instance as the first argument to
#    the method (named self)
# - instances have their own data, called instance attributes/variables
# - when an attribute is read, python searched for it in the instance first
#    then in the class
