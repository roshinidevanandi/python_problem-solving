def str_fun(str,k):
    for i in range(len(str)-1,-1,-1):
        print(str[i],k)
        print(k)
str=input("enter the string here: ")
num=int(input("enter the number here: "))
str_fun(str,num)