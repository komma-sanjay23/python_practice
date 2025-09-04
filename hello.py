

"""
print('hello')


print("Hi Python") # Double quotes
print('Hello Python')


print('''Your Learning Path:
      \t-Python Basics
      \t-Data Engineering
      \t-AI''')


name='sam'
language='java'
print('My Name is', name)
print(name, 'is learning', language)      



name='datawithbaraa.com'
print('info@'+name)
print('support@'+name)
print('www.'+name)


# a='sanjay'
# b=50
# c=a+b
# # b=a.upper()
# print(c.upper())




print('sanjay'.upper())

print((-5).bit_length())

"""
'''
age=24
height=5.8
name='sanjay'
is_student=True
a=None

print(age,'\n',height,'\n',name,'\n',is_student,'\n',a)
print(type(age),type(height),type(name),type(is_student),type(a))
print(len(name))


num='+49 (176) 123-4567'
print(num.replace('+','00').replace('(','').replace(')','').replace('-','').replace(' ',''))



a='968-Maria, (D@t@ Engineer  ) ;; 27y  '

parts = a.split('-')
name_part = parts[1].split(',')[0].strip().lower()
print(name_part)
# print(parts)

role_part = a.split('(')[1].split(')')[0].replace('@','a').strip().lower()
print(role_part)

year_part=a.split(';;')[1].replace('y','').strip()
print(year_part)

print(f'My name is {name_part}, My role is {role_part}, and I am {year_part}')

'''
import random
import string 
# name_string = input('Enter the names of the seperated by comma:')
# names=name_string.split(',')
# name_len = len(names)
# choice=random.randint(0,name_len-1)
# print(names[choice])

'''
map = [
  ["⬜", "⬜", "⬜"],
  ["⬜", "⬜", "⬜"],
  ["⬜", "⬜", "⬜"]
]

print(f"{map[0]}\n{map[1]}\n{map[2]}")

# 32 column row 
position=input('Enter the no.: ')
column = int(position[0])-1
row = int(position[1])-1

map[row][column] = 'X'

print(f"{map[0]}\n{map[1]}\n{map[2]}")

'''

import math 

# number = random.randint(1,100)
# if number%2 == 0:
#     print(f'My number is {number} and it is Even')
# else:
#     print(f"My number is {number} and it is Odd")    



# num = int(input('Enter the num: '))
# a=math.sqrt(num)
# print(round(a),num**0.5)

'''

email='*abc.g@mail@.com'
email=email.strip()
if email == '':
    print("Email not be empty.")
elif not('.' in email and '@' in email):
    print('Email must contain . and @')    
elif email.count('@') != 1:
    print('Email must contain only one @')
elif not(email.endswith(('.org','.net','.com'))):
    print('Email must end with .org or .net or .com')  
elif not (len(email) <= 254):
    print('Email not be longer that 254 chars')   
elif not(email[0].isalnum() and email[-1].isalnum()):
    print('Email is start and with digit or letter')       
else:
    print('Email is valid')        



email='abc@gmail.com'
valid = True
email=email.strip()
if email == '':
    print("Email not be empty.")
    valid = False
if not('.' in email and '@' in email):
    print('Email must contain . and @')   
    valid = False 
if email.count('@') != 1:
    print('Email must contain only one @')
    valid = False
if not(email.endswith(('.org','.net','.com'))):
    print('Email must end with .org or .net or .com') 
    valid = False 
if not (len(email) <= 254):
    print('Email not be longer that 254 chars')   
    valid = False
if not(email[0].isalnum() and email[-1].isalnum()):
    print('Email is start and with digit or letter') 
    valid = False      
if valid:
    print('Email is valid') 

'''

'''
email = 'abc@gmail.com'
password = 'Abc@gmail.commm'
password = password.strip()

print(sorted(password))
print(sorted(password)[-1].islower())
if password == '':
    print('Password must not be empty')
elif not(len(password) >= 8):
    print('Password must be atleast 8 characters')
elif password == email:
    print('Password not be same as email') 
elif not(password[0].isalnum() and password[-1].isalnum()):
    print('Password must start with digit or letter')  
# elif sorted(password)[-1].islower()      
else:
    print('Password is valid')
'''




'''
string='sA'


has_upper = False
has_lower = False

for char in string:
    if char.isupper():
        has_upper=True
    else:
        has_lower=True    
# return has_upper and has_lower
'''


