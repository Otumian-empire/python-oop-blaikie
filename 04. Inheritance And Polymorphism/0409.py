# Conposition vs Inheritance

# Inheritance can be brittle (a change may require changes elsewhere)
# Decouple code is classes, functions, etc that work independently and
# don't depend on one another
# As long as interface is maintained, interactions between classes will
# work
# Not checking or requiring particular types is polymorphic and pythonic

# this is a python2 code
import random
import StringIO


class WriteMyStuff:

    def __init__(self, writer):
        self.writer = writer

    def write(self):
        write_text = "hello there!!"
        self.writer.write(write_text)


file_handler = open('text.txt', 'w')
my_writer = WriteMyStuff(file_handler)

my_writer.write()
file_handler.close()


string_io_handler = StringIO.StringIO()
my_writer_s = WriteMyStuff(string_io_handler)
my_writer_s.write()


print("file object:", {open('text.txt', 'r').read()})
print("string IO object:", {string_io_handler.getvalue()})
