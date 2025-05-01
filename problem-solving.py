# # "Write a Python function that takes a string and an integer k, and returns the string after rotating it to the right
# #  by k positions."
# def round_string(s,k):
#     rotated=s[-k:]+s[:-k]
#     print(rotated)


# str=input("Enter the string: ")
# number=int(input("Enter the num: "))
# round_string(str,number)


# 1.Print a 2D matrix in a clean format
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# for row in matrix:
#     print(' '.join(str(x) for x in row))

# or

# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# for row in matrix:
#     print(*row)


# 2.Transpose a matrix (rows become columns).
# Method_1
# matrix = [[1, 2], [3, 4], [5, 6]]
# transpose=[]
# for i in range(len(matrix[0])): 
#     one=[]   
#     for j in range(len(matrix)):
#         one.append(matrix[j][i])
#     transpose.append(one)
# for row in transpose:
#     print(row)


# Method_2

matrix = [[1, 2], [3, 4], [5, 6]]
transpose = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
for row in transpose:
    print(row)




