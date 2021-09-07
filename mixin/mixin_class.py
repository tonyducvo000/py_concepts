
class A:
    def foo(self):
        print("Hello from A")

class B(A):
    def foo(self):
        print("Hello from B")

class C(A):
    def foo(self):
        print("Hello from C")

class D(C, B):
    pass

objD = D()
objD.foo()