# number = 7 
# for i in range(1,11):
#     print(f'{number} x {i} = {7*i}')




# n=5
# for i in range(n):
#     for j in range(i+1):
#         print('*',end='')
#     print()  


# n=5
# for i in range(n):
#     print('*'*(i+1))





# n=5
# for i in range(n):
#     for j in range(n-i):
#         print('*',end='')
#     print()    


# n=5
# for i in range(n):
#     print('*'*(n-i))



# n=6
# for i in range(1,n):
#     print(' ' *(n-i-1) + '*'*i) 


# n=6
# for i in range(1,n):
#     print(' '*(i-1) + '*'*(n-i)) 



# n=5
# for i in range(1,n):
#     print(' '*(n-i) + '*'*((2*i)-1))



# n=5
# for i in range(n):
#     print(' '*i +'*'*(2*(n-i)-1))


# n=5
# for i in range(1,n):
#     print(' '*(n-i) + '*'*((2*i)-1))

# for i in range(n-1,0,-1):
#     print(' '*(n-i) + '*'*((2*i)-1))


# n=5
# for i in range(n):
#     print(i * (i+1))

# n=5
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end='')
#     print() 


# text = input("Enter a string: ")

# uppercase = sum(1 for ch in text if ch.isupper())
# lowercase = sum(1 for ch in text if ch.islower())
# digits = sum(1 for ch in text if ch.isdigit())
# special = len(text) - (uppercase + lowercase + digits)

# print(f"Uppercase: {uppercase}, Lowercase: {lowercase}, Digits: {digits}, Special: {special}")



# print(math.lcm(3,4))

# print(math.factorial(23))

# print(math.gcd(23,47))


# print(math.perm(6,3))

# print(math.fabs(-78))


# print(math.trunc(-78.6754))

# print(math.sqrt(67))

# print(math.isqrt(67))

# print(math.pow(2,53))
# print(math.cbrt(343))




# num = int(input('Enter the password len:'))

# total_words = string.ascii_letters + string.digits + string.punctuation
# password = ''.join(random.choice(total_words) for i in range(num))
# print(password)


# number=10
# print(number.bit_length())


# names=[]
# for i in range(1,6):
#     name = input(f"Enter the name {i}: ")
#     names.append(name)
# names.sort()
# print(names)    



# tup = ('apple','banana','cherry','date','elderberry')
# print(tup[2])

# tupp = list(tup)
# tupp.append('fig')
# print(tupp)

# for i in range(1,51):
#     if i%2 == 0:
#         print(i,end=' ')
#     # else:
#     #     print(f"{i} is Odd")    


# nums=[]
# for i in range(1,6):
#     num = int(input(f'Enter the num {i}: '))
#     nums.append(num)
# total = sum(nums)   
# ave = total / len(nums) 

# print(total)
# print(ave)
# print(f'The total is {total}')



# word = input("Enter a word: ").strip().split(' ')
# # word=word.split(' ')
# print(word, len(word))
# print(word[0],word[-1])





# txt = input("Enter a sentence: ").strip().lower()
# vowels = 'aeiou'
# count = 0
# for char in txt:
#     if char in vowels:
#         count += 1
# print("Number of vowels:", count)


# sett = {1,2,3,4,5,6,7,8,9,10}
# print([i for i in sett if i%2 ==1])

# nums = set(range(1,11))
# print([i for i in nums if i%2 == 1])


# word = input("Enter a word: ").replace(' ','').lower()  
# if word == word[::-1]:
#     print(f"The word '{word}' is a palindrome.")
# else:
#     print(f"The word '{word}' is not a palindrome.")



# def factorial(n):
#     if n < 0:
#         return None
#     elif n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)
# input_num = int(input("Enter a number: "))
# print(factorial(input_num))



# nums = [1,2,3,4,5,6,7,8,9,10]
# nums = range(1,11)
# def square_numbers(nums):
#     return [n**2 for n in nums]
# print(square_numbers(nums))




# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n**0.5) + 1):   #interesting
#         if n % i == 0:
#             return False
#     return True

# # num = int(input("Enter a number: "))
# # if is_prime(num):
# #     print(f"{num} is a prime number.")
# # else:
# #     print(f"{num} is not a prime number.")


# nums = [n for n in range(1,101) if is_prime(n)]
# print(nums)






