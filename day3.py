# Example1:

# class and object

# class Movie:
#     def __init__(self,name,hero,release_date):
#         self.name=name
#         self.hero=hero
#         self.release_date=release_date
#     def release(self):
#         print(f"The {self.name} movie hero is {self.hero} and movie released in {self.release_date}")


# m1=Movie("salar","prabhas",2023)
# m2=Movie("hit","nani",2025)

# m1.release()       
# m2.release()


# class Student:
#     def __init__(self,m1,m2,m3):
#         self.m1=m1
#         self.m2=m2
#         self.m3=m3

#     def avg(self):
#         return (self.m1+self.m2+self.m3)/3

# std1=Student(65,86,98)
# std2=Student(64,82,99)
# print(std1.avg())
# print(std2.avg())


# Example2: class methods and class variables

# class Student:
#     school="ZPHS SCHOOL"
#     def __init__(self,m1,m2,m3):
#         self.m1=m1
#         self.m2=m2
#         self.m3=m3

#     def avg(self):
#         return (self.m1+self.m2+self.m3)/3
    
#     @classmethod
#     def info(cls):
#         print(cls.school)

# std1=Student(65,86,98)
# std2=Student(64,82,99)
# print(std1.avg())
# print(std2.avg())
# Student.info()


# Example 3: static method

# class Student:
#     school="ZPHS SCHOOL"

#     def __init__(self,m1,m2,m3):
#         self.m1=m1
#         self.m2=m2
#         self.m3=m3

#     @staticmethod
#     def school_info():
#         print("helo i am roshini")
        
# std1=Student(43,23,89)
# std2=Student(43,34,21)
# Student.school_info()  



# compare two objects are the same or not       

# class Employee:

#     def __init__(self):
#         self.name="rosy"
#         self.age=22

#     def compare(self,other):
#         if self.age==other.age:
#             return True
#         else:
#             return False
        

# emp1=Employee()
# emp1.age=23
# emp2=Employee()

# if emp1.compare(emp2):
#     print("both are the same")
# else:
#     print("both are the different")


# Example 4:


class Car:
    wheels=4

    def __init__(self):
        self.mil=10
        self.com="BMW"

c1=Car()
c2=Car()

print(c1.mil)
print(c1.com)
print(Car.wheels)


# Example 5:

# Accessor Methods:
# If you want to get the variable you have to use the accessor method

# Mutator Methods:
# If you want to modifies any change we use set method is called mutator method



# class Student:
#     def __init__(self,m1,m2,m3):
#         self.m1=m1
#         self.m2=m2
#         self.m3=m3

#     def avg(self):
#         return (self.m1+self.m2+self.m3)/3
    
#     def get_m1(self):
#         print(self.m1)

    
#     def set_m1(self,value):
#         self.m1=value
#         print(self.m1)

# std1=Student(65,86,98)
# std2=Student(64,82,99)
# print(std1.avg())
# print(std2.avg())


# std1.get_m1()

# std1.set_m1(99)