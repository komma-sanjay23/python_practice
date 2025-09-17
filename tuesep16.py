

# unpacking

# lst = ['san',32,'data engineer','austin']
# name,age,role,city = lst
# print(name)
# print(role)



# lst = ['san',32,'data engineer','austin']
# name,*details,city = lst
# print(name)
# print(details)
# print(city)


# lst = ['san',32,'data engineer','austin']
# name,_,_,city = lst
# print(name)
# # print(age)
# print(_)
# print(city)


# lst = ['san',32,'data engineer','austin']
# name,*_,city = lst
# print(name)
# # print(age)
# print(_)
# print(city)

# nums = [10, 20, 30, 40, 50]
# f,*m,l = nums
# print(f)
# print(m)
# print(l)

# a,b = 5,10
# a,b = b,a
# print(a,b)

# nums = [100, 200, 300, 400]
# f,_,lb,_ = nums
# print(f)
# print(_)
# print(lb)


# data = ("Alice", (25, "Engineer"))
# name,(age,role) = data
# print(name)
# # print(age)
# print(role)


# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# com = *list1,*list2
# comb = [*list1,*list2]
# print(com)
# print(comb)


# pairs = [(1, 'a'), (2, 'b'), (3, 'c')]
# nums,chars = zip(*pairs)
# print(nums)
# print(chars)



# def merge_lists(*lists):
#     return [*lists[0], *lists[1], *lists[2]]


# # def merge_lists(*lists):
# #     return [lists[0], lists[1], lists[2]]

# print(merge_lists([1, 2], [3, 4], [5, 6]))  


# default = {"color": "blue", "size": "M"}
# custom = {"size": "L"}
# sol = {**default,**custom}
# print(sol)


# def greet(name,age,city):
#     return (f'Hello {name}, {age} yrs old from {city}')

# # s = {'name' : 'san','city': 'austin','age': 32}
# s = {'name' : 'san','age': 32,'city': 'austin'}
# print(greet(**s))
# # print(greet('san',32,'austin'))



# nested = [[1, 2], [3, 4], [5, 6]]
# lst1 = *nested[0],*nested[1],*nested[2]
# print(lst1)
# lst1 = [*nested[0],*nested[1],*nested[2]]
# print(lst1)


# records = [(1, "Alice", 25), (2, "Bob", 30), (3, "Charlie", 22)]

# for id,name,age in records:
#     print(f'{id} -> {name},{age}')
#     # print(f'my name and id is {name},{id}, and age {age}')


# data = ("User1", (25, ["Python", "SQL", "AWS"]))
# name, (age, [skill1, skill2, skill3]) = data
# print(name, age, skill1, skill2, skill3)


# a, *b, c, *d = [1, 2, 3, 4, 5, 6, 7]
# print(a, b, c, d)  
# ----------------------ERROR FOR MULTIPLE STARS-----------


# a, *b, c = [1, 2, 3, 4, 5, 6, 7]
# print(a, b, c)  


# nums = [1, 2, 3, 4, 5]
# rot = [*nums[2:],*nums[:2]]
# rote = [*nums[3:],*nums[:3]]
# rota = [*nums[1:],nums[0]]
# print(rota) 
# print(rot)
# print(rote)


# a = {"x": 1, "y": 2}
# b = {"y": 100, "z": 200}
# print({**a,**b})


# def profile(name, *skills, **details):
#     print(name, skills, details)

# profile("Alice", "Python", "SQL", age=25, city="NYC")


# s = "HELLO"
# a,b,*c = s
# print(a,b,c)


# records = [(101, "Alice"), (102, "Bob"), (103, "Charlie")]
# for index, (id,name) in enumerate(records,start = 1):
#     print(f'{index} -> {id},{name}')


# nums = (7, 3, 9, 2, 10)
# f,*m,l = set(sorted(nums))
# # f,*m,l = sorted(nums)
# print(f,m)
# print(l)




# s = 'hello'
# rev = ''
# for i in s:
#     rev = i + rev
# print(rev)    

# print(s[::-1])


# s = 'swiss'
# for i in s:
#     if s.count(i) == 1:
#         print(i)
#         break

