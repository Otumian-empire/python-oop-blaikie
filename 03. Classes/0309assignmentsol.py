# Assignment

class MaxSizeList:

    def __init__(self, size):
        self.size = size
        self.list_obj = []

    def push(self, val):
        self.list_obj.append(val)

        if len(self.list_obj) > self.size:
            del self.list_obj[0]

    def get_list(self):
        return self.list_obj


a = MaxSizeList(3)

a.push('hey')
a.push('hi')
a.push('let\'s')
a.push('go')

print(a.get_list())
