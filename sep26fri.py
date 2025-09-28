


# Hierarchical Inheritance

# Hierarchical Inheritance is a type of inheritance in 
# Object-Oriented Programming where multiple subclasses inherit 
# from a single base class. In other words, a single base class 
# acts as a parent class for multiple subclasses. This is a way 
# of establishing relationships between classes in a hierarchical 
# manner.


# When more than one derived class are created from a single base 
# this type of inheritance is called hierarchical inheritance. 
# In this program, we have a parent (base) class and two child 
# (derived) classes.


# syntax

# class BaseClass:
#   pass

# class D1(BaseClass):
#   pass

# class D2(BaseClass):
#   pass

# class D3(D1):
#   pass


# exm:

# class Parent:

#     def func1(self):
#         print("This function is in parent class.")


# class Child1(Parent):

#     def func2(self):
#         print("This function is in child 1.")
      

# class Child2(Parent):

#     def func3(self):
#         print("This function is in child 2.")
 
# object1 = Child1()
# object2 = Child2()

# object1.func1()
# object1.func2()
# object2.func1()
# object2.func3()


# class Animal:

#     def __init__(self,name):
#         self.name = name

#     def show(self):
#         print(f'The of animal is {self.name}')

# class Dog(Animal):

#     def __init__(self,color):
#         Animal.__init__(self,name = 'Homeone')
#         self.color = color

#     def show(self):
#         Animal.show(self)
#         print(f'The color of the animal is {self.color}')

# class Cat(Animal):

#     def __init__(self,bread):
#         Animal.__init__(self,name = 'Homeone')
#         self.bread = bread            

#     def show(self):
#         Animal.show(self)
#         print(f'The bread is {self.bread}')    

# a = Cat('german')
# a.show()




# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def show_details(self):
#         print("Name:", self.name)

# class Dog(Animal):
#     def __init__(self, name, breed):
#         Animal.__init__(self, name)
#         self.breed = breed

#     def show_details(self):
#         Animal.show_details(self)
#         print("Species: Dog")
#         print("Breed:", self.breed)

# class Cat(Animal):
#     def __init__(self, name, color):
#         Animal.__init__(self, name)
#         self.color = color

#     def show_details(self):
#         Animal.show_details(self)
#         print("Species: Cat")
#         print("Color:", self.color)


# class Fox(Cat):

#     def __init__(self,name,thing):
#         Cat.__init__(self,name,color = 'gold')
#         self.thing = thing

#     def show_details(self):    
#         Cat.show_details(self)
#         print(f'The nature of the {self.name} is {self.thing}')


# # dog = Dog("Max", "Golden Retriever")
# # dog.show_details()
# # cat = Cat("Luna", "Black")
# # cat.show_details()
# fox = Fox('fox1','austraila')
# fox.show_details()




# Hybrid Inheritance:


# Hybrid inheritance is a combination of multiple inheritance and 
# single inheritance in object-oriented programming. It is a type 
# of inheritance in which multiple inheritance is used to inherit 
# the properties of multiple base classes into a single derived 
# class, and single inheritance is used to inherit the properties 
# of the derived class into a sub-derived class.

# In Python, hybrid inheritance can be implemented by creating a 
# class hierarchy, in which a base class is inherited by multiple 
# derived classes, and one of the derived classes is further 
# inherited by a sub-derived class.

# Inheritance consisting of multiple types of inheritance is 
# called hybrid inheritance.

# syntax:

# class BaseClass:
#   pass

# class Derived1(BaseClass):
#   pass  

# class Derived2(BaseClass):
#   pass  

# class Derived3(Derived1, Derived2):
#   pass




# class BaseClass1:
#   # attributes and methods

# class BaseClass2:
#   # attributes and methods

# class DerivedClass(BaseClass1, BaseClass2):
#   # attributes and methods


# Exmp:


# class School:

#     def func1(self):
#         print("This function is in school.")
 
 
# class Student1(School):

#     def func2(self):
#         print("This function is in student1. ")
 
 
# class Student2(School):

#     def func3(self):
#         print("This function is in student2.")
 
 
# class Student3(Student1, School):

#     def func4(self):
#         print("This function is in student3.")
 

# object = Student3()
# object.func1()
# object.func2()
# # object.func3()    gives error 




# class Human:
  
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age
    
#   def show_details(self):
#     print(f'Name:  {self.name}')
#     print(f'Age:  {self.age}')
    

# class Person(Human):
  
#   def __init__(self, name, age, address):
#     Human.__init__(self, name, age)
#     self.address = address
    
#   def show_details(self):
#     Human.show_details(self)
#     print(f'Address: {self.address}')
    

# class Program:
  
#   def __init__(self, program_name, duration):
#     self.program_name = program_name
#     self.duration = duration
    
#   def show_details(self):
#     print(f'Program Name: {self.program_name}')
#     print(f'Duration: {self.duration}')
    

# class Student(Person):
  
#   def __init__(self, name, age, address, program):
#     Person.__init__(self, name, age, address)
#     self.program = program
    
#   def show_details(self):
#     Person.show_details(self)
#     self.program.show_details()


# program = Program("Computer Science", 4)
# student = Student("John Doe", 25, "123 Main St.", program)
# student.show_details()















































# class ParentClass:
#     def parent_method(self):
#         print("This is the parent method.")

# class ChildClass(ParentClass):
#     def child_method(self):
#         super().parent_method()
#         print("This is the child method.")
#         # super().parent_method()

# child_object = ChildClass()
# child_object.child_method()




































