# num= int(input("Enter a number: "))
# a = round(float(math.sqrt(num)),3)
# b = round(float(math.pow(num,3)),3)
# print(a,b)









# word = input("Enter a word: ").strip().split(' ')
# # word=word.split(' ')
# # print(word, word[::-1])
# r = ' '.join(reversed(word))
# print(r)
# print(word[0],word[-1])




# word = input("Enter a word: ").strip().split(' ')
# print(word)
# for i in word:
#     print(count i in word)



import calendar

# yy = 2025
# mm = 9
# print(calendar.month(yy,mm))





# number gussing game

# random_number = random.randint(1,15)
# count = 0

# while True:
#     user_guess = int(input("Enter your guess (1-15): "))
#     if user_guess < 1 or user_guess > 15:
#         print("Please guess a number between 1 and 15.")   
#     elif user_guess < random_number:
#         print("Too low! Try again.")
#         count += 1 
#     elif user_guess > random_number:
#         print("Too high! Try again.")
#         count += 1
#     else:
#         print(f"Congratulations! You've guessed the number in {count} attempts.")
#         break





# random_number = random.randint(1,25)
# print("Welcome to the Number Guessing Game!")
# print("I'm thinking of a number between 1 and 25.")

# while True:
#     user_guess = int(input("Enter your guess: "))
#     # print(random_number)
#     if user_guess < 1 or user_guess > 25:
#         print("Please guess a number between 1 and 25.")
#     elif user_guess == random_number:
#         print("Congratulations! You've guessed the number.")
#         # print(random_number)
#         break
#     else:
#         print("Try again!")



# n = int(input("Enter a number: "))
# fib = [0,1]
# for i in range(n-2):
#     fib.append(fib[-1] + fib[-2])
# print(fib)




# dicte = {'name:' : 'sanjay','age:' : 25,'city:' : 'new york'}
# for key,value in dicte.items():
#     print(key,value)

# print(dicte)
# print(dicte['name'])
# print(dicte.get('age'))
# print(dicte.keys())
# print(dicte.values())
# print(dicte.items())



# lst = [10,20,25,30]
# print(25 in lst)

# if 25 in lst:
#     print("25 is in the list")
# else:
#     print("25 is not in the list")

# a = " Python Programming"
# vowels = 'aeiouAEIOU'
# count = sum(1 for char in a if char in vowels)
# print("Number of vowels:", count)


# lst = [1,2,3,4]
# tupl = tuple(lst)
# print(tupl)



# dict1 = {'name': 'sanjay', 'age': 25, 'city': 'new york'}
# dict2 = {'names': 'john', 'ages': 30, 'citys': 'los angeles'}
# # dict3 = {**dict1, **dict2}
# print({**dict1, **dict2})


# lst = [1,2,3,4]
# lst[0],lst[-1] = lst[-1],lst[0]
# # lst[-1] = lst[0]
# print(lst)


# lst = [10,1,2,3,4,1,2,6,7,5,5,7,8,9]
# unique = []
# for i in lst:
#     if i not in unique:
#         unique.append(i)
# unique.sort()
# print(unique)



# tup = (1, 2, 3, 4)
# print(tup[::-1])


# str1 = "apple banana mango"
# for i in str1.split(' '):
#     print(i)
# # str1 = str1.split(' ')
# # print(str(str1),end='\n')


# prices = {"apple": 50, "banana": 30, "mango": 80}

# for fruit, price in prices.items():
#     if price > 40:
#         print(f"The price of {fruit} is {price}.")


# words = ["apple", "banana", "kiwi", "pear"]
# # sorted_words = sorted(words, key=len)
# print(sorted(words, key=len))


# set1 = {1, 2, 3}
# set2 = {2, 3, 4}
# print(set1 & set2)



# a="programming with sanjay"
# count = 0 
# for i in a:
#     if i not in a[:count]:
#         print(f"{i}: {a.count(i)}")
#     count += 1  


# keys = ["name", "age"]
# values = ["John", 25]
# mapped = dict(zip(keys, values))
# print(mapped)



# lst = ["apple", "", "banana", "", "cherry"]
# filtered = [fruit for fruit in lst if fruit]
# print(filtered)


# a="programming with sanjay"
# a=a.split(' ')
# ans = max(a, key=len)
# print(ans,(len(ans)))



