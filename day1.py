# 1.how to work for loop

fruits=["apple","banana","kiwi"]
iter_obj=iter(fruits)

while True:
    try:
        fruit=next(iter_obj)
        print(fruit)
    except StopIteration:
        break


# 2.print prime numbers in beetween 1 to 100

try:
    for i in range(2,100):
        is_prime=True
        for j in range(2,i):
            if i%j==0:
                is_prime=False
                break
        if is_prime:
            print(i)
except Exception as e:
    print(e)


# 3.print first 10 prime numbers

# x=2
# count=0
# n=10
# while count<n:
#     for i in range(2,x):
#         if x%i==0:
#             break
#     else:
#         print(x)
#         count+=1
#     x+=1

# method2:          
# def is_prime(n):
#     x=2
#     count=0
#     while count<n:
#         for i in range(2,int(x**0.5)+1):
#             if x%i==0:
#                 break
#         else:
#             print(x)
#             count+=1
#         x+=1
# n=10
# is_prime(n)


# using lamda function
# sq=lambda x:x**2
# print(sq(2))

# using def
# def sq(x):
#     return x**2
# print(sq(4))

# 4.fibonacci series upto 10

# def fibonacci(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return fibonacci(n-1)+fibonacci(n-2)
# print(fibonacci(2))


# 5.factorial

def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(4))

# method2 (shortcut)
import math
print(math.factorial((4)))

# Higher order function examples
# example1:
def sub(a,b):
    return a-b
def fun(sub,x,y):
    return sub(x,y)
print(fun(sub,12,8))

# example2:
# def msg(name):
#     return f"Hello {name}!"
# def fun1(fun2,name):
#     return fun2(name)
# print(fun1(msg,"roshinidevanandi"))


# li=[lambda arg=i:arg*20 for i in range(1,5)]
# for i in li:
#     print(i())

# num=lambda n:"even" if n%2==0 else "odd"
# print(num(96))
# print(num(3))


# Filter ->It is used to filter the given sequence with the help of the function that tests the elments of a sequence to be True or Not

# l=[1,2,3,4,5,6]
# even=filter(lambda x:x%2==0,l)
# print(list(even))


# map
# The map() function is a built-in Python function that takes a function and an iterable (like a list, tuple, etc.) and returns 
# a map object (which is an iterator) that applies the given function to each item in the iterable.
# l=[1,2,3,4,5,6]
# mul=map(lambda x:x*3,l)
# print(list(mul))


# l=[1,2,3,4,5,6]
# a=filter(lambda x:x%2==0,l)
# b=map(lambda p:p*20,a)
# print(list(b))

# Without using lambda function, FILTER,MAP method

# l=[1,2,3,4,5,6]
# def fun1(a):
#     b=[]
#     c=[]
#     for r in a:
#         if r%2==0:
#             b.append(r)
#     for i in b:
#             d=i*20
#             c.append(d)
#     print(c)
# fun1(l)


# s1 = "Hello"
# s2 = "World"
# s3 = s1 + " " + s2
# print(s3)
