

print(round(3.5))
print(round(2.5))




# a = [1,2,3,4]
# a.append(a)
# b = (1,2,3)
# a.append(b)
# print(a)



# nums = [1, 2, 3, 4, 5]
# target = 6
# # for i,x in enumerate(nums):
# #     if target - x in nums[i+1:]:
# #         print([i, nums.index(target - x, i + 1)])
# #         break


# # print([(x, y) for i, x in enumerate(nums) for y in nums[i+1:] if x+y == target])


# for i,x in enumerate(nums):
#     # for j,y in enumerate(nums[i+1:]):
#     for y in nums[i+1:]:
#         if x + y == target:
#             # print([i, j+i+1])
#             print((x,y))
#             break



# lst = [1, 2, 2, 3, 3, 3, 4]
# print(max(set(lst)))
# print(max(set(lst), key=lst.count))




# arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# max_sum = arr[0]
# curr_sum = arr[0]
# for num in arr[1:]:
#     curr_sum = max(num, curr_sum + num)
#     max_sum = max(max_sum, curr_sum)
# print(max_sum)




# l1 = [2,4,3]
# l2 = [5,6,4]
# # Output: [7,0,8]
# result = []
# for i in range(len(l1)):
#     result.append(l1[i] + l2[i])
# print(result)
# print(list(map(lambda x, y: x + y, l1, l2)))
# print([l1[i] + l2[i] for i in range(len(l1))])
# print([x + y for x, y in zip(l1, l2)])    
# print([sum(i) for i in zip(l1, l2)])
# print([a + b for a, b in zip(l1, l2)])    
# print(list(map(sum, zip(l1, l2))))
# print(list(map(lambda x, y: x + y, l1, l2)))
# print(list(map(lambda x: sum(x), zip(l1, l2))))
# print(list(map(lambda x: x[0] + x[1], zip(l1, l2))))
# print(list(map(lambda x: sum(x), zip(l1, l2))))







# a = 'A'
# print(a)

# print(ord(a))
# print(ord('Z'))
# print(type(ord(a)))
# print(type(a))
# print(ord('a'))




# print(chr(65))
# print(chr(90))
# print(chr(97))
# print(chr(122))
# print(chr(48))
# print(chr(57))  




# print(chr(32))
# print(chr(10))
# print(chr(9))   
# print(chr(8))
# print(chr(13))
# print(chr(127))
# print(chr(255))






# a = 12
# if a%3 == 0 and a%5 == 0:
#     print("Yes it is multiple of both 3 and 5")
# else:
#     print("No it is not multiple of both 3 and 5")



# num = 5
# exp = 3
# result = 1
# for i in range(exp):
#     result *= num
# print(result)




# a = 5
# b = 10
# # temp = a
# temp = a
# a = b
# b = temp    
# print(a,b)


# a = 18
# b = 7

# # print(a % b)
# print(a//b)
# print(a - (a // b) * b)




# sec = 5000
# hr = sec // 3600
# print(hr)
# s = sec % 60
# print(s)





# sec = 3665
# h = sec // 3600
# m = (sec % 3600) // 60
# s = sec % 60
# print(h, "h", m, "m", s, "s")



sec = 47564
h = sec // 3600
m = (sec%3600) // 60
s = sec % 60
print(f"{h}h {m}m {s}s") 




# Take two numbers from user and print their sum, difference, product, and division result.

# Convert kilometers to miles.

# Check if a given number is positive, negative, or zero.

# Find the ASCII value of a character entered by the user.

# Check if a number is a multiple of both 3 and 5.

# Take three float inputs and calculate the average.

# Find the power of a number without using ** operator.

# Swap two variables using a temporary variable.

# Find the remainder without using the % operator.

# Convert seconds into hours, minutes, and seconds.






# Print all odd numbers between 1 and 50.

# Reverse a string without using slicing.

# Find the factorial of a number using a while loop.

# Check if a given year is a leap year.

# Generate the first n prime numbers.

# Print multiplication tables for numbers 1 to 10.

# Count how many even and odd numbers are in a list.

# Check if a number is a palindrome without converting to a string.

# Print a diamond pattern of *.

# Use match-case to check if a number is 1, 2, 3, or something else.



# for i in range(1, 51):
#     if i % 2 == 1:
#         print(i, end=' ')


# # s = "Hello, World!"
# # reversed_s = ''
# # for char in s:
# #     reversed_s = char + reversed_s
# # print(reversed_s)


# s = 'hello'
# rev = ''
# for i in s:
#     rev = i + rev
# print(rev)



# n = 5
# fact = 1
# while n > 0:
#     fact *= n
#     n -= 1
# print(fact)



# y = 2023
# if (y%4 ==0 and y%100 != 0 ) or (y%400 == 0):
#     print(f"{y} is a leap year")
# else:
#     print(f"{y} is not a leap year")




# for j in range(1,11):
#     for i in range(1,11):
#         print(f'{j} x {i} = {j*i}')
#     print()




# lst = [1, 2, 3, 4, 5, 6,7,9,13,35]
# even = sum([1 for i in lst if i%2 == 0])
# odd = sum([1 for i in lst if i%2 != 0])
# print(even,odd)
# # print(odd)



# n = 121
# rev = 0
# while n > 0:
#     # n = n%10
#     rev = (rev * 10) + n%10
#     n = n // 10
# # print(rev)

# if rev == n:
#     print("Palindrome")
# else:
#     print("Not a palindrome")


# n = 121
# original = n
# rev = 0
# while n > 0:
#     nn = n%10
#     rev = (rev * 10) + nn
#     n = n // 10
# print(rev)

# if rev == original:
#     print("Palindrome")
# else:
#     print("Not a palindrome")



# a = set('pack my box with five dozen liquor jugs')
# b = sorted(a)
# print(b)


# aa = set("The quick brown fox jumps over the lazy dog".lower())
# bb = sorted(aa)
# print(bb)



# def is_panagram(s):
#     return set('abcdefghijklmnopqrstuvwxyz').issubset(s.lower())

# print(is_panagram('"The quick brown fox jumps over the lazy dog"'))






def lst(l1,l2):
    return list(set(l1) & set(l2))

print(lst([1,2,2,3,4],[3,4,2,5,6,7]))






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

































