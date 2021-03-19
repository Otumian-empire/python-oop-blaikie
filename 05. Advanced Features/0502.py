# Inheriting from built-ins

# Inherite the dict class and implement the __setitem__ method


class NumberDict(dict):
    """ This is dictionary that only take numbers (int and float) as value """

    def __setitem__(self, key, value):
        if type(value) in [int, float]:
            dict.__setitem__(self, key, value)
        else:
            raise ValueError("Integer or Float value required")


# ndict = NumberDict()

# ndict['one'] = 1
# # ndict['two'] = 'two'  # This will raise a ValueError

# print(ndict)


# Inherite the list class and modify the __setitem__ and __getitem__ methods
# So that that the index starts at 1 and not 0

class OneIndexedList(list):
    def __setitem__(self, index, value):
        if index == 0:
            raise IndexError("Index starts at 1")
        if index > 0:
            index -= 1

        list.__setitem__(self, index, value)

    def __getitem__(self, index):
        if index == 0:
            raise IndexError("Index starts at 1")
        if index > 0:
            index -= 1

        return list.__getitem__(self, index)


nlist = OneIndexedList([1, 2, 3])
print(nlist)

nlist.append(4)
print(nlist)

print(nlist[1], nlist[4])