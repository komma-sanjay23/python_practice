


# print('hello')


# __init__ Method
# __init__ method is the constructor in Python, automatically 
# called when a new object is created. It initializes the 
# attributes of the class.

# Example: In this example, we create a Dog class and use 
# __init__ method to set the name and age of each dog when 
# creating an object.


# class Dog:
#     def __init__(self, name, age):
#         print(f'I am cool person')
#         self.name = name
#         self.age = age
#     def info(self):
#         print(f'My name is {self.name} and my age {self.age} ')    

# dog1 = Dog("Buddy", 67)
# dog2 = Dog('sam',7)
# dog1.info()
# # dog2.info()
# # print(dog1.name)



# class Dog:
#     def __init__(self):
#         print(f'I am cool person')
#         # self.name = name
#         # self.age = age
#     def info(self):
#         name = 'san'
#         age = 5
#         print(f'My name is {name} and my age {age} ')    

# # dog1 = Dog("Buddy", 67)
# # dog2 = Dog('sam',7)
# dog1 = Dog()
# dog2 = Dog()
# dog3 = Dog()
# dog1.info()
# # dog2.info()
# # print(dog1.name)



# class Person:

#   def __init__(self, name, occ):
#     print("Hey I am a person")
#     self.name = name
#     self.occ = occ

#   def info(self):
#     print(f"{self.name} is a {self.occ}")


# a = Person("Harry", "Developer")
# b = Person("Divya", "HR") 
# c = Person(' ',' ')
# a.info()
# b.info()



# From Harry
# Constructors
# A constructor is a special method in a class used to create 
# and initialize an object of a class. There are different 
# types of constructors. Constructor is invoked automatically 
# when an object of a class is created.

# A constructor is a unique function that gets called automatically 
# when an object is created of a class. The main purpose of a 
# constructor is to initialize or assign values to the data 
# members of that class. It cannot return any value other than None.


# Syntax of Python Constructor


# def __init__(self):
# 	# initializations


# init is one of the reserved functions in Python. 
# In Object Oriented Programming, it is known as a constructor.


# Types of Constructors in Python

# Parameterized Constructor
# Default Constructor

# Parameterized Constructor in Python
# When the constructor accepts arguments along with self, it 
# is known as parameterized constructor.

# These arguments can be used inside the class to assign the 
# values to the data members.

# Example:


# class Details:
#     def __init__(self, animal, group):
#         self.animal = animal
#         self.group = group

# obj1 = Details("Crab", "Crustaceans")
# print(obj1.animal, "belongs to the", obj1.group, "group.")




# class Details:
#     def __init__(self, animal, group):
#         self.animal = animal
#         self.group = group
#     def auto(self):
#         print(f'{self.animal} belongs to the {self.group} group.')    

# obj1 = Details("Crab", "Crustaceans")
# # print(f'{self.animal}, belongs to the, {self.group}, group.')
# obj1.auto()



# Default Constructor in Python
# When the constructor doesn't accept any arguments from the 
# object and has only one argument, self, in the constructor, 
# it is known as a Default constructor.

# Example:

# class Details:
#   def __init__(self):
#     print("animal Crab belongs to Crustaceans group")

# obj1 = Details()
# obj2 = Details()




# Create a class Person with attributes name and age. 
# Initialize using constructor and print them.



# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#         print(f'{self.name} and age {self.age}')

# a = Person('san',8)
# # print(a.name,a.age)


# Create two objects of class Car with attributes brand and year.


# class car:
#     def __init__(self,br,yr):
#         self.brand = br 
#         self.year = yr

# a = car('BMW',2019)
# b = car('benz',2028)
# print(a.brand,a.year,b.brand,b.year)



# Default values in constructor

# class default:
#     def __init__(self,br = 'toyota',yr = 2017):
#         self.brand = br
#         self.year = yr
#         print(f'Its the default value')

# a = default('hundai',2019)
# b = default('honda',2018) 
# c = default()       
# print(a.brand,a.year,b.brand,b.year,c.brand,c.year)



# Create class Circle with attribute radius. Add constructor 
# that also calculates area.


# class Circle:
#     def __init__(self,r):
#         self.r = r
#         print(f'Area od circle: {3.14*r*r}')

# a = Circle(7)


# Constructor with string input processing


