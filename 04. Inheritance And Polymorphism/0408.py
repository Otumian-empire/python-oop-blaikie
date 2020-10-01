# Method overloading - extemding and providing implementations


import abc


class GetSetParent:
    __metaclass__ = abc.ABCMeta

    def __init__(self, val):
        self.value = 0

    def set_val(self, val):
        self.value = val

    def get_val(self):
        return self.value

    @abc.abstractmethod
    def show_doc(self):
        return


class GetSetInt(GetSetParent):

    def set_val(self, val):
        if type(val) != int:
            val = 0
        super(GetSetInt, self).set_val(val)

    def show_doc(self):
        print(f"GetSetInt object, ({id(self)}) only accepts integer values")


# x = GetSetInt(12)
# x.set_val(4)
# print(x.get_val())
# x.show_doc()


class GetSetList(GetSetParent):

    def __init__(self, val=0):
        self.values = [val]

    def get_val(self):
        return self.values[-1]

    def get_vals(self):
        return self.values

    def set_val(self, val):
        self.values.append(val)

    def show_doc(self):
        print(f"GetSetList object, len ({len(self.values)}) stores "
              "history of values set")
