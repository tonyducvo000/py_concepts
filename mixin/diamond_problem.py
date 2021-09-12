# Program to demonstrate the "diamond problem".
# This problem arises due to multiple inheritance and the ambiguity which property/method to inherit.

# Parent class.
class A:
    def foo(self):
        print("Hello from A")

# Subclass of A.
class B(A):
    def foo(self):
        print("Hello from B")  # Override the method.

# Another subclass of A.
class C(A):
    def foo(self):
        print("Hello from C")  # Override the method.

# D is a Subclass of both C and B, which are both subclasses of A.
# This is an ambiguous inheritance, since D is unsure of which foo() method to inherit.
# Calling foo() method will print "Hello from C".
# If class D(B, C), calling foo() method will print "Hello from B".
class D(C, B):
    pass

objD = D()
objD.foo()
print(D.mro())