

# oops

# Introduction to Object-oriented programming
# Introduction to Object-Oriented Programming in Python: 
# In programming languages, mainly there are two approaches 
# that are used to write program or code.



# 1). Procedural Programming
# 2). Object-Oriented Programming
# The procedure we are following till now is the 
# “Procedural Programming” approach. So, in this session, 
# we will learn about Object Oriented Programming (OOP). 
# The basic idea of object-oriented programming (OOP) in 
# Python is to use classes and objects to represent real-world 
# concepts and entities.



# A class is a blueprint or template for creating objects. 
# It defines the properties and methods that an object of that 
# class will have. Properties are the data or state of an object, 
# and methods are the actions or behaviors that an object can 
# perform.


# An object is an instance of a class, and it contains its 
# own data and methods. For example, you could create a class
# called "Person" that has properties such as name and age, 
# and methods such as speak() and walk(). Each instance of the 
# Person class would be a unique object with its own name and 
# age, but they would all have the same methods to speak and walk.


# One of the key features of OOP in Python is encapsulation, 
# which means that the internal state of an object is hidden 
# and can only be accessed or modified through the object's '
# 'methods. This helps to protect the object's data and prevent 
# it from being modified in unexpected ways.


# Another key feature of OOP in Python is inheritance, which 
# allows new classes to be created that inherit the properties 
# and methods of an existing class. This allows for code reuse 
# and makes it easy to create new classes that have similar 
# functionality to existing classes.


# Polymorphism is also supported in Python, which means that 
# objects of different classes can be treated as if they were 
# objects of a common class. This allows for greater flexibility 
# in code and makes it easier to write code that can work with 
# multiple types of objects.


# In summary, OOP in Python allows developers to model real-world 
# concepts and entities using classes and objects, encapsulate 
# data, reuse code through inheritance, and write more flexible 
# code through polymorphism.



# class
# object
# inheritance
# polymorphism
# encapsulation
# abstraction



# Python OOP Concepts
# Object Oriented Programming is a fundamental concept in 
# Python, empowering developers to build modular, maintainable 
# and scalable applications.

# OOP is a way of organizing code that uses objects and 
# classes to represent real-world entities and their behavior. 
# In OOP, object has attributes thing that has specific data 
# and can perform certain actions using methods.

# Key Features of OOP in Python:
# Organizes code into classes and objects
# Supports encapsulation to group data and methods together
# Enables inheritance for reusability and hierarchy
# Allows polymorphism for flexible method implementation
# Improves modularity, scalability, and maintainability



# Characteristics of OOP (Object Oriented Programming)
# Python supports the core principles of object-oriented 
# programming, which are the building blocks for designing 
# robust and reusable software. The diagram below demonstrates 
# these core principles:


# 1. Class

# A class is a collection of objects. Classes are blueprints 
# for creating objects. A class defines a set of attributes 
# and methods that the created objects (instances) can have.

# Some points on Python class:  

# Classes are created by keyword class.
# Attributes are the variables that belong to a class.
# Attributes are always public and can be accessed using 
# the dot (.) operator. 
# Example: Myclass.Myattribute

# Creating a Class
# Here, class keyword indicates that we are creating a 
# class followed by name of the class (Dog in this case).


# class Dog:
#     species = "Canine"  # Class attribute

#     def __init__(self, name, age):
#         self.name = name  # Instance attribute
#         self.age = age  # Instance attribute


# Explanation:

# class Dog: Defines a class named Dog.
# species: A class attribute shared by all instances of the class.
# __init__ method: Initializes the name and age attributes 
# when a new object is created.

# ------------------------------------------------------------


# From Harry
# A class is a blueprint or a template for creating objects, 
# providing initial values for state (member variables or 
# attributes), and implementations of behavior 
# (member functions or methods). The user-defined objects 
# are created using the class keyword.

# Creating a Class:
# Let us now create a class using the class keyword.

# class Details:
#     name = "Rohan"
#     age = 20

# # a = Details()
# # print(a.name)



# 2. Objects
# An Object is an instance of a Class. It represents a specific 
# implementation of the class and holds its own data.

# An object consists of:

# State: It is represented by the attributes and reflects the 
# properties of an object.
# Behavior: It is represented by the methods of an object and 
# reflects the response of an object to other objects.
# Identity: It gives a unique name to an object and enables one 
# object to interact with other objects.

# Creating Object
# Creating an object in Python involves instantiating a class 
# to create a new instance of that class. This process is 
# also referred to as object instantiation.


# class Dog:
#     species = "Canine"  # Class attribute

#     def __init__(self, name, age):
#         self.name = name  # Instance attribute
#         self.age = age  # Instance attribute

# # Creating an object of the Dog class
# dog1 = Dog("Buddy", 3)

# print(dog1.name,dog1.age) 
# print(dog1.species)



# From Harry
# Creating an Object:

# Object is the instance of the class used to access the 
# properties of the class Now lets create an object of the class.

# Example:

# obj1 = Details()      # Now we can print values:

# Example:

# class Details:
#     name = "Rohan"
#     age = 20
# obj1 = Details()
# print(obj1.name)
# print(obj1.age)


# Self Parameter

# Self parameter is a reference to the current instance of 
# the class. It allows us to access the attributes and methods 
# of the object.

# Example: In this example, we create a Dog class with both 
# class and instance attributes, then demonstrate how to access 
# them using the self parameter.



# class Dog:
#     species = "Canine"  # Class attribute

#     def __init__(self, name, age):
#         self.name = name  # Instance attribute
#         self.age = age  # Instance attribute

# dog1 = Dog("Buddy", 3)  # Create an instance of Dog
# dog2 = Dog("Charlie", 5)  # Create another instance of Dog

# print(dog1.name, dog1.age, dog1.species)  # Access instance and class attributes
# print(dog2.name, dog2.age, dog2.species)  # Access instance and class attributes
# print(Dog.species)  # Access class attribute directly



# From Harry
# self parameter
# The self parameter is a reference to the current instance 
# of the class, and is used to access variables that belongs 
# to the class.

# It must be provided as the extra parameter inside the method 
# definition.

# Example:

# class Details:
#     name = "Rohan"
#     age = 20
#     def desc(self):
#         print("My name is", self.name, "and I'm", self.age, "years old.")
# obj1 = Details()
# obj1.desc()



# class Details:
#     name = "Rohan"
#     age = 20
#     def desc(self,n):
#         self.name = n
#         print("My name is", self.name, "and I'm", self.age, "years old.")
# obj1 = Details()
# obj1.desc('sanjay')



# class person:
#     name = 'sanjay'
#     occ = 'data engineer'
#     sal = '5k'
#     def info(self):
#         print(f'{self.name} is an {self.occ}')

# a = person()
# b = person()
# # print(a.name)
# # print(a.occ)
# # print(a.sal)

# a.name = 'komma'
# a.occ = 'developer'

# b.name = 'bhar'
# b.occ = 'engineer'

# # print(a.name)
# # print(b.name)
# c = person()

# a.info()
# b.info()
# c.info()




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






































































