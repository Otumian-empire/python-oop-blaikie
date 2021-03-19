# Private variable names
# Variable naming - PEP8
# module names = all_lower_case
# class and exception names = CamelCase
# global and local name = all_lower_case
# function names = all_lower_case
# constants = ALL_CAPS

# variable naming with public and private
# public attributes/variables = regular_lower_case
# private (internal use only by module or class) = _single_leading_underscore
# private (should not be sub classed) = __double_leading_underscore
# magic attributes = __double_underscore__ (use them but don't create them)


class GetSet:
    instance_count = 0
    __mangled_val = 'no privacy'

    def __init__(self, value):
        self._val = value
        GetSet.instance_count += 1

    @property
    def var(self):
        return self._val

    @var.setter
    def var(self, value):
        self._val = value

    @var.deleter
    def var(self):
        self._val = None


gs = GetSet(12)

gs.var = 90

print(gs._val)
print(gs.var)
print(gs._GetSet__mangled_val )
