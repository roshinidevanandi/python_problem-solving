# ____________File Handling__________

# File handling refers to the process of performing operations on a file such as creating, opening, reading, writing and 
# closing it, through a programming interface.


# 1.read file 
# file=open("./sample.txt","r")
# print(file.read())

# If you want to read line of the file we have to use "readline()"
# file=open("./sample.txt","r")
# print(file.readline())

# If you want to read all lines of the file we have to use "readlines()" and output is like list type
# file=open("./sample.txt","r")
# print(file.readlines())



# 2.write file
# It writes the content on the mentioned file but with the help of this we can replace the new content with previous content
# paragraph="hello i am from the actual sample"
# f=open("./sample.txt","w")
# f.write(paragraph)
# f.close()

# If you want to add the content with previous one have to use the append
# f=open("./sample.txt","a")
# f.write("hello i am from the actual sample3\n")
# f.close()

# If you want to add more than one strings we have to use "writelines()"

# data_list=["hello file1\n","hello file2\n","hello file3\n"]
# file=open("./sample.txt","a")
# file.writelines(data_list)
# file.close() 

# when you open the file to access the another file if your work is done you have to terminate the file first
# file.close()


# 3.create file
# If you want to create new file we have to use write file only but you have to take the new file name what you want to create a new file
# file=open("./new_file.txt","w")
# file.write("hello i am roshini")
# file.close()


# 4. delete file
# If you want to delete the content of the file use 
# file=open("./new_file.txt","w")
# file.write("")
# file.close()


# 5.seek
# change the file pointer position which is used only for read
# file=open("./new_file.txt","r")
# file.seek(10)
# print(file.read())


# 6. tell
# Returns the current position of the file pointer
# file=open("./new_file.txt","r")
# file.seek(10)
# print(file.tell())
# print(file.read())




# If you want to delete the entire file you have to import os module and than remove file
# import os
# os.remove("new_file.txt")

# If you want to create directory/folder
# os.mkdir("new_one")