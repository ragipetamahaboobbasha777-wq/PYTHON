class A:
    def display_A(self):
        print("from class-A")
class B(A):
    def display_B(self):
        print("from class-B")
class C(A):
    def display_C(self):
        print("from class-C")
S=B()
P=C()
S.display_A()
S.display_B()
P.display_C()