# class string:
#     def __init__(self,name):
#         self.name1,self.name2 = name.split()

# a = string('san kom')
# print(a.name2)        



# Constructor that initializes a list


# class list:
#     def __init__(self,nums,lst):
#         self.nums = nums
#         self.lst = lst

# a = list(4,[1,2,3,4])        
# print(a.nums,a.lst)



# Constructor chaining simulation (via default parameter)


# class emp:
#     def __init__(self,name,sal = 2000):
#         self.sal = sal
#         self.name = name

# a = emp('san',5000)
# b = emp('kom')
# print(a.name,a.sal,b.name,b.sal)


# Constructor with type conversion

# class type():
#     def __init__(self,num1,num2):
#         self.num1 = int(num1)
#         self.num2 = round(float(num2),2)

# a = type(3.4,67.987457)
# print(a.num1,a.num2)        


# Constructor with boolean attribute


# class Bool:
#     def __init__(self,val):
#         self.val = bool(val)

# a = Bool(0)
# print(a.val)


# class Light:
#     def __init__(self, status):
#         self.is_on = True if status.lower() == "on" else False

# a = Light("ON")
# print(a.is_on)  



# Constructor that validates input


# class person:
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks if marks <= 100 else 0

# a = person('san',819)
# print(a.name,a.marks)


# Constructor with multiple data types

# class Item:
#     def __init__(self, name, quantity, price):
#         self.name = name
#         self.quantity = int(quantity)
#         self.price = float(price)

# item = Item("Pen", "10", "1.5")
# print(item.name, item.quantity, item.price)  


# Constructor that creates derived attribute

# class Area:
#     def __init__(self,l,b):
#         self.l = l
#         self.b = b 
#         self.area = 2*l*b

# a = Area(4,5)        
# print(a.l,a.b,a.area)


# Constructor with list of objects

# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# a = [Student('sa',54),Student('ko',67)]
# for i in a:
#     print(i.name) 


# Constructor that accepts variable number of arguments


# class mark:
#     def __init__(self,name,*marks):
#         self.name = name
#         # self.marks = marks
#         self.marks = list(marks)
#         self.sum = sum(marks)

# a = mark('san',45,6,7,97,54)
# print(a.name,a.sum,a.marks)


# Constructor that stores a dictionary

# class dict:
#     def __init__(self,**kwags):
#         self.ags = kwags

# a = dict(aa = 'san',bb = 'dev')
# print(a.ags)


# Bank Account with auto-balance setup

# class bank:
#     def __init__(self,name,balance = 0):
#         self.name = name
#         self.balance = balance

# a = bank('san','500')
# b = bank('kom')
# print(a.name,a.balance)
# print(b.name,b.balance)


# Student with GPA calculation

# class mark:
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = list(marks)
#         self.gpa = sum(marks)/len(marks)

# a = mark('san',[1,2,4,7,8])
# print(a.gpa)


# Product with discount

# class product:
#     def __init__(self,name,amount,discount=0):
#         self.name = name
#         self.amount = amount
#         self.total = amount - ((amount*discount)/100)
#         print(f'The total amount is {self.total}')

# a = product('san',50,8)


# Employee with yearly salary


# class emp:
#     def __init__(self,sal):
#         self.sal = sal
#         self.yrsal = sal*12
#         print(f'The year sal is {self.yrsal}')

# a = emp(500)


# Circle with diameter

# class circle:
#     def __init__(self,r):
#         self.raduis = r
#         print(f'The circle with daiameteris {2*r}')

# a = circle(6)


# User with email validation


# class email:
#     def __init__(self,name,email):
#         self.name = name
#         self.email = 'valid' if '@gmail.com' in email else 'invalid'
#         print(f'The {email} is {self.email}')

# a = email('san','abc@gmail.com')
# b = email('kom','ssgmail.com')


# Movie rating system


# class movie:
#     def __init__(self, title, ratings):
#         self.title = title
#         self.ratings = ratings
#         self.avg_rating = sum(ratings)/len(ratings) if ratings else 0

# m = movie("Inception", [9, 8, 10, 9])
# print(m.title, m.avg_rating)


# Laptop with multiple attributes
    

# class Laptop:
#     def __init__(self, brand, ram, storage):
#         self.brand = brand
#         self.ram = ram
#         self.storage = storage

