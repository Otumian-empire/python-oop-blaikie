# With context

# open file and close it
fp = open('Hello.txt', '+a')
print('I am a new text file', file=fp)
fp.close()


# We don't have to close it
with open('Hello.txt', '+a') as op:
    print('I am a new line in the Hello.txt file', file=op)

# seems like not a valid python3 code
# class MyWithClass:

#     def __enter__(self):
#         print("Entered the class")

#     def __exit__(self, type, value, traceback):
#         print("Exit the class")

#     def say_hello(self):
#         print('Hello')


# with MyWithClass as cc:
#     c = cc()
#     c.say_hello()

# print("After the with block")