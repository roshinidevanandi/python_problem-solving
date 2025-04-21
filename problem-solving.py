# "Write a Python function that takes a string and an integer k, and returns the string after rotating it to the right
#  by k positions."
def round_string(s,k):
    rotated=s[-k:]+s[:-k]
    print(rotated)


str=input("Enter the string: ")
number=int(input("Enter the num: "))
round_string(str,number)