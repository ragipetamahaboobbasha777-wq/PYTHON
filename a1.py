class A:
    def display_A(self):
        print("from class-A")
class B(A):
    def display_B(self):
        print("from class-B")
class C(B):
    def display_C(self):
        print("from class-C")
S=C()
S.display_A()
S.display_B()
S.display_C()