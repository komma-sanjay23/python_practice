

# a = 5
# b = 2
# c = 5*2 + 3
# a += 13-2
# print(a)


# print('abc' == 'a'+'bc')






# Opening a File

# Before we can perform any operations on a file, we must 
# first open it. Python provides the open() function to open 
# a file. It takes two arguments: the name of the file and 
# the mode in which the file should be opened. The mode 
# can be 'r' for reading, 'w' for writing, or 'a' 
# for appending.


# Here's an example of how to open a file for reading:

# with open('myfile.txt', 'w') as f:
#     f.write('hi')


# f = open('myfile.txt', 'w')
# # f.read()
# print(f.write('hello'))


# f = open('myfile.txt', 'w')
# print(f.write('ji'))



# f = open('myfile.txt', 'a')
# f.write('Hello, world!')


# f = open('myfile.txt', 'r')
# # ... do something with the file
# f.close()


# with open("sample.txt", "w") as f:
#     f.write("Hello, Python!\nWelcome to file handling.")


# with open('sample.txt','r') as f:
#     print(f.read())


# with open("sample.txt", "r") as f:
#     for line in f:
#         print(line)
#         # print(line.strip())


# with open("sample.txt", "r") as f:
#     # f.write('\nsanjay')
#     print(f.readlines())


# with open("sample.txt", "r") as f:
#     print(len(f.read().split()))



# Modes in file
# There are various modes in which we can open files.

# read (r): This mode opens the file for reading only and gives 
# an error if the file does not exist. This is the default mode 
# if no mode is passed as a parameter.

# write (w): This mode opens the file for writing only and 
# creates a new file if the file does not exist.

# append (a): This mode opens the file for appending only and 
# creates a new file if the file does not exist.

# create (x): This mode creates a file and gives an error if
# the file already exists.

# text (t): Apart from these modes we also need to specify
# how the file must be handled. t mode is used to handle 
# text files. t refers to the text mode. There is no 
# difference between r and rt or w and wt since text 
# mode is the default. The default mode is 'r' 
# (open for reading text, synonym of 'rt' ).

# binary (b): used to handle binary files (images, pdfs, etc).



# with open("sample.txt", "w") as f:
#     f.write("Hello, Python!\nWelcome to file handling.")


# with open('sample.txt', 'r') as f:
#     print(f.read())



# with open('sample.txt','r') as f:
#     for line in f:
#         print(line)


# with open('sample.txt','r') as f:
#     for line in f:
#         print(line.strip())

# with open('sample.txt','a') as f:
#     f.write('\nSanjay')
# # print(a)    


# with open('sample.txt','r') as f:
#     print(f.readlines())



# with open('sample.txt','r') as f:
#     # a = f.read()
#     print(len(f.read().split()))


# with open('sample.txt','r') as f, open('sample1.txt','w') as f1:
#     f1.write(f.read())


# with open('sample.txt','r') as f:
#     print(max(f,key = len))


# lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
# with open('sample2.txt','w') as f:
#     print(f.writelines(lines))


# try:
#     with open('myfile.txt','r') as f:
#         print(f.read())
# except FileNotFoundError:
#     print('File Not Found')        


# with open('sample.txt','w') as f:
#     for i in range(1,11):
#         f.write(str(i) + '\n')



# with open('sample.txt','r') as f:
#     print(sum([int(i) for i in f]))




# with open('sample1.txt','r') as f:
#     a = f.read()
#     # a = len(f.read())
#     print(f'Lines: {a.count(' ') + 1}')
#     print(f'Words: {len(a.split())}')
#     print(f'Chars: {len(a)}')
# # print(a)
# # print(b)

# with open('myfile.txt','w') as f:
#     print(f.write('hello')) 

# import os 
# if os.path.exists('myfile.txt'):
#     os.remove('myfile.txt')
#     print("Deleted myfile.txt")
# else:
#     print("File does not exist")


# with open('sample1.txt','r') as f:
#     a = f.read()
# # print(a)
# with open('sample1_reverse.txt','w') as f:
#     a = str(a.split())
#     # print(a[::-1])
#     print(f.write(a[::-1]))


# with open('sample1.txt','a') as f:
#     f.write('\n Hello everyone')



# data = [1, 2, 3, 4]
# with open('new.txt','w') as f:
#     a = f.write(str(data))
# # print(a)

# with open('new.txt','r') as f:
#     a = f.read()
# print(type(a),a)


# with open('new.txt','r') as f:
#     a = eval(f.read())
# print(type(a),a)




# Write a program to create a new file hello.txt and write "Hello, Python!" into it.

# Write a program to read the contents of hello.txt and print them.

# Append "Learning file handling" to the same file without overwriting.

# Count the number of words in a text file story.txt.

# Count how many lines are in a text file.



# Write a program to read a text file and display only the lines that contain the word "Python".

# Write a program to copy the contents of story.txt into a new file story_copy.txt.

# Write a program to merge two files file1.txt and file2.txt into a third file merged.txt.

# Read a CSV file data.csv and display each row.

# Write a program to replace all occurrences of "old" with "new" in a file.



# Write a program to read a log file and count how many times the word "ERROR" appears.

# Write a program that reads a JSON file and prints the data in a structured format.

# Write a program to encrypt the contents of a file (Caesar Cipher) and save it into encrypted.txt.

# Write a program to read from a file and remove duplicate lines, then save the result to a new file.

# Write a program to split a large file into smaller files of 100 lines each.



# Create a program that keeps appending student names and grades into a file grades.txt, then read and calculate the class average.

# Write a Python script that logs every time the program is run into a file log.txt with timestamp.

# Write a program that reads config.json (containing settings for an app) and prints them nicely.

# Write a script to scan through a transactions.csv file and print the total sales.

# Write a backup script that copies all .txt files from one folder into a new folder called backup/.





# with open('hello.txt','w') as f:
#     print(f.write('Hello, Python!'))    



# with open('hello.txt','r') as f:
#     print(f.read())


# with open('hello.txt','a') as f:
#     print(f.write("\nLearning file handling"))


# with open('hello.txt','r') as f:
#     print(len(f.read().split()))


# with open('hello.txt','r') as f:
#     a = f.read()
#     print(a.count('\n') + 1)

# with open('hello.txt','r') as f:
#     print(len(f.readlines()))


# with open('hello.txt','r') as f:
#     for i in f:
#         if 'Python' in i:
#             print(i.strip())


# with open('hello.txt','r') as f, open('copy_hello.txt','w') as f1:
#     f1.write(f.read())



# with open('hello.txt','r') as f, open('copy_hello.txt','r') as f1, open('merged.txt','w') as m:
#     print(m.write(f.read() + '\n' + f1.read()))    


# with open('sample1.txt','r') as f:
#     # print(f.read())
#     a = f.read().replace('Python!','Java')
#     print(a)



# with open("sample1.txt", "r") as f:
#     data = f.read().replace("Python", "new")
# with open("sample1.txt", "w") as f:
#     print(f.write(data))
















