# def palindrome(s):
#     # s = input("Enter a string: ")
#     s = s.lower().replace(" ", "")
#     if s == s[::-1]:
#         print(f"Yes, {s} is a palindrome!")
#     else:
#         print(f"No, {s} is not a palindrome.")

# palindrome("level")



# list1 = [1, 2, 3]
# list2 = [3, 4, 5]
# merged = list(set(list1  + list2))
# print(merged)



# data = [{"name": "Alice", "score": 90}, {"name": "Bob", "score": 95}]
# a = max(data, key=lambda x: x['score'])
# print(a)

# strings = ["apple", "banana", "cherry"]
# a = set("".join(strings))
# print(a)


# nested = [[1, 2], [3, 4], [5, 6],[7,8],[9,87,8]]

# flattened = [item for i in nested for item in i]
# print(flattened)


# scores = {"Alice": 50, "Bob": 75, "Charlie": 60}
# a = dict(sorted(scores.items(), key=lambda x: x[1], reverse=True))
# print(a)


# products = [("Laptop", 1200), ("Mouse", 25), ("Phone", 800)]
# a = dict([p for p in products if p[1] > 100])
# print(a)


# def anagram(a1,a2):
#     if sorted(a1.lower()) == sorted(a2.lower()):
#         return True
#     return False    

# print(anagram("listen", "silent"))
# # print(anagram("hello", "world"))


# pairs = [("a", 10), ("b", 20), ("a", 5)]

# import pandas as pd
# data = [{"name": "Alice", "score": 90}, {"name": "Bob", "score": 95}]
# df = pd.DataFrame(data)
# print(df)



# a = 'I am sanjay komma and my email is so and so '
# a = a.split(' ')
# for word in a:
#     print(word)


# import time
# timestamp = time.strftime('%H:%M:%S')
# print(timestamp)
# # timestamp = time.strftime('%H')
# # print(timestamp)
# # timestamp = time.strftime('%M')
# # print(timestamp)
# # timestamp = time.strftime('%S')
# # print(timestamp)
# # # https://docs.python.org/3/library/time.html#time.strftime


# hour = int(time.strftime('%H'))
# print(hour)
# if hour <= 11:
#     print("Good Morning")
# elif hour >= 12 and hour < 18:
#     print("Good Afternoon")
# else:
#     print("Good Evening")


# colors = ["Red", "Green", "Blue", "Yellow"]
# for x in colors:
#     print()
#     for i in x:
#         print(i)
#     # print(x)

# for i in range(2, 6):
#     for j in range(1, 11):
#         print(f"{i} x {j} = {i*j}")
#     print("-" * 10)



# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# transpose = []
# for i in range(len(matrix[0])):
#     row = []
#     for j in range(len(matrix)):
#         row.append(matrix[j][i])
#     transpose.append(row)

# print(transpose)



# n=5
# for i in range(1, n+1):
#     print(' ' * (n - i) + '*' * (2*i - 1))

# for i in range(n-1, 0, -1):
#     print(' ' * (n - i) + '*' * (2*i - 1))



# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# k = int(input("Enter the value of k: "))
# n = len(lst)
# temp1 = []
# temp2 = []
# for i in range(k):
#     temp1.append(lst[i])
# temp1.reverse()

# for i in range(k, n):
#     temp2.append(lst[i])
# temp2.reverse()
# add = temp1 + temp2    
# add.reverse()

# print(add)


# num = 6
# while num != 1:
#     print(num, end=" ")
#     if num % 2 == 0:
#         num //= 2
#     else:
#         num = num * 3 + 1
# print(1)




# def fib(num):
#   '''Takes num and returns fibonacci series'''
#   if num ==0:
#     return 0
#   elif num==1:
#     return 1
#   else:
#     return fib(num-1)+fib(num-2)
# print(fib.__doc__)
# for i in range(10):
#   print(fib(i),end=" ")


# login = "user"
# password = input("Enter the password: ")
# i = 0
# while i < 3:
#     password = input("Enter the password: ")
#     if password == "pass":
#         print("Login successful!")
#         break
#     else:
#         i += 1
#         print("Try again.")
# else:
#     print("Login failed.")




# for i in range(1,101):
#     print(i ,end=" ")
#     if(i==5):
#         break
#     else:
#         print("Mississippi")
# print("Thank you")



