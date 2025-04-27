# classes and object

# Class Variable (species): Shared by all instances of the class. Changing Dog.species affects all
#  objects, as it’s a property of the class itself.

# Instance Variables (name, age): Defined in the __init__ method. Unique to each instance 
# (e.g., dog1.name and dog2.name are different).

# Accessing Variables: Class variables can be accessed via the class name (Dog.species) or an 
# object (dog1.species). Instance variables are accessed via the object (dog1.name).

# Updating Variables: Changing Dog.species affects all instances. Changing dog1.name only affects
# dog1 and does not impact dog2.

# Python Inheritance
# Inheritance allows a class (child class) to acquire properties and methods of another 
# class (parent class).

# 1 Single Inheritance: A child class inherits from a single parent class.

class Dog:
    def __init__(self, name):
        self.name = name

    def display_name(self):
        print(f"Dog's Name: {self.name}")

class Labrador(Dog):  # Single Inheritance
    def sound(self):
        print("Labrador woofs")
        
lab = Labrador("Buddy")
lab.display_name()
lab.sound()

# 2.Multiple Inheritance: A child class inherits from more than one parent class.

class Dog:
    def __init__(self, name):
        self.name = name

    def display_name(self):
        print(f"Dog's Name: {self.name}")

class Labrador(Dog):  
    def sound(self):
        print("Labrador woofs")

class GuideDog(Labrador):
    def guide(self):
        print(f"{self.name}Guides the way!")

class Friendly:
    def greet(self):
        print("Friendly!")

class GoldenRetriever(Dog, Friendly):  # Multiple Inheritance
    def sound(self):
        print("Golden Retriever Barks")

retriever = GoldenRetriever("Charlie")
retriever.display_name()
retriever.greet()
retriever.sound()


# Multilevel Inheritance: A child class inherits from a parent class, which in turn inherits
#  from another class.

class Dog:
    def __init__(self, name):
        self.name = name

    def display_name(self):
        print(f"Dog's Name: {self.name}")

class Labrador(Dog): 
    def sound(self):
        print("Labrador woofs")

class GuideDog(Labrador):  # Multilevel Inheritance
    def guide(self):
        print(f"{self.name}Guides the way!")

guide_dog = GuideDog("Max")
guide_dog.display_name()
guide_dog.guide()