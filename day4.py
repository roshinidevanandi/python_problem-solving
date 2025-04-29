# Inheritance:
# Inheritance allows a class (child class) to acquire properties and methods of another class (parent class).

# single inheritance:

class A:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        print(f"addition of two numbers is:{self.a+self.b}")

class B(A):
    def sub(self):
        print(f"subtraction of two numbers is:{self.a-self}")
a1=A(8,6)
a2=A(9,3)

a1.add()