# def average(**nums):
#   total = 0
#   for i in nums.values():
#       total += i
#   print("The average is ",int( total / len(nums)))


# c = average(a=5, b=6, c=72, d=1)
# # c = int(c)
# print(c)


# a = 'sanjaybhargav'
# print(a[5::-1])

# l = [11, 45, 1, 2, 4, 6, 1, 1]
# m = [900, 1000, 1100]
# l.extend(m)
# print(l)



# tup = (1, 2, 76, 342, 32, "green", True)
# tup2 = tup[1:4]
# print(tup2)


# price = 49.09999
# txt = f"For only {price:.2f} dollars!"
# print(txt)

# info = {"Carla", 19, False, 5.9, 19}
# print(info)

# harry = set()
# print(type(harry))

# for value in info:
#   print(value)

# s1 = {1,3,5,6,4,7,8,9}
# s2 = {5,6,7,9,10,11,12}
# # print(s1.union(s2))
# # print(s1.intersection(s2))
# s2.intersection_update(s1)
# print(s2)
# # print(s1.difference(s2))
# # print(s1.symmetric_difference(s2))



# def count_vowels(s):
#     return sum(1 for ch in s.lower() if ch in "aeiou")
# print(count_vowels("hello world"))



# def amstrong_number(n):
#     sum = 0
#     for i in str(n):
#         sum += int(i) ** len(str(n))
#     return n == sum 
# print(amstrong_number(371))

# def amstrong(n):
#     return n == sum(int(i)**len(str(n)) for i in str(n))

# print(amstrong(371))



# a = 'sanjaybhargav'
# for i in set(a):
#     a.count(i)
#     print(f"{i}: {a.count(i)}")

# a = 'sanjaybhargav'
# for i in a:
#     a.count(i)
#     print(f"{i}: {a.count(i)}")

# s = "hello world"
# print({ch: s.count(ch) for ch in set(s)})

# a = 'sanjaybhargavejigeovu'
# # if a:
# #     a = a.replace('a', '')
# #     a = a.replace('e', '')
# #     a = a.replace('i', '')
# #     a = a.replace('o', '')
# #     a = a.replace('u', '')
# #     print(a)

# ans = [i for i in a if i not in 'aeiou']
# print(''.join(ans))

# ans = (i for i in a if i not in 'aeiou')
# print(''.join(ans))

# a = 'sanjay'
# b = 'jsayan'
# if sorted(a) == sorted(b):
#     print("The strings are anagrams.")
# else:
#     print("The strings are not anagrams.")

# a = 'sanjay'
# b = 'jsayan'
# if sorted(a,reverse = True) == sorted(b,reverse = True):
#     print("The strings are anagrams.")
# else:
#     print("The strings are not anagrams.")


# a = 'snajay bhargav komma and i am in austin'
# a = a.replace(' ','_')
# print(a)


# a = 'snajay bhargav komma and i am in austin'
# for i in a.split():
#     print(i,len(i))


# a = 'snajay bhargav komma and i am in austin'
# a = max(a.split(),key = len)
# print(a,len(a))


# a = 'snajay bhargav komma and i am in austin'
# print(max(a.split(), key=len))


# a = 'snajay bhargav komma and i am in austin'
# print(a.title())



# def func(a):
#     for i in a.split():
#         i = i.capitalize()
#         print(''.join(i))

# a = 'snajay bhargav komma and i am in austin'
# func(a)
# # for i in a.split():
# #     i = i.capitalize()
# #     print(''.join(i))



# print(' '.join(i.capitalize() for i in a.split()))

# a = "this is is a test"
# a = 'sanjay bhargav komma i and i am in austin'.split()
# for i in set(a):
#     print(f"{i}: {a.count(i)}")

# a = 'sanjay bhargav komma i and i am in austin'.split()
# for i in a:
#     print(i[::-1])


# a = 'sanjay bhargav komma i and i am in austin'.split()
# print(' '.join(i[::-1] for i in a))


# lst = [1,4,6,3,67,33,62,12,67,86,95]
# print(max(lst),min(lst),sum(lst),len(lst),sorted(lst),sorted(lst,reverse=True))


# lst = [1,4,6,3,67,33,62,12,67,86,95]
# lst.sort()
# print(lst)  


# lst = [1,4,6,3,67,33,62,12,67,86,95]
# print(sorted(lst))  


