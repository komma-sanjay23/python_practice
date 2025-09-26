

# 3. Inheritance


# Inheritance allows a class (child class) to acquire properties 
# and methods of another class (parent class). It supports 
# hierarchical classification and promotes code reuse.


# Types of Inheritance:

# Single Inheritance: A child class inherits from a single parent 
# class.
    
# Multiple Inheritance: A child class inherits from more than 
# one parent class.
    
# Multilevel Inheritance: A child class inherits from a parent 
# class, which in turn inherits from another class.

# Hierarchical Inheritance: Multiple child classes inherit from 
# a single parent class.
    
# Hybrid Inheritance: A combination of two or more types of 
# inheritance.



# In this example, we create a Dog class and demonstrate single, 
# multilevel and multiple inheritance. We show how child classes 
# can use or extend parent class methods.




# # Single Inheritance
# class Dog:
#     def __init__(self, name):
#         self.name = name

#     def display_name(self):
#         print(f"Dog's Name: {self.name}")

# class Labrador(Dog):  # Single Inheritance
#     def sound(self):
#         print("Labrador woofs")

# # Multilevel Inheritance
# class GuideDog(Labrador):  # Multilevel Inheritance
#     def guide(self):
#         print(f"{self.name} Guides the way!")

# # Multiple Inheritance
# class Friendly:
#     def greet(self):
#         print("Friendly!")

# class GoldenRetriever(Dog, Friendly):  # Multiple Inheritance
#     def sound(self):
#         print("Golden Retriever Barks")

# # Example Usage
# lab = Labrador("Buddy")
# lab.display_name()
# lab.sound()

# guide_dog = GuideDog("Max")
# guide_dog.display_name()
# guide_dog.guide()

# retriever = GoldenRetriever("Charlie")
# retriever.display_name()
# retriever.greet()
# retriever.sound()

# Explanation:

# Single Inheritance: Labrador inherits Dog's attributes 
# and methods.

# Multilevel Inheritance: GuideDog extends Labrador, inheriting 
# both Dog and Labrador functionalities.

# Multiple Inheritance: GoldenRetriever inherits from both Dog 
# and Friendly.



# From Harry
# Inheritance in python

# When a class derives from another class. The child class 
# will inherit all the public and protected properties and 
# methods from the parent class. In addition, it can have its 
# own properties and methods,this is called as inheritance.



# Python Inheritance Syntax

# class BaseClass:
#   Body of base class
    
# class DerivedClass(BaseClass):
#   Body of derived class
    
# Derived class inherits features from the base class where 
# new features can be added to it. This results in re-usability 
# of code.


# Types of inheritance:

# Single inheritance
# Multiple inheritance
# Multilevel inheritance
# Hierarchical Inheritance
# Hybrid Inheritance




# class Employee:
#     def __init__(self, name, id):
#         self.name = name
#         self.id = id 

#     def showDetails(self):
#         print(f"The name of Employee: {self.id} is {self.name}")

# class Programmer(Employee):
#     def showLanguage(self):
#         print("The default langauge is Python")


# a = Employee('sanj',76)
# a.showDetails()
# # a.showLanguage()  # Error
# b = Programmer('komm',98)
# b.showDetails()
# b.showLanguage()




# Types of inheritance:

# Single inheritance
# Multiple inheritance
# Multilevel inheritance
# Hierarchical Inheritance
# Hybrid Inheritance

# ==========================================================

# Single inheritance enables a derived class to inherit properties 
# from a single parent class, thus enabling code reusability and 
# the addition of new features to existing code.


# class Parent:
#     def func1(self):
#         print("This function is in parent class.")
 
# class Child(Parent):
#     def func2(self):
#         print("This function is in child class.")
 
# object = Child()
# object.func1()
# object.func2()

# ============================================================

# Single Inheritance in Python

# Single inheritance is a type of inheritance where a class 
# inherits properties and behaviors from a single parent class. 
# This is the simplest and most common form of inheritance.


# Syntax

# The syntax for single inheritance in Python is straightforward 
# and easy to understand. To create a new class that inherits from 
# a parent class, simply specify the parent class in the class 
# definition, inside the parentheses, like this:


# class ChildClass(ParentClass):
#     # class body

# Example

