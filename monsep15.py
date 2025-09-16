






# Exception Handling
# Exception handling is the process of responding to unwanted or 
# unexpected events when a computer program runs. 
# Exception handling deals with these events to avoid the program 
# or system crashing, and without this process, exceptions would 
# disrupt the normal operation of a program.


# Exceptions in Python
# Python has many built-in exceptions that are raised when your 
# program encounters an error (something in the program goes wrong).

# When these exceptions occur, the Python interpreter stops the 
# current process and passes it to the calling process until it 
# is handled. If not handled, the program will crash.



# Finally Clause
# The finally code block is also a part of exception handling. 
# When we handle exception using the try and except block,
# we can include a finally block at the end. The finally block 
# is always executed, so it is generally used for doing the 
# concluding tasks like closing file resources or closing 
# database connection or may be ending the program execution 
# with a delightful message.



# try:
#     num = int(input("Enter an integer: "))
# except ValueError:
#     print("Number entered is not an integer.")
# else:
#     print("Integer Accepted.")
# finally:
#     print("This block is always executed.")

# 1. What is an Exception?

# An exception is an error that occurs during program execution, 
# which disrupts the normal flow.
# Examples:

# ZeroDivisionError → dividing by zero.

# FileNotFoundError → trying to open a non-existent file.

# ValueError → invalid data type conversion.

# Without handling, Python will stop execution and print a traceback.


# # 2. Basic Exception Handling (try / except)
# try:
#     x = 10 / 0
# except ZeroDivisionError:
#     print("Error: Division by zero is not allowed.")


# # Program doesn’t crash, instead it prints the error message.



# # 3. Handling Multiple Exceptions
# try:
#     num = int("abc")
#     result = 10 / num
# except ValueError:
#     print("Error: Invalid conversion to integer.")
# except ZeroDivisionError:
#     print("Error: Cannot divide by zero.")

# # You can catch different exceptions separately.


# # 4. Catching All Exceptions (Generic)
# try:
#     a = [1, 2, 3]
#     print(a[5])
# except Exception as e:
#     print("Error occurred:", e)

# try:
#     a = [1, 2, 3]
#     print(a[ab])
# except Exception as e:
#     print("Error occurred:", e)


# #  Exception as e captures the error message.

# #  Best practice: Don’t overuse generic Exception — use specific 
# # ones where possible.




# # 5. else Block

# # Runs if no exception occurs.

# try:
#     num = int("100")
# except ValueError:
#     print("Conversion failed.")
# else:
#     print("Conversion successful:", num)


# try:
#     num = int("100a")
# except ValueError:
#     print("Conversion failed.")
# else:
#     print("Conversion successful:", num)



# # 6. finally Block

# # Always executes (cleanup code).

# try:
#     file = open("data.txt", "r")
#     content = file.read()
# except FileNotFoundError:
#     print("File not found.")
# finally:
#     print("Closing file (if opened).")
#     try:
#         file.close()
#     except:
#         pass

# # Used for closing files, releasing resources, disconnecting DBs.



# # 7. Raising Exceptions (raise)

# # Manually trigger exceptions.

# def withdraw(balance, amount):
#     if amount > balance:
#         raise ValueError("Insufficient funds")
#     return balance - amount

# try:
#     withdraw(100, 200)
# except ValueError as e:
#     print("Transaction failed:", e)


# # 8. Custom Exceptions

# # Define your own exception class (inherit from Exception).

# class NegativeNumberError(Exception):
#     pass

# def square_root(x):
#     if x < 0:
#         raise NegativeNumberError("Cannot compute square root of negative number")
#     return x ** 0.5

# try:
#     print(square_root(-9))
# except NegativeNumberError as e:
#     print("Custom Exception:", e)




# # In python, we can raise custom errors by using the raise keyword.

# salary = int(input("Enter salary amount: "))
# if not 2000 < salary < 5000:
#     raise ValueError("Not a valid salary")


# we learned about different built-in exceptions in Python and 
# why it is important to handle exceptions. However, 
# sometimes we may need to create our own custom exceptions
# that serve our purpose.





questions = [
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ]
]

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]
money = 0
for i in range(0, len(questions)):
  
  question = questions[i]
  print(f"\n\nQuestion for Rs. {levels[i]}")
  print(f"{question[0]}")
  print(f"a. {question[1]}          b. {question[2]} ")
  print(f"c. {question[3]}          d. {question[4]} ")
  reply = int(input("Enter your answer (1-4) or  0 to quit: \n" ))
  if (reply == 0):
    money = levels[i-1]
    break
  if(reply == question[-1]):
    print(f"Correct answer, you have won Rs. {levels[i]}")
    if(i == 4):
      money = 10000
    elif(i == 9):
      money = 320000
    elif(i == 14):
      money = 10000000
  else:
    print("Wrong answer!")
    break 

print(f"Your take home money is {money}")








