# lst = [1,4,6,3,67,33,62,12,67,86,95,1,4,67,33]
# lst = set(lst)
# print(list(lst))


# lst = [1,4,6,3,67,33,62,12,67,86,95]
# lst1 = [1,4,6,3,67,33,62,12,67,86,95,1,4,67,33]
# lst = set(lst)
# lst1 = set(lst1)
# lst.intersection(lst1)
# lst = list(lst)
# print(lst)



# lst = [1,4,6,3,67,33,62,12,67,86,95]
# lst1 = [1,4,6,3,67,33,62,12,67,86,95,1,4,67,33]
# lst = set(lst)
# lst1 = set(lst1)

# a = lst.union(lst1)
# a = list(a)
# print(a)



# lst = [1,4,6,3,67,33,62,12,67,86,95,1,4,67,33]

# k=5
# lst1 = [1,2,3,4,5,6,7,8,9,10]
# # lst1[5:] + lst1[:5]
# print(lst1[k:] + lst1[:k])


# def rotate(k):
#     return lst1[k:] + lst1[:k]  


# k = int(input('Enter the k value:'))
# lst1 = input('Enter the list values separated by comma:').split(',')
# # lst1 = [1,2,3,4,5,6,7,8,9,10]
# print(rotate(k))


# lst = [1,4,6,3,67,33,62,12,67,86,95,1,4,67,33]
# lst = sorted(lst)
# lst = set(lst)
# print(lst)


# lst = [1,4,6,3,67,33,62,12,67,86,95,1,4,67,33]
# # print(lst)
# lst = set(lst)
# lst = sorted(lst)
# lst = list(lst)
# print(lst[-2])


# lst = [1,4,6,3,67,33,62,12,67,86,95,1,4,67,33]
# for i in set(lst):
#     print(f'{i}:{lst.count(i)}')


# list_of_tuples = [("a", 1), ("b", 2)]
# list_of_tuples = dict(list_of_tuples)
# print(list_of_tuples)


# t = (1, 2, 3,4,5)
# a, b, c, d, e = t
# print(a, b, c, d, e)


# s1 = {1,2,3,4,5}
# s2 = {4,5,6,7,8}
# print(s1 | s2)
# print(s1 & s2)
# print(s1 - s2)
# print(s2 - s1)
# s3 = s1.union(s2)
# s4 = s1.intersection(s2)
# s5 = s1.difference(s2)
# s6 = s2.difference(s1)
# print(s3)
# print(s4)
# print(s5)
# print(s6)


# s1 = {1,2,3,4,5}
# s2 = {4,5,6,7,8}

# s7 = s1.issubset(s2)
# s8 = s2.issubset(s1)
# print(s7)
# print(s8)


# s1.discard(2)
# print(s1)



# lst = [1,4,6,3,67,33,62,12,67,86,95,1,4,67,33]
# for i in dict.fromkeys(lst):
#     print(f'{i}:{lst.count(i)}')

# lst = [1,4,6,3,67,33,62,12,67,86,95,1,4,67,33]
# for i in set(lst):
#     print(f'{i}:{lst.count(i)}')


# sentence = "hello world hello".split()
# # s = sentence.split()
# for word in set(sentence):
#     print(f'{word}: {sentence.count(word)}')

# print({word: sentence.count(word) for word in set(sentence)})





# dict1 = {"a": 1}
# dict2 = {"b": 2}

# dict3 = {**dict1, **dict2}
# print(dict3)


# dict1 = {'a' : 2, 'c': 9, 'd': 4, 'e': 1}
# sorted_dict1 = dict(sorted(dict1.items(),key = lambda item: item[1]))
# print(sorted_dict1)
# -------------------research------------------------------------------------------



# dict1 = {'a' : 2, 'c': 9, 'd': 4, 'e': 1}
# # for k,v in dict1.items():
# #     print(f'{v}: {k}')


# print({v:k for k,v in dict1.items()})


# dict1 = {'a' : 2, 'c': 9, 'd': 4, 'e': 1}
# max_key = max(dict1, key=lambda k: dict1[k])
# print(max_key)


# dict1 = {'a' : 2, 'c': 9, 'd': 4, 'e': 1}
# max_key = max(dict1, key=dict1.get)
# print(max_key, dict1[max_key])

