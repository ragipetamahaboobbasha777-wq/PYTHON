class A:
    def display_A(self):
        print("from class-A")
class B(A):
    def display_B(self):
        print("from class-B")
S=B()
S.display_A()
S.display_B()     