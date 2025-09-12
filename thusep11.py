


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


# lst = [1, 2, 2, 3, 4, 4, 5]
# # lst = [1, 2, 2, 3, 4, 4, 5]
# # for i in set(lst):
# #     if lst.count(i) > 1:
# #         print(i)
# print([i for i in set(lst) if lst.count(i) > 1])


# lst = [0, None, False, 1, "", 2]
# print([i for i in lst if i not in (False,'',None)])




# # for i in range(1,21):
# print([x**2 for x in range(1,21)])


# nested = [[1, 2], [3, 4]]
# print([j for i in nested for j in i])


# tuples = [(1, 2), (1, 2, 3), (4,)]
# print(max(tuples,key = len))



# keys = ["a", "b"]
# vals = [1, 2]
# print(dict(zip(keys,vals)))



# keys = [1, 2]
# vals = [3, 4]
# # vals = [val**2 for val in vals]
# # print(dict(zip(keys,vals)))
# # for k ,v in zip(keys,vals):
# #     print({k,v})


# print({k : v**2 for k ,v in zip(keys,vals)})


# keys = [1, 2]
# vals = [3, 4]
# print({k: v**2 for k, v in zip(keys, vals)})


# d = {"a": 10, "b": 5, "c": 7}
# print(min(d,key = d.get))



# for i in range(1,11):
#     print(i,i**3)


# print({x: x**3 for x in range(1,11)})



# set1, set2 = {1, 2, 3}, {3, 4, 5}
# print(set1 - set2)
# print(set1 - set2 , set2 - set1)
# print((set1 - set2) | (set2 - set1))




# Implement a stack using a list and add push, pop, and peek operations.

# Implement a queue using deque.

# Find the first recurring element in a list.

# Use a dictionary to group words by their first letter.

# Write a program to find all pairs of integers in a list whose sum is equal to a target (without repeating pairs).

# Sort a list of dictionaries by a specific key.

# Implement binary search recursively.

# Find the missing number in a list from 1 to n without using sum formula.

# Rotate a list to the left by k steps.

# Check if a given list is a palindrome.


# stack = []
# stack.append(5)
# stack.append(7)
# print(stack)
# stack.pop()
# print(stack)


# queue = []
# -----------------------------------------
 

# lst = [1, 2, 3, 2, 5,4,5,6,6]
# for i in set(lst):
#     if lst.count(i) > 1:
#         print(i)
#         break



# words = ["apple", "bat", "ball", "cat"]
# ----------------------------------------


# lst = [1, 2, 3, 4, 5]
# target = 6
# p = []
# for i in range(len(lst)):
#     for j in range(i+1,len(lst)):
#         if lst[i]+lst[j] == target:
#             p.append((lst[i],lst[j]))
#             print({i,j})
# print(p)



# data = [{"name": "John", "age": 25}, {"name": "Jane", "age": 20}]
# print(dict(data))
# print(sorted(data,key = lambda x : x['age']))



# def binary_search(arr, target, low, high):
#     if low > high:
#         return -1
#     mid = (low + high) // 2
#     if arr[mid] == target:
#         return mid
#     elif arr[mid] < target:
#         return binary_search(arr, target, mid+1, high)
#     else:
#         return binary_search(arr, target, low, mid-1)
# print(binary_search([1, 2, 3, 4, 5], 3, 0, 4))
# --------------------------------------------------



# lst = [1, 2, 4, 5]
# n = len(lst)
# a = 0
# for i in lst:
#     a += i
# print(int(((n+1)*(n+2))/2) - a)    



# lst = [1, 2, 4, 5]
# n = len(lst) + 1
# for i in range(1,n):
#     if i not in lst:
#         print(i)
#         break


# lst = [1, 2, 3, 4, 5]
# k = 2
# print(lst[k:] + lst[:k])


# lst = [1, 2, 3, 2, 1]
# if lst == lst[::-1]:
#     print('Palindrome')







# Write a program to calculate compound interest.

# Find the greatest common divisor (GCD) and least common multiple (LCM) of two numbers without using math library.

# Convert a decimal number to binary, octal, and hexadecimal.

# Swap two numbers using XOR.

# Count how many times a digit appears in a number.

# Generate Pascal’s Triangle up to N rows.

# Print all prime numbers in a given range.

# Check if a number is an Armstrong number (narcissistic number).

# Find all divisors of a number.

# Print all perfect numbers less than 1000.



# n = 23
# print(bin(n))
# print(oct(n))
# print(hex(n))


# n = 1223334444
# d = 3
# # for i in str(n):
# print(str(n).count(str(d)))



# a = 5
# b = 10
 
# by using xor we can do swap numbers

# a ^= b 
# print(a, b)
# b ^= a
# print(a, b)
# a ^= b 
# # a ^= b; b ^= a; a ^= b
# print(a, b)

# a ^= b; b ^= a; a ^= b
# print(a, b)



# n = 5
# for i in range(n):
#     num = 1
#     for j in range(i+1):
#         print(num, end=" ")
#         num = num * (i-j) // (j+1)
#     print()
# -------------------------------------------------------


# n = 153
# s = sum(int(i) ** len(str(n)) for i in str(n))
# if n == s:
#     print('Amstrong')
# else:
#     print('Not')

# # print("Amstrong" if n == s else 'Not')



n = 28
print([i for i in range(1,n) if n%i == 0])


# for n in range(2, 1000):
#     if sum(i for i in range(1, n) if n % i == 0) == n:
#         print(n)







# Write a recursive function to calculate the nth Fibonacci number.

# Write a recursive function for binary search.

# Write a recursive function to check if a string is a palindrome.

# Write a recursive function to calculate sum of elements in a list.

# Write a recursive function to generate all subsets of a set.

# Find the first non-repeated character in a string.

# Check if a string is a valid palindrome (ignoring spaces, punctuation, and case).

# Implement your own version of startswith() and endswith().

# Check if one string is a subsequence of another.

# Find the longest palindrome substring in a string.





# s = "aabbcde"
# for i in s:
#     if s.count(i) == 1:
#         print(i)
#         break

# s = "A man, a plan, a canal: Panama"

# s = s.lower().replace(' ','').replace(',','').replace(':','')
# print('Palin' if s == s[::-1] else 'No')


# s = "A man, a plan, a canal: Panama"
# s =s.lower()
# ss = ''
# for i in s:
#     if i.isalpha():
#         ss += i
# print(ss)        
# print(ss ,'Palindrome' if ss == ss[::-1] else 'Not')




def longest_pal(s):
    res=""
    for i in range(len(s)):
        for j in range(i,len(s)):
            sub=s[i:j+1]
            if sub==sub[::-1] and len(sub)>len(res):
                res=sub
    return res
print(longest_pal("babad"))







































