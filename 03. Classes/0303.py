class Joe:
    greeting = "Hello there, joe"


big_joe = Joe()
print(big_joe.greeting)


# create a method
class JoeMethod:

    # this is an instance method - because the instance is passed the first
    # argument when the method is called
    def call_me(self):
        print('I am the call_me method from the JoeMethod class')


jojo = JoeMethod()
jojo.call_me()  # instance is passed/bound by default
