# Advanced features

# Iplementing core syntax

# Our classes can respond to core syntax features
# - operators: +, -, *, /, in
# - built-in functions: len and str
# - looping
# - subscripts and slices
# core syntax features translate to "magic" method calls


# Concatenating strings

# firstname = 'Dan '
# lastname = 'Ammy'

# fullname = firstname + lastname
# print(fullname)
# The above is the same as ,
# fullname = firstname.__add__(lastname)
# print(fullname)


# Using magic methods


class SumList:

    def __init__(self, some_list):
        self.this_list = some_list

    def __add__(self, other_sumlist):

        # new_list = []

        # for i in range(len(self.this_list)):
        #     sum_of_list_items = self.this_list[i] + other_sumlist.this_list[i]
        #     new_list.append(sum_of_list_items)

        # new_list = [self.this_list[i] + other_sumlist.this_list[i]
        #             for i in range(len(self.this_list))]

        # new_list = [x + y for x,
        #             y in zip(self.this_list, other_sumlist.this_list)]

        new_list = [sum(pair) for pair in zip(
            self.this_list, other_sumlist.this_list)]

        return SumList(new_list)

    def __repr__(self):
        return str(self.this_list)


a = SumList([1, 2, 3])
b = SumList([3, 4, 5])
c = a + b

print(c)


# Some magic methods - core syntax resolution

'''
"abc" in var    =>    var.__contains__("abc")
var == "abc"    =>    var._eq("abc")
var[1]          =>    var.__getitem__(1)
var[1:3]        =>    var.__getslice__(1, 3)
len(var)        =>    var.__len__()
print(var)      =>    var.__repr__()
'''

# rafekettler.com