# dict1 = {'a' : 2, 'c': 9, 'd': 4, 'e': 1}
# print(max(dict1,key = dict1.get))


# dict1 = {'a' : 2, 'c': 9, 'd': 4, 'e': 1}
# print({k:v for k, v in dict1.items()})
#     # print(f'{k}: {v}')

# dict1 = {'a' : 2, 'c': 9, 'd': 4, 'e': 1}
# print(dict1.keys())

# dict1 = {'a' : 2, 'c': 9, 'd': 4, 'e': 1}
# print(dict1.values())


# print(dict1 == dict2)


# dict1 = {'a' : 2, 'c': 9, 'd': 4, 'e': 1}
# dict1.pop('c')
# print(dict1)

# dict1 = {'a' : 2, 'c': 9, 'd': 4, 'e': 1}
# dict1.popitem()
# print(dict1)

# dict1 = {'a' : 2, 'c': 9, 'd': 4, 'e': 1}
# dict1.pop('a', None)
# print(dict1)

# dict1 = {'a' : 2, 'c': 9, 'd': 4, 'e': 1}
# dict1.update({'f': 6})
# print(dict1)



# dict1 = {"a",'b','c'}
# dict2 = 0
# c = dict.fromkeys(dict1,dict2)
# print(c)


# stack = []
# stack.append(1)
# stack.append(2) 
# stack.append(3)
# stack.append(4)
# # stack.pop()
# # stack.pop()
# print(stack.pop())
# print(stack)


# ---------------------------------------
s = 'swiwss'
for i in s:
    if s.count(i) == 1:
        print(i)
        break
else:
    print(None)



# print([i for i in s if s.count(i) == 1])











# Stack implementation using list.

# Queue implementation using collections.deque.

# Find the first non-repeating character in a string.

# Find all pairs in a list that sum to a target.

# Group anagrams from a list of words.

# Find the most frequent element in a list.

# Implement binary search on a sorted list.

# Find missing number from a sequence.

# Flatten a nested list.

# Find subarray with the maximum sum (Kadane’s Algorithm).




s = "A man, a plan, a canal: Panama"
s = s.replace(',','').replace(':','').replace(' ','').lower().strip()
if s == s[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")


# s = 'The quick brown fox jumpss'
# s = s.split()
# print({i:s.count(i) for i in set(s) })


# s = 'The quick brown fox jumpss fox'
# s = s.split()
# print({i:s.count(i) for i in s})




# s = 'The quick brown fox jumpss'
# s = s.split()
# for i in set(s):
#     print(i,len(i))


# s = 'The quick brown fox jumpss'
# a = max(len(i) for i in s.split())
# print(a)

# def longest_word(s):
#     max_length = 0
#     for i in s.split():
#         max_length = max(max_length, len(i))
#     return max_length

# print(longest_word("The quick browhhhn fox jumpss"))


# s = 'The quick brhhhown fox jumpss'
# n = s.split()
# final = ''
# max_length = max(len(i) for i in n)
# for i in n:
#     if len(i) == max_length:
#         final += i
# print(final)


s = 'The quick brhhhhown fox jumpss'.split()
high = ''
for i in range(len(s)):
    # print(len(s[i]))
    if len(s[i]) > len(high):
        high = s[i]
print(high)


print('hello')





# s = 'The quick brown fox jumpss'
# for i in s.split():
#     print(i,len(i))












# pip install google-generativeai

# import google.generativeai as genai

# API_KEY = 'AIzaSyDSe7flBnfjzNfptZB79Skk8B5PaIDfZVs'
# genai.configure(api_key=API_KEY)


# model = genai.GenerativeModel('gemini-2.0-flash')
# chat = model.start_chat()


# print("Chat with Gemini! Type 'exit' to quit.")
# while True:
#     user_input = input("You: ")
#     if user_input.lower() == 'exit':
#         break
#     response = chat.send_message(user_input)
#     print('Gemini:',response.text)




# response = chat.send_message('hello')
# print('Gemini:',response.text)







# print(int(eval(input("Enter: "))))   intresting






























# n=5
# for i in range(n):
#     for j in range(n):
#         if i==0 or j==0 or i==n-1 or j==n-1:
#             print('*',end='')
#         else:
#             print(' ',end='')
#     print()            



# n=5
# for i in range(n):
#     print('*'*n if i in [0,n-1] else '*' + ' '*(n-2) + '*')



