# l = Laptop("Dell", "16GB", "512GB SSD")
# print(l.brand, l.ram, l.storage)


# Order with item list and total price


# class order:
#     def __init__(self,items):
#         self.items = list(items)
#         self.total = sum(price for item,price in items)
#         print(f'The no. of items is {len(items)} and total price is {self.total}')

# a = order([("Book", 200), ("Pen", 20), ("Bag", 500)])


# Course with students


# class course:
#     def __init__(self,course,students):
#         self.course = course
#         self.students = list(students)
#         print(f'The course is {self.course} and the students are {self.students}')

# a = course("Python", ["San", "Bha", "Komm"])


# Temperature converter in constructor

# class temp:
#     def __init__(self,c):
#         self.c = c
#         self.f = (c * (9/5)) + 32
#         print(f'The temperature in fahrenheit is {self.f}')

# a = temp(56)


# Flight ticket cost calculator

# class ticket:
#     def __init__(self,name,price,quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity 
#         self.total = price * quantity
#         print(f'The total cost is {self.total}')

# a = ticket('sam',35,8)


# Bank loan EMI calculator

# class Loan:
#     def __init__(self,p,r,y):
#         self.principle = p
#         self.rate = r / 100 / 12
#         self.month = y * 12
#         self.emi = (p * self.rate * (1 + self.rate) ** self.month) / ((1 + self.rate) ** self.month - 1)
#         print(f'The emi is {round(self.emi,2)}')

# a = Loan(100000, 10, 2)


# Shopping cart

# class Items:
#     def __init__(self,items):
#         self.items = list(items)
#         self.count = len(items)
#         print(f'The no. of items is {self.count} and the items are {self.items}')

# a = Items(['soap','brush','towel'])


# class Items:
#     def __init__(self,*items):
#         self.items = list(items)
#         self.count = len(items)
#         print(f'The no. of items is {self.count} and the items are {self.items}')

# a = Items('soap','brush','towel')



# Rectangle with area and perimeter

# class Rect:
#     def __init__(self,l,b):
#         self.l = l
#         self.b = b
#         self.area = l*b
#         self.perimeter = 2 * (l+b)
#         print(f'The area and perimeter of rectangle is {self.area} and {self.perimeter}')

# a = Rect(4,6)



# Class and Instance Variables

# In Python, variables defined in a class can be either class 
# variables or instance variables, and understanding the 
# distinction between them is crucial for object-oriented 
# programming.

# Class Variables

# These are the variables that are shared across all instances 
# of a class. It is defined at the class level, outside any methods.
# All objects of the class share the same value for a class 
# variable unless explicitly overridden in an object.

# Instance Variables

# Variables that are unique to each instance (object) of a class. 
# These are defined within the __init__ method or other instance 
# methods. Each object maintains its own copy of instance variables, 
# independent of other objects.

# Example: In this example, we create a Dog class to show 
# difference between class variables and instance variables. We 
# also demonstrate how modifying them affects objects differently.




# class Dog:
#     # Class variable
#     species = "Canine"

#     def __init__(self, name, age):
#         # Instance variables
#         self.name = name
#         self.age = age

# # Create objects
# dog1 = Dog("Buddy", 3)
# dog2 = Dog("Charlie", 5)

# # Access class and instance variables
# print(dog1.species)  # (Class variable)
# print(dog1.name)     # (Instance variable)
# print(dog2.name)     # (Instance variable)

# # Modify instance variables
# dog1.name = "Max"
# print(dog1.name)     # (Updated instance variable)

# # Modify class variable
# Dog.species = "Feline"
# print(dog1.species)  # (Updated class variable)
# print(dog2.species)



# Explanation:

# Class Variable (species): Shared by all instances of the class. 
# Changing Dog.species affects all objects, as it's a property of 
# the class itself.
    
# Instance Variables (name, age): Defined in the __init__ method. 
# Unique to each instance (e.g., dog1.name and dog2.name are 
# different).

# Accessing Variables: Class variables can be accessed via the 
# class name (Dog.species) or an object (dog1.species). Instance 
# variables are accessed via the object (dog1.name).

# Updating Variables: Changing Dog.species affects all instances. 
# Changing dog1.name only affects dog1 and does not impact dog2.




# 3. Inheritance



















































