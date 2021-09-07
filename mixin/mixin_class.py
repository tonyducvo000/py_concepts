# class A:
#     total = 1234
#
#
# class B(A):
#     pass
#
#
# class C(A):
#     pass
#
# # Mixin class
# class M():
#     def print_total(self):
#         print(self.total)
#
#
# class D(B, M):
#     pass
#
#
# class E(B, M):
#     pass
#
# e = E()
# e.print_total()

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