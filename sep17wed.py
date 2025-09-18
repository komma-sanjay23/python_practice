




# import os
# # print(dir(os))

# print(os.getcwd())



# if "__name__ == "__main__" in Python
# The if __name__ == "__main__" idiom is a common pattern 
# used in Python scripts to determine whether the script is 
# being run directly or being imported as a module into 
# another script.

# In Python, the __name__ variable is a built-in variable 
# that is automatically set to the name of the current module. 
# When a Python script is run directly, the __name__ variable 
# is set to the string __main__ When the script is imported 
# as a module into another script, the __name__ variable is 
# set to the name of the module.

# Here's an example of how the if __name__ == __main__ 
# idiom can be used:


# def main():
#     print("Running script directly")

# if __name__ == "__main__":
#     main()


# In this example, the main function contains the code 
# that should be run when the script is run directly. 
# The if statement at the bottom checks whether 
# the __name__ variable is equal to __main__. 
# If it is, the main function is called.


# main()
# print(main())


# This idiom is useful because it allows you to reuse 
# code from a script by importing it as a module into 
# another script, without running the code in the 
# original script. For example, consider the following script:



# def main():
#     print("Running script directly")
# if __name__ == "__main__":
#     main()


# If you run this script directly, it will output 
# "Running script directly". However, if you import it 
# as a module into another script and call the main function 
# from the imported module, it will not output anything:

# import mymath
# mymath.main()


# It's important to note that the if __name__ == "__main__" 
# idiom is not required to run a Python script. You can 
# still run a script without it by simply calling the 
# functions or running the code you want to execute directly. 
# However, the if __name__ == "__main__" idiom can be a useful 
# tool for organizing and separating code that should be run 
# directly from code that should be imported and used as a 
# module.


# In summary, the if __name__ == "__main__" idiom is a common 
# pattern used in Python scripts to determine whether the 
# script is being run directly or being imported as a module 
# into another script. It allows you to reuse code from a 
# script by importing it as a module into another script, 
# without running the code in the original script.


# def greet():
#     print("Hello from function!")

# if __name__ == "__main__":
#     greet()



# import mymath as m 
# # m.greet()


# # print(m.add(3,4))

# # print(m.add(5,4))

# m.hello()



# import mymath as m

# print(f"Add: {m.add(2,4)}")
# print(f"Sub: {m.sub(6,3)}")



# import sys
# def main():
#     if len(sys.argv) < 3:
#         print("Usage: python script.py num1 num2")
#         return
#     n1, n2 = int(sys.argv[1]), int(sys.argv[2])
#     print("Sum =", n1 + n2)

# if __name__ == "__main__":
#     main()
# # --------------------------------------------------


# def multiply(a, b): 
#     return a * b

# if __name__ == "__main__":
#     assert multiply(2, 3) == 6
#     assert multiply(5, 0) == 0
#     # assert multiply(9, 5) == 45
#     print("All tests passed!")
# # else:
# #     print('NOT')



# import mymath as m
# print(m.square(3))



# import time


# # def timer(s):
# #     print(f"Waiting {s} seconds...")
# #     time.sleep(s)
# #     print("Done!")

# # if __name__ == "__main__":
# #     timer(5)




# def timer(s):
#     print(f"Waiting {s} seconds...")
#     time.sleep(1)

# timer(5)

# # print(dir(time))



# def divide(a, b): 
#     return a / b

# if __name__ == "__main__":
#     try:
#         print(divide(10, 2))  
#         print(divide(10, 0))  
#     except ZeroDivisionError:
#         print("Handled ZeroDivisionError")




# os Module in Python---------------------------

# The os module in Python is a built-in library that provides 
# functions for interacting with the operating system. 
# It allows you to perform a wide variety of tasks, 
# such as reading and writing files, interacting with the 
# file system, and running system commands.

# Here are some common tasks you can perform with 
# the os module:

# Reading and writing files The os module provides 
# functions for opening, reading, and writing files. 
# For example, to open a file for reading, you can use 
# the open function:



# import os
# # Open the file in read-only mode
# f = os.open("myfile.txt", os.O_RDONLY)
# # Read the contents of the file
# contents = os.read(f, 1024)
# # Close the file
# os.close(f)
# ---------------------------------------------------



