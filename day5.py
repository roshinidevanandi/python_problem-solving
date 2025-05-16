import math

# print length of the number

num=123456789
len=0
while num>0:
    num=math.floor(num/10)
    len+=1
print(len)


# print reverse of the number

num=123456789
reverse=0
while num>0:
    digit=num%10
    reverse=reverse*10+digit
    num=math.floor(num/10)
print(reverse)


# print even and odd count of the number

num=123456789
even=0
odd=0
while num>0:
    if (num%10)%2==0:
        even+=1
    else:
        odd+=1
    num=math.floor(num/10)
print(f"even count is {even}")
print(f"odd count is {odd}")