# Let's consider a simple example of single inheritance in Python. 
# Consider a class named "Animal" that contains the attributes and 
# behaviors that are common to all animals.



# class Animal:
#     def __init__(self, name, species):
#         self.name = name
#         self.species = species
        
#     def make_sound(self):
#         print("Sound made by the animal")

# a = Animal('dog','germansheperd')
# a.make_sound()  
      


# # If we want to create a new class for a specific type of animal, 
# # such as a dog, we can create a new class named "Dog" that 
# # inherits from the Animal class.


# class Dog(Animal):
#     def __init__(self, name, breed):
#         Animal.__init__(self, name, species="Dog")
#         self.breed = breed
        
#     def make_sound(self):
#         print("Bark!")

# a = Dog('dog1','german')
# a.make_sound()

# b = Animal('dog','germansheperd')
# b.make_sound()  


# The Dog class inherits all the attributes and behaviors of the 
# Animal class, including the __init__ method and the make_sound 
# method. Additionally, the Dog class has its own __init__ method 
# that adds a new attribute for the breed of the dog, and it also 
# overrides the make_sound method to specify the sound that a dog 
# makes.

# Single inheritance is a powerful tool in Python that allows you 
# to create new classes based on existing classes. It allows you to 
# reuse code, extend it to fit your needs, and make it easier to 
# manage complex systems. Understanding single inheritance is an 
# important step in becoming proficient in object-oriented 
# programming in Python.



# class Animal:
#     def __init__(self, name, species):
#         self.name = name
#         self.species = species
        
#     def make_sound(self):
#         print("Sound made by the animal")


# class Dog(Animal):
#     def __init__(self, name, breed):
#         Animal.__init__(self, name, species="Dog")
#         self.breed = breed
        
#     def make_sound(self):
#         print("Bark!")

# class Cat(Animal):
#     def __init__(self,name):
#         Animal.__init__(self,name,species = 'cat')

#     def sound(self):
#         print(f'{self.name} says Meow')

# a = Cat('Homecat')
# a.sound()            


# Multiple Inheritance

# Multiple inheritance is a powerful feature in object-oriented 
# programming that allows a class to inherit attributes and methods 
# from multiple parent classes. This can be useful in situations 
# where a class needs to inherit functionality from 
# multiple sources.

# Syntax

# In Python, multiple inheritance is implemented by specifying 
# multiple parent classes in the class definition, separated by 
# commas.


# class ChildClass(ParentClass1, ParentClass2, ParentClass3):
#     # class body

# In this example, the ChildClass inherits attributes and methods 
# from all three parent classes: ParentClass1, ParentClass2, and 
# ParentClass3.

# ------MOST-----------------MRO-----------IMP---------------

# It's important to note that, in case of multiple inheritance, 
# Python follows a method resolution order (MRO) to resolve 
# conflicts between methods or attributes from different parent 
# classes. The MRO determines the order in which parent classes 
# are searched for attributes and methods.


# Example


# class Animal:
#     def __init__(self, name, species):
#         self.name = name
#         self.species = species
        
#     def make_sound(self):
#         print("Sound made by the animal")
        

# class Mammal:
#     def __init__(self, name, fur_color):
#         self.name = name
#         self.fur_color = fur_color
        
#     def make_sound(self):
#         print("Sound made by the mammal")


# class Dog(Mammal,Animal):
#     def __init__(self,name,bread,color):
#         Mammal.__init__(self,name,color)
#         Animal.__init__(self,name,species = Dog)
#         self.bread = bread

#     def sound(self):
#         print(f'{self.name} says meow')

# a = Dog('Homecat','normal','white')
# a.sound()
# a.make_sound()


# In this example, the Dog class inherits from both the Animal 
# and Mammal classes, so it can use attributes and methods from 
# both parent classes.


# class ParentA:
#     def common_method(self):
#         print("Method from ParentA")

# class ParentB:
#     def common_method(self):
#         print("Method from ParentB")

# class Child(ParentA,ParentB):
#     pass

# a = Child()
# a.common_method() 

# print(Child.__mro__)




# class Mother:
#     mothername = ""
 
#     def mother(self):
#         print(self.mothername)
 
 
# class Father:
#     fathername = ""
 