# # To open a file for writing, you can use the os.O_WRONLY flag:

# import os
# # Open the file in write-only mode
# f = os.open("myfile.txt", os.O_WRONLY)
# # Write to the file
# os.write(f, b"Hello, world!")
# # Close the file
# os.close(f)
# --------------------------------------------------------



# Interacting with the file system
# The os module also provides functions for interacting
# with the file system. For example, you can use the 
# os.listdir function to get a list of the files in 
# a directory:



# import os

# # Get a list of the files in the current directory
# # files = os.listdir()
# # print(files)  # Output: ['myfile.txt', 'otherfile.txt']

# # print(dir(os))


# print(os.listdir())


# You can also use the os.mkdir function to create 
# a new directory:

# import os
# # Create a new directory
# # os.mkdir("newdir")

# os.rmdir("newdir")


# Running system commands
# Finally, the os module provides functions for running 
# system commands. For example, you can use the os.system 
# function to run a command and get the output:


# import os

# # Run the "ls" command and print the output
# output = os.system("ls")
# print(output)  # Output: ['myfile.txt', 'otherfile.txt']
# --------------------------------------------------


# import os

# f = os.popen("ls")

# output = f.read()
# print(output)  

# f.close()
# ----------------------------------------------


# In summary, the os module in Python is a built-in library 
# that provides a wide variety of functions for interacting
# with the operating system. It allows you to perform tasks 
# such as reading and writing files, interacting with the 
# file system, and running system commands.


# import os
# # print(os.getcwd())


# os.chdir('C:/Users/komma')
# print(os.getcwd())



# import os
# print(os.listdir())


# print(os.listdir('.'))


# import os 
# # os.mkdir('sanjay')
# # print("folder created")

# os.rmdir('sanjay')
# print('folder deleted')



# import os
# # os.makedirs('sanjay/sanjay1/sanjay2')
# # print('created')

# os.removedirs('sanjay/sanjay1/sanjay2')
# print('deleted')



# import os
# # with open("old.txt", "w") as f:
# #     f.write("hello")

# # os.rename('old.txt','new.txt')


# os.remove('old.txt')


# import os
# print(os.path.isfile("new.txt"))
# print(os.path.isdir("."))


# import os
# for root, dirs, files in os.walk("."):
#     print("Root:", root)
#     print("Dirs:", dirs)
#     print("Files:", files)
#     break  # just first level

# # print(dir(os))


# import os
# print(os.path.abspath("new.txt"))
# print(os.path.abspath("next.py"))

# # print(os.listdir())


# # import os
# # with open('new.txt','w') as f:
# #     f.write('hi')

# if os.path.exists("new.txt"):
#     os.remove("new.txt")
#     print("Deleted")


# import os
# print(os.environ.get("PATH"))



# import os
# print(os.environ.get("PATH"))


# import os
# os.environ["MY_VAR"] = "HelloWorld"
# print(os.environ["MY_VAR"])



# import os
# folder = "C:/Users"
# file = "notes.txt"
# print(os.path.join(folder, file))



# import os
# path = "C:/Users/komma/data.txt"
# print(os.path.split(path))      # ('C:/Users/komma', 'data.txt')
# print(os.path.splitext(path))   # ('C:/Users/komma/data', '.txt')



# import os
# with open("size_test.txt", "w") as f:
#     f.write("12345")
# print(os.path.getsize("size_test.txt"))



# import os
# print(os.access("size_test.txt", os.R_OK))  # Readable?
# print(os.access("size_test.txt", os.W_OK))  # Writable?
# print(os.access("size_test.txt", os.X_OK))  # Executable?




# import os
# # os.system("cp size_test.txt copy_test.txt")
# os.system("copy size_test.txt copy_test.txt")



# import os
# stream = os.popen("echo Hello from Shell")
# output = stream.read()
# print(output)



# import os
# print("Process ID:", os.getpid())



import os
# pid = os.fork()
# if pid == 0:
#     print("Child process")
# else:
#     print("Parent process")



# os.remove('copy_test.txt')

print(dir(os))
















