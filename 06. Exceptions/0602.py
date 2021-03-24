# Custom Exceptions

class MyError(Exception):

    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = ''

    def __str__(self):
        if self.message:
            return f"Error message: {self.message}"
        return "MyError Exception"


print(MyError())

print(MyError('The was no name', 3))

# raise MyError("This is a raised error")