#     def father(self):
#         print(self.fathername)
 
 
# class Son(Mother, Father):
#     def parents(self):
#         print(f"Father name is : {self.fathername}")
#         print(f"Mother : {self.mothername}")


# s1 = Son()
# s1.fathername = "Mom"
# s1.mothername = "Dad"
# s1.parents()



# class Employee:

#     def __init__(self, name):
#         self.name = name

#     def show(self):
#         print(f"The name is {self.name}")

# class Dancer:

#     def __init__(self, dance):
#         self.dance = dance

#     def show(self):
#         print(f"The dance is {self.dance}")


# class DancerEmployee(Dancer,Employee):
# # class DancerEmployee(Employee,Dancer):    

#     def __init__(self, dance, name):
#         self.dance = dance
#         self.name = name


# o  = DancerEmployee("kathakali", "san")
# print(o.name,o.dance)
# o.show() 
# # print(DancerEmployee.mro())




# Multilevel Inheritance 


# Multilevel inheritance is a type of inheritance in 
# object-oriented programming where a derived class inherits 
# from another derived class. This type of inheritance allows 
# you to build a hierarchy of classes where one class builds 
# upon another, leading to a more specialized class.


# In multilevel inheritance, features of the base class and the 
# derived class are further inherited into the new derived class. 
# This is similar to a relationship representing a child and a 
# grandfather.


# In Python, multilevel inheritance is achieved by using the 
# class hierarchy. The syntax for multilevel inheritance is quite 
# simple and follows the same syntax as single inheritance.

# Syntax

# class BaseClass:
#     # Base class code
#     pass

# class DerivedClass1(BaseClass):
#     # Derived class 1 code
#     pass
    
# class DerivedClass2(DerivedClass1):
#     # Derived class 2 code



# In the above example, we have three classes: BaseClass, 
# DerivedClass1, and DerivedClass2. The DerivedClass1 class 
# inherits from the BaseClass, and the DerivedClass2 class 
# inherits from the DerivedClass1 class. This creates a hierarchy 
# where DerivedClass2 has access to all the attributes and methods 
# of both DerivedClass1 and BaseClass.



# class Animal:

#     def __init__(self,name):
#         self.name = name

#     def sound(self):
#         print(f'{self.name} is animal')


# class Dog(Animal):

#     def __init__(self,color):
#         Animal.__init__(self,name = 'Dog')
#         self.color = color

#     def sound(self):
#         Animal.sound(self)
#         print(f'The color of the dog is {self.color}')


# class Dog1(Dog):

#     def __init__(self,bread):
#         Dog.__init__(self,color = 'White')
#         self.bread = bread

#     def sound(self):
#         Dog.sound(self)
#         print(f'The one is last thing in bread {self.bread}')

# a = Dog1('homeone')                        
# a.sound()

# b = Dog('outone')
# b.sound()

# c = Animal('both')
# c.sound()




# class Animal:

#     def __init__(self,name,species):
#         self.name = name
#         self.species = species

#     def show(self):
#         print(f'The name is {self.name}')
#         print(f'The specie is {self.species}')


# class Dog(Animal):

#     def __init__(self,name,bread):
#         Animal.__init__(self,name,species = 'hybrid')
#         self.bread = bread

#     def show(self):
#         Animal.show(self)
#         print(f'The bread is {self.bread}')


# class Dog1(Dog):

#     def __init__(self,name,color):
#         Dog.__init__(self,name,bread = 'german')
#         self.color = color 

#     def show(self):
#         Dog.show(self)
#         print(f'The color is {self.color}')


# a = Dog("tommy", "Black")
# a.show()
# print(Dog1.mro())




# class Gfather:
 
#     def __init__(self, gfname):
#         self.gfname = gfname
 
 
# class Father(Gfather):
#     def __init__(self, fname, gfname):
#         self.fname = fname
#         Gfather.__init__(self, gfname)


# class Son(Father):
#     def __init__(self, sname, fname, gfname):
#         self.sname = sname
#         Father.__init__(self, fname, gfname)
 
#     def print_name(self):
#         print(f'Grandfather name : {self.gfname}')
#         print(f'Father name : {self.fname}')
#         print(f'Son name : {self.sname}')


# a = Son('san', 'shi', 'bal')
# # print(s1.gfname)
# a.print_name()

































































