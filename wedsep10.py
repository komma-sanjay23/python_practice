




# Create a function to check if a string is a pangram (contains all letters A–Z).

# Create a function to return the intersection of two lists.

# Create a function that returns the largest word in a sentence.

# Write a function to convert snake_case string to camelCase.

# Create a function that returns a dictionary of character counts from a string.

# Write a recursive function to calculate the sum of digits of a number.

# Create a function to count the number of uppercase and lowercase letters in a string.

# Write a function to remove all special characters from a string.

# Create a function to merge two dictionaries and sum the values of common keys.

# Create a function that accepts a list of numbers and returns the second smallest element.


# def is_panagram(s):
#     return set('abcdefghijklmnopqrstuvwxyz').issubset(s.lower())

# print(is_panagram('I love programming in Python'))
# print(is_panagram('The quick brown fox jumps over the lazy dog'))
# print(is_panagram('pack my box with five dozen liquor jugs'))


# def intersection(lst1,lst2):
#     return set(lst1) & set(lst2)
#     # return list(set(lst1) & set(lst2))

# print(intersection([1,2,3,4,5],[3,4,5,6,7]))




# def largest(a):
#     return max(a.split())

# print(largest('I love programming in Python'))



# def largest(a):
#     return max(a.split(),key = len)

# print(largest('I love programming in Python'))



# a = 'I lo pro iryn Python'
# y = a.split()
# print(y)
# print(max(y,key = len))

# a = 'I love programming in Python'
# for i in a:
#     print(f'{i}: {a.count(i)}')



# a = 'I love programming in Python'
# for i in set(a):
#     print(f'{i}: {a.count(i)}')



# a = 'I love programming in Python'

# a = 'I love programming in Python'.lower()

# # for i in dict.fromkeys(a):
# #     print(f'{i}: {a.count(i)}')
  

# print({i:a.count(i) for i in set(a)})  


# def sumofdigits(n):

#     # n = 1346
#     sum = 0
#     while n > 0:
#         d = n%10
#         sum += d
#         n //= 10
#     return sum

# print(sumofdigits(123678))  



# def recursivesum(n):
#     if n == 0:
#         return 0
#     else:
#         return n%10 + recursivesum(n//10)


# print(recursivesum(547))



# def countlu(a):
#     u = sum(1 for i in a if i.isupper())
#     l = sum(1 for i in a if i.islower())
#     # return u,l
#     # print(f'Count of upper chars is  {u} and lower is {l}')
#     return (f'Count of upper chars is  {u} and lower is {l}')

# print(countlu('Hello World'))


# def ssmallest(lst):
#     a = sorted(set(lst))[-2]
#     # a = set(a)
#     # a = list(a)
#     # a = sorted(lst)
#     return a 
# print(ssmallest([4, 1, 7, 1, 9]))


# def ssmallest(lst):
#     return sorted(set(lst))[-2]

# print(ssmallest([4, 1, 7, 1, 9]))








# Check if two strings are rotations of each other.

# Remove all whitespace from a string without using .replace().

# Count the frequency of each vowel in a given string.

# Find the most common character in a string.

# Capitalize the first letter of every word in a sentence without using .title().

# Reverse the order of words in a string.

# Check if a string contains only unique characters.

# Replace multiple spaces with a single space.

# Remove all duplicate characters from a string while keeping the first occurrence.

# Check if a given substring occurs in a string without using in.




# a = 'abs'
# b = 'sab'
# if len(a) == len(b) and b in (a+a):
#     print('It\'s rotatable')
# else:
#     print('It\'s not rotatable')    


# def rotation(a,b):
#     return len(a) == len(b) and b in a+a

# print(rotation('bds','sbd'))


# def whitespaces(s):
#     s = s.split()
#     # return s.split()
#     return ''.join(s)

# print(whitespaces("hello   world"))



# s = "hello   world"
# s = s.replace(' ','')
# print(s)
# print(s.strip())



# a = 'Hello World'
# a = a.lower()
# for i in set(a):
#     if i in 'aeiou':
#         print(f'{i}:{a.count(i)}')


# def vowelfreq(a):
#     a = a.lower()
#     for i in set(a):
#         if i in 'aeiou':
#             return ({i: a.count(i)})
#     # return ({i: a.lower().count(i) for i in 'aeiou'})    
        
# print(vowelfreq('Hello World'))        




# s = "mississippii"
# print(max(s,key=s.count))
# print(max(set(s),key = s.count))



# s = "hello world"
# # print(s.title())
# print(' '.join(i.capitalize() for i in s.split()))


# s = "python is fun"
# # s = s.split()
# # s = s.reverse()
# print(s)
# # print(reversed(s.split()))
# # print(reversed(s))
# print(' '.join(reversed(s.split())))


# s = "abcdef"
# print(len(s) == len(set(s)))



# s = "banana"
# new = ''
# for i in s:
#     if i not in new:
#         new = i + new
# print(new)        



# s = "hello world"
# sub = "world"
# if sub in s:
#     print('True')
# else:
#     print('False')    


s = "hello world"
sub = "world"
for i in s.split():
    print(i)






# Find all numbers in a list that occur more than once.

# Remove all falsy values (None, False, 0, '') from a list.

# Create a list of squares for numbers 1 to 20 using list comprehension.

# Flatten a list of lists using list comprehension.

# Find the longest tuple in a list of tuples.

# Create a dictionary from two lists (keys and values).

# Merge two lists into a dictionary where values from the second list are squared.

# Find the key with the smallest value in a dictionary.

# Create a dictionary where keys are numbers from 1 to 10 and values are their cubes.

# Given two sets, find symmetric difference without using ^ operator.



lst = [1, 2, 2, 3, 4, 4, 5]
for i in set(lst):
    if lst.count(i) > 1:
        print(i)






























