

# class Dog:

#     def __init__(self,name,bread):
#         self.name = name
#         self.bread = bread

# a = Dog('chotu','germen')
# print(a.name)        



# Encapsulation with private variable

# class Account:

#     def __init__(self,balance = 0):
#         self.__balance = balance

#     def deposit(self,amount):
#         self.__balance += amount

#     def total_balance(self):        
#         return self.__balance

# a = Account()
# a.deposit(500)
# print(a.total_balance())



# class Vehicle:

#     def __init__(self, brand):
#         self.brand = brand

# class Car(Vehicle):

#     def __init__(self, brand, model):
#         super().__init__(brand)
#         self.model = model


# a = Car("Toyota", "Corolla")
# print(a.brand, a.model)




# class Animal:

#     def sound(self):
#         return "Some sound"

# class Mammal(Animal):

#     def sound(self):
#         return "Mammal sound"

# class Dog(Mammal):

#     def sound(self):
#         return "Bark"

# a = Dog()
# print(a.sound())  



# class A:

#     def method(self):
#         return "From A"

# class B:

#     def method(self):
#         return "From B"

# class C(B,A):
#     pass
#     # def method(self):
#     #     return "From A if it is first in MRO"

# c = C()
# print(c.method())  


# class Bank:

#     def __init__(self,anumber,balance):
#         self.anumber = anumber
#         self.balance = balance

#     def deposit(self,amount):
#         self.balance += amount

#     def withdraw(self,amount):
#         if amount <= self.balance:
#             self.balance -= amount
#         else:    
#             return "Insufficient funds"
        
#     def total_balance(self):
#         return self.balance
    
# a = Bank('345',500)
# a.deposit(500)
# a.withdraw(90)
# print(a.anumber,a.total_balance())    



# class Emp:

#     def __init__(self,name,sal):
#         self.name = name
#         self.sal = sal
    
#     def t_sal(self):
#         return self.sal*12
    
# class Client(Emp):

#     def __init__(self,name,sal,bonus):
#         super().__init__(name,sal)
#         self.bonus = bonus    

#     def t_sal(self):
#         return super().t_sal() + self.bonus
    

# a = Client('san',5000,900)
# print(a.t_sal())




# class Person:

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# class Student(Person):

#     def __init__(self, name, age, student_id):
#         super().__init__(name, age)
#         self.student_id = student_id

# a = Student("Alice", 20, "S101")
# print(a.name, a.age, a.student_id)  




# class Father:

#     def skill(self):
#         return "Gardening"

# class Mother:

#     def skill(self):
#         return "Cooking"

# class Child(Father, Mother):

#     def skill(self):
#         return Father.skill(self) + " & " + Mother.skill(self)

# c = Child()
# print(c.skill())  




# class Animal:

#     def speak(self):
#         return "Animal sound"

# class Mammal(Animal):

#     def speak(self):
#         return "Mammal sound"

# class Dog(Mammal):

#     def speak(self):
#         return "Bark"

# a = Mammal()
# print(a.speak())  

# b = Animal()
# print(b.speak())

# c = Dog()
# print(c.speak())



# class Vehicle:

#     def __init__(self, brand):
#         self.brand = brand


# class Car(Vehicle):

#     def __init__(self, brand, model):
#         super().__init__(brand)
#         self.model = model


# class Bike(Vehicle):

#     def __init__(self, brand, cc):
#         super().__init__(brand)
#         self.cc = cc


# a = Car("Toyota", "Corolla")
# b = Bike("Yamaha", 150)
# print(a.brand, a.model)  
# print(b.brand, b.cc)     



# class A:

#     def method(self):
#         return "From A"

# class B(A):

#     def method(self):
#         return "From B"

# class C(A):

#     def method(self):
#         return "From C"

# class D(B, C):  
#     pass

# a = D()
# print(a.method())  

# b = C()
# print(b.method())



# class A:
#     def show(self):
#         return "A"

# class B(A):
#     def show(self):
#         return "B"

# class C(A):
#     def show(self):
#         return "C"

# class D(B, C): 
#     pass

# d = D()
# print(d.show())       
# print(D.mro())       



# class Bank:

#     def __init__(self,anumber,name,balance = 0):
#         self.anumber = anumber
#         self.name = name
#         self.balance = balance

#     def deposit(self,amount):
#         self.balance += amount
#         return self.balance
    

# class Saving(Bank): 

#     def __init__(self,anumber,name,balance,intrest = 0.05):
#         super().__init__(anumber,name,balance)
#         self.intrest = intrest

#     def add_intrest(self):
#         self.balance += self.balance * self.intrest 
#         return self.balance
    
# a = Saving(123,'san',500)
# a.deposit(500)
# print(a.add_intrest())




# class Camera:

#     def take_photo(self):
#         return "Photo captured"

# class Phone:

#     def make_call(self):
#         return "Calling"

# class Smartphone(Camera, Phone):

#     def browse(self):
#         return "Browsing internet"


# a = Smartphone()
# print(a.take_photo())  
# print(a.make_call())  
# print(a.browse())      



# class Person:

#     def __init__(self, name):
#         self.name = name


# class Employee(Person):

#     def __init__(self, name, emp_id):
#         super().__init__(name)
#         self.emp_id = emp_id


# class Manager(Employee):

#     def __init__(self, name, emp_id, department):
#         super().__init__(name, emp_id)
#         self.department = department


# a = Manager("John", "E123", "IT")
# print(a.name, a.emp_id, a.department) 























































