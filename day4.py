# Inheritance:
# Inheritance allows a class (child class) to acquire properties and methods of another class (parent class).

# single inheritance:

# class A:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def add(self):
#         print(f"addition of two numbers is:{self.a+self.b}")

# class B(A):
#     def sub(self):
#         print(f"subtraction of two numbers is:{self.a-self.b}")
# a1=B(8,6)
# a2=B(9,3)
# a1.add()
# a1.sub()


# muiltiple inheritance:

# class A:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def add(self):
#         print(f"addition of two numbers is:{self.a+self.b}")

# class B:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def sub(self):
#         print(f"subtraction of two numbers is:{self.a-self.b}")

# class C(A,B):
#     def mul(self):
#         print(f"Multiplication of two numbers is:{self.a*self.b}")

# a1=C(8,6)
# a2=C(9,3)
# a1.add()
# a1.sub()
# a1.mul()


# multi-level inheritance:


class A:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        print(f"addition of two numbers is:{self.a+self.b}")

class B(A):
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def sub(self):
        print(f"subtraction of two numbers is:{self.a-self.b}")

class C(B):
    def mul(self):
        print(f"Multiplication of two numbers is:{self.a*self.b}")


a1=C(8,6)
a2=C(9,3)
a1.add()
a1.sub()
a1.mul()


# Hierarchical inheritance:


class Animal:
    def speak(self):
        print("Animal speaks")

# Derived class 1
class Dog(Animal):
    def bark(self):
        print("Dog barks")

# Derived class 2
class Cat(Animal):
    def meow(self):
        print("Cat meows")

# Using the classes
d = Dog()
d.speak()   # Inherited from Animal
d.bark()    # Defined in Dog

c = Cat()
c.speak()   # Inherited from Animal
c.meow()    # Defined in Cat
