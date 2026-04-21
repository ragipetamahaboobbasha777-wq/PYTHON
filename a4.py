class A:
 def display_A(self):
  print("From Class A")
class B:
 def display_B(self):
  print("From Class B")
class C(A,B):
 def display_C(self):
  print("From Class C")
class D(C):
 def display_D(self):
  print("From Class D")
s=C()
p=D()
s.display_A()
s.display_B()
s.display_C()
p.display_D()