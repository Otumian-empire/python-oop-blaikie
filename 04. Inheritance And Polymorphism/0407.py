# Abstract (Base) class
# An Abstract class is a kind of a medel for other classes to defined.
# Abstract classes are not designed to be instanciated or to contruct
# instances but to can be extended/subclassed by regular classes
# An Abstract class can define an interface or a method that must be
# defined /implemented by a subclass

# An a simple way, one may say that an Abstract class is a blue print
# for how classes should be designed


import abc


class GetterSetter:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def set_val(self, val):
        ''' Set value in the instance '''
        return

    @abc.abstractmethod
    def get_val(self):
        ''' Get and return value from the instance '''
        return


# methods in abstract classes are required to be implemented
# abtract methods have no implementations


class MyClass(GetterSetter):

    def set_val(self, val):
        self.value = val

    def get_val(self):
        return self.value


# MyClass extends GetterSetter as such we must implement set_val and get_val

m = MyClass()
print(m)
