# working with class and instance data


class InstanceCounter:

    count = 0

    def __init__(self, val):
        self.value = val
        InstanceCounter.count += 1
        # The count is a class attribute and thus called with the class name
        # because, assuming that count is a global variable, and we have 
        # count as a class attribute just as we do have now, then we'd have a
        # conflict

    def set_val(self, val):
        self.value = val

    def get_val(self):
        return self.value

    def get_count(self):
        return InstanceCounter.count




a = InstanceCounter(5)
b = InstanceCounter(10)
c = InstanceCounter(3)


for i in (a, b, c):
    print(f"value of object: {i.get_val()}")
    print(f"count: {i.get_count()}")

