# Inheritance
# The ability to make one class to attain the attributes
# and methods of another class

#  Inheriting Attributes


class MyDate:

    def get_date(self):
        return '2020-09-29'


class MyTime(MyDate):

    def get_time(self):
        return '13:05:34'


my_date_obj = MyDate()

print(my_date_obj.get_date())

my_time_obj = MyTime()
print(my_time_obj.get_date())
print(my_time_obj.get_time())


# Object lookup attribute hierarchy
# The instance
# The class
# Any class from which this is class inherits

# Some inheritance terms
# Super class, Parent class, Inherited class, Base class
# Sub class, Child class, Inheriting class, Derived class