# print([i for i in s if s.count(i) == 1])






# How importing in python works
# Importing in Python is the process of loading code from a 
# Python module into the current script. This allows you to 
# use the functions and variables defined in the module in 
# your current script, as well as any additional modules that 
# the imported module may depend on.

# To import a module in Python, you use the import statement 
# followed by the name of the module. For example, to import 
# the math module, which contains a variety of mathematical 
# functions, you would use the following statement:

# import math

# Once a module is imported, you can use any of the functions 
# and variables defined in the module by using the dot notation. 
# For example, to use the sqrt function from the math module, 
# you would write:

# import math
# result = math.sqrt(9)
# print(result)  


# # from keyword
# # You can also import specific functions or variables 
# # from a module using the from keyword. For example, 
# # to import only the sqrt function from the math module, 
# # you would write:

# from math import sqrt
# result = sqrt(9)
# print(result)


# # You can also import multiple functions or variables 
# # at once by separating them with a comma:

# from math import sqrt, pi
# result = sqrt(9)
# print(result)  
# print(pi)


# # importing everything
# # It's also possible to import all functions and variables 
# # from a module using the * wildcard. However, this is 
# # generally not recommended as it can lead to confusion 
# # and make it harder to understand where specific functions 
# # and variables are coming from.

# from math import *
# result = sqrt(9)
# print(result) 
# print(pi)  


# # Python also allows you to rename imported modules using 
# # the as keyword. This can be useful if you want to use a 
# # shorter or more descriptive name for a module, or if you 
# # want to avoid naming conflicts with other modules or 
# # variables in your code.


# # The "as" keyword

# import math as m
# result = m.sqrt(9)
# print(result)  
# print(m.pi) 



# # The dir function
# # Finally, Python has a built-in function called dir 
# # that you can use to view the names of all the functions 
# # and variables defined in a module. This can be helpful 
# # for exploring and understanding the contents of a new module.


# import math
# print(dir(math))


# This will output a list of all the names defined in the 
# math module, including functions like sqrt and pi, as well 
# as other variables and constants.

# In summary, the import statement in Python allows you to 
# access the functions and variables defined in a module 
# from within your current script. You can import the entire 
# module, specific functions or variables, or use the * wildcard
# to import everything. You can also use the as keyword to 
# rename a module, and the dir function to view the contents 
# of a module.



# import math

# # print(dir(math))
  

# print(math.gcd(23,46))
# print(math.lcm(45,32))

# import random

# print(dir(random))


# import tensorflow

# print(dir(tensorflow))


# import pandas
# print(dir(pandas))


# import math as m
# from math import sqrt
# print(m.sqrt(144))
# print(sqrt(144))

# from math import pi
# def area(r):
#     return pi*r*r

# print(area(5))

# import math as m
# print(m.factorial(5))


# from math import *
# print(pi)
# print(sqrt(169))
# print(factorial(10))
# print(tan(90))
# print(cos(0))

# import mymath as mm
# from mymath import *
# print(add(7,9))
# print(minus(7,1))

# print(mm.add(7,19))
# print(mm.minus(7,9))


# import mymath as mm
# print(mm.count_vowels('hello world'))

# from datetime import date
# import datetime as dt
# # print(dt.date.today())
# print(dt.datetime(2025,1,9).strftime("%a %m %y"))

# print(date.today().strftime("%Y-%m-%d"))
# print(dt.timezone())
# print(dir(dt))

# from datetime import date 
# import datetime as dt
# print(dt.date.today().strftime("%a-%m-%y"))

# import random
# a = random.sample(range(1,15),5)
# print(a)

# module = 'math'
# math = __import__(module)
# print(math.sqrt(169))


# from mymath import cube
# from mymath import upper

# print(cube(6))
# print(upper('hello world'))


# import math
# # print(dir(math))
# print([i for i in dir(math) if not i.startswith('_')])


# import os
# print(os.getcwd())

# import sys
# print(sys.path)

# def fact(x):
#     import math
#     return math.factorial(x)

# print(fact(7))
# print(fact(5))
# print(fact(8))


import pkgutil
modules = [m.name for m in pkgutil.iter_modules()]
print(modules[:13])  



































































