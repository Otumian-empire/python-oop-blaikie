# Multiple inheritance and the look up tree
# This uses a depth first search


class A:

    def do_this(self):
        print('I am A')


class B(A):
    pass


class C:

    def do_this(self):
        print('I am C')


#  multiple inheritance - D inherits from B and C
class D(B, C):
    pass


d_inst = D()
d_inst.do_this()

print(D.mro())
# method resolution order (mro) of D class: D->B->A->C
# depth first search

# For the diamond shape inheritance:
# class A, class B(A), class C(A), class D(B, C)
# method resolution order (mro) of D class: D->B->C->A
# this is not a breadth first search but depth first search
# actually a modified depth first search, that is,
# if the same class appears in the mro, the earlier occurencies
# of this class are removed from the mro
