


# local and global variables
# Before we dive into the differences between local 
# and global variables, let's first recall what a 
# variable is in Python.

# A variable is a named location in memory that stores 
# a value. In Python, we can assign values to variables 
# using the assignment operator =. 
# For example:

# x = 5
# y = "Hello, World!"


# Now, let's talk about local and global variables.

# A local variable is a variable that is defined within 
# a function and is only accessible within that function. 
# It is created when the function is called and is destroyed 
# when the function returns.

# On the other hand, a global variable is a variable that 
# is defined outside of a function and is accessible from 
# within any function in your code.



# # Here's an example to help clarify the difference:

# x = 10 # global variable
# def my_function():
#   y = 5 # local variable
#   print(y)
# my_function()
# print(x)
# # print(y) # this will cause an error because y is a local variable and is not accessible outside of the function



# In this example, we have a global variable x and a 
# local variable y. We can access the value of the global 
# variable x from within the function, but we cannot access 
# the value of the local variable y outside of the function.

# The global keyword
# Now, what if we want to modify a global variable from 
# within a function? This is where the global keyword
# comes in.

# The global keyword is used to declare that a variable 
# is a global variable and should be accessed from the 
# global scope. 



# # Here's an example:

# x = 10 # global variable
# def my_function():
#   global x
#   x = 5 # this will change the value of the global variable x
#   y = 5 # local variable
# my_function()
# print(x) # prints 5
# # print(y) # this will cause an error because y is a local variable and is not accessible outside of the function




# In this example, we used the global keyword to declare 
# that we want to modify the global variable x from within 
# the function. As a result, the value of x is changed to 5.

# It's important to note that it's generally considered good 
# practice to avoid modifying global variables from within 
# functions, as it can lead to unexpected behavior and make 
# your code harder to debug.

# I hope this tutorial has helped clarify the differences 
# between local and global variables and how to use the 
# global keyword in Python. Thank you for watching!



# Local variable → defined inside a function, accessible 
# only within that function.

# Global variable → defined outside all functions, 
# accessible everywhere.

# global keyword → allows modifying a global variable 
# inside a function.

# nonlocal keyword → allows modifying variables in an 
# enclosing (non-global) scope.



# x = 10  

# def show():
#     x = 5  
#     print("Inside:", x)

# show()
# print("Outside:", x)



# x = 20
# def display():
#     print("Inside function:", x)  

# display()
# print("Outside function:", x)



# count = 0

# def increment():
#     global count
#     count += 1

# increment()
# increment()
# print("Final count:", count)  



# name = "GlobalName"

# def func():
#     name = "LocalName"
#     print("Inside:", name)

# func()
# print("Outside:", name)



# def outer():
#     x = "outer var"
#     def inner():
#         nonlocal x
#         x = "modified by inner"
#     inner()
#     print("After inner:", x)

# outer()


# def out():
#     x = "outer var"
#     def inner():
#         nonlocal x
#         # global x
#         x = "modified by inner"
#     inner()
#     print("After inner:", x)

# out()


# def test():
#     x = 50
#     print("Inside:", x)

# test()
# # print(x)  



# x = 100
# def scope_demo():
#     y = 200
#     print("Locals:", locals())  
#     print("Globals keys:", list(globals().keys())[:10])  

# scope_demo()



# # print(locals())
# # print(locals().keys())
# # print(locals().values())

# # print(globals().keys())
# # print(list(globals().keys()))
# # print(globals().values())



# PI = 3.14159

# def area_circle(r):
#     PI = 3.14  
#     return {PI,PI * r * r}

# print(area_circle(5)) 
# print(PI)             



# x = [1, 2, 3]

# def modify():
#     x.append(4)  
#     print("Inside:", x)

# modify()
# print("Outside:", x)



# num = 10

# def change():
#     # num += 5  
#     global num
#     num += 5

# change()
# print(num)  



# score = 0

# def add_points(n):
#     global score
#     score += n

# def reset_score():
#     global score
#     score = 0

# add_points(10)
# add_points(5)
# print("Score:", score)  
# reset_score()
# print("Score:", score)  


# config = {"theme": "dark", "language": "en"}

# def update_config(key, value):
#     global config
#     config[key] = value

# update_config("theme", "light")
# print(config) 



# counter = 0

# def track_calls():
#     global counter
#     counter += 1
#     print(f"Function called {counter} times")

# track_calls()
# track_calls()

# track_calls()


# def compute(a, b):
#     result = a*b + a/b
#     print("Locals:", locals())
#     return result

# print(compute(10, 2))



# status = "active"

# def change_status():
#     status = "inactive"  
#     print("Inside:", status)

# change_status()
# print("Outside:", status)




# status = "active"

# def change_status():
#     global status
#     status = "inactive"
#     print("Inside:", status)

# change_status()
# print("Outside:", status)



# version = 1

# def upgrade():
#     global version
#     version += 2

# upgrade()
# print("Version:", version)



# x = 5
# nums = [x for x in range(3)]
# print(nums)  
# print(x)    



# def outer():
#     a = 10
#     def middle():
#         b = 20
#         def inner():
#             nonlocal a, b
#             a += 1
#             b += 1
#             return a, b
#         return inner()
#     return middle()

# print(outer())  



# def factorial(n):
#     cache = {}
#     def inner(m):
#         if m in cache:
#             return cache[m]
#         if m == 0 or m == 1:
#             cache[m] = 1
#         else:
#             cache[m] = m * inner(m-1)
#         return cache[m]
#     return inner(n)

# print(factorial(5))  # 120
# # --------------------------------------------



# Opening a File

# Before we can perform any operations on a file, we must 
# first open it. Python provides the open() function to open 
# a file. It takes two arguments: the name of the file and 
# the mode in which the file should be opened. The mode 
# can be 'r' for reading, 'w' for writing, or 'a' 
# for appending.


# Here's an example of how to open a file for reading:

# with open('myfile.txt', 'w') as f:
#     f.write('hi')


# f = open('myfile.txt', 'w')
# # f.read()
# print(f.write('hello'))


# f = open('myfile.txt', 'w')
# print(f.write('ji'))



# f = open('myfile.txt', 'a')
# f.write('Hello, world!')


# f = open('myfile.txt', 'r')
# # ... do something with the file
# f.close()


# with open("sample.txt", "w") as f:
#     f.write("Hello, Python!\nWelcome to file handling.")


# with open('sample.txt','r') as f:
#     print(f.read())


# with open("sample.txt", "r") as f:
#     for line in f:
#         print(line)
#         # print(line.strip())


# with open("sample.txt", "r") as f:
#     # f.write('\nsanjay')
#     print(f.readlines())


# with open("sample.txt", "r") as f:
#     print(len(f.read().split()))
































