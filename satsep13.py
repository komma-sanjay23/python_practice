

# numbers = lambda a, b, c : a+b+c
# print(numbers(1,2,4)) 




# lst = [1,2,3,4,5]
# # for i in lst:
# a = list(map(lambda i : i**2,lst))
# print(a)



# lst = [1,2,3,4,5]
# a = list(filter(lambda i : i%2 == 0,lst))
# print(a)


# nums = [4, 7, -2, 8, -9]
# for i, num in enumerate(nums,start = 1):
#     print(f'{i}: {num}')


# nums = [4, 7, -2, 8, -9]
# for i, num in enumerate(nums):
#     if num < 0:
#         print(i)
#         break


# names = ["Alice", "Bob", "Charlie"]
# for i,name in enumerate(names,start = 1):
#     print(f'{i}: {name}')


# def fact(n):
#     return 1 if n == 0 else n * fact(n-1)

# print(fact(5)) 



# def fib(n):
#     return n if n <= 1 else fib(n-2) + fib(n-1)

# print(fib(7))

# print([fib(i) for i in range(3)])



# try:
#     num = 10 / 0
# except ZeroDivisionError:
#     print("You cannot divide by zero!")




try:
    x = int("abc")
    y = 10 / 0
except ValueError:
    print("Invalid conversion!")
except ZeroDivisionError:
    print("Cannot divide by zero!")








































