# Exception
# Identify exceptions (errors)
# trapping exception using try and except
# trigging exception with raise
# define custom exceptions

# ZeroDivisionError - dividing by zero
# print(5/0)

# NameError - variable name not defined before calling
# name = "dan"
# print(names)

# SyntaxError - missing token
# print('Hello)  # the string was incomplete

# KeyError - accessing a value with a key that does not exist
# mydict = {}
# print(mydict['name'])  # the mydict is no key - name

# IndexError - accessing an index of list that does not exist
# mylist = [1, 2, 3]
# print(mylist[5]) # There are only 3, so the max index is 2


# Most of this errors can be trapped using a try and except
# try:
#     print(5/0)
# except ZeroDivisionError:
#     print("Can not divide by Zero")


# Two or exceptions can be trapped
# try:
#     print(5/0)
# except ZeroDivisionError, ValueError:
#     print("Can not divide by Zero")
