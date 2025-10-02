

import random
import string

# import requests

# a = requests.get('https://www.google.com')
# print(a.text)




# b = requests.get('https://jsonplaceholder.typicode.com/todos/1')
# print(b.text)

 







# Write a python program to translate a message into secret code 
# language. Use the rules below to translate normal English into 
# secret code language

# Coding:

# if the word contains atleast 3 characters, remove the first 
# letter and append it at the end now append three random 
# characters at the starting and the end else: simply reverse 
# the string


# Decoding:

# if the word contains less than 3 characters, reverse it else: 
# remove 3 random characters from start and end. Now remove 
# the last letter and append it to the beginning


# Your program should ask whether you want to code or decode




# words = input("Enter the word: ").split(' ')
# for word in words:
#     if len(word) >= 3:
#         coded = 'xyz' + word[1:] + word[0] + 'abc'
#         print(f'The coded word is: {coded}')
#     else:
#         coded = word[::-1]
#         print(f'The coded word is: {coded}')    




'''
coding = False
if(coding):
    words = input("Enter the word: ").split(' ')
    for word in words:
        if len(word) >= 3:
            coded = 'xyz' + word[1:] + word[0] + 'abc'
            print(f'The coded word is: {coded}')
        else:
            coded = word[::-1]
            print(f'The coded word is: {coded}')
else:
    words = input("Enter the coded word: ").split(' ')
    for word in words:
        if len(word) >= 3:
            decoded = word[3:-3]
            decoded = decoded[-1] + decoded[:-1]
            print(f'The decoded word is: {decoded}')
        else:
            decoded = word[::-1]
            print(f'The decoded word is: {decoded}')            
'''


"""
'''Better way'''

# letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
letter = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
a = ''.join(random.choice(letter) for i in range(3))
b = ''.join(random.choice(letter) for i in range(3))
# print(a)
# print(a,b)

msg = input("Enter the message: ").split(' ')
coding = input("Do you want to code or decode (c/d): ")
if coding == 'c':
    new = []
    for word in msg:
        if len(word) >= 3:
            coded = a + word[1:] + word[0] + b
            new.append(coded)
            # print(f'The coded word is: {coded}')
        else:
            new.append(word[::-1])
            # coded = word[::-1]
            # print(f'The coded word is: {coded}')
    print(' '.join(new))        

elif coding == 'd':
    new = []
    for word in msg:
        if len(word) >= 3:
            decoded = word[3:-3]
            decoded = decoded[-1] + decoded[:-1]
            new.append(decoded)
            # print(f'The decoded word is: {decoded}')
        else:
            new.append(word[::-1])
            # decoded = word[::-1]
            # print(f'The decoded word is: {decoded}')
    print(' '.join(new))        

else:
    print("Invalid input")            


"""


# Snake Water Gun

# Snake, Water and Gun is a variation of the children's game 
# "rock-paper-scissors" where players use hand gestures to 
# represent a snake, water, or a gun. The gun beats the snake, 
# the water beats the gun, and the snake beats the water. 
# Write a python program to create a Snake Water Gun game in 
# Python using if-else statements. Do not create any fancy GUI. 
# Use proper functions to check for win.




'''
a = ['snake', 'water', 'gun']
b = random.choice(a)
# print(b)
user = input("Enter your choice (snake/water/gun): ").lower()
if user == b:
    print(f'Both selected {user}. It is a tie')
elif user == 'snake' and b == 'water':
    print(f'User selected {user} and computer selected {b}. User wins')
elif user == 'water' and b == 'gun':
    print(f'User selected {user} and computer selected {b}. User wins')
elif user == 'gun' and b == 'snake':
    print(f'User selected {user} and computer selected {b}. User wins')
elif user == 'snake' and b == 'gun':
    print(f'User selected {user} and computer selected {b}. Computer wins')
elif user == 'water' and b == 'snake':
    print(f'User selected {user} and computer selected {b}. Computer wins')
elif user == 'gun' and b == 'water':
    print(f'User selected {user} and computer selected {b}. Computer wins')
else:
    print("Invalid input")                            

'''



# '''Better way'''

# user = int(input("Enter your choice (0-Snake, 1-Water, 2-Gun): "))
# comp = random.randint(0, 2)

# if user == comp:
#     print(f'Both selected {user}. It is a tie')
# elif (user == 0 and comp == 1) or (user == 1 and comp == 2) or (user == 2 and comp == 0):
#     print(f'User selected {user} and computer selected {comp}. User wins')
# elif (user == 0 and comp == 2) or (user == 1 and comp == 0) or (user == 2 and comp == 1):
#     print(f'User selected {user} and computer selected {comp}. Computer wins')
# else:
#     print("Invalid input")            


"""
comp = random.randint(0, 2)
user = int(input("Enter your choice (0-Snake, 1-Water, 2-Gun): "))

def game(user, comp):
    if user == comp:
        return 0
    elif (user == 0 and comp == 1) or (user == 1 and comp == 2) or (user == 2 and comp == 0):
        return 1
    elif (user == 0 and comp == 2) or (user == 1 and comp == 0) or (user == 2 and comp == 1):
        return -1
    else:
        return None

# a = game(user, comp)
# if a == 0:
#     print(f'Both selected {user}. It is a tie')
# elif a == 1:
#     print(f'User selected {user} and computer selected {comp}. User wins')
# elif a == -1:
#     print(f'User selected {user} and computer selected {comp}. Computer wins')
# else:
#     print("Invalid input")            

print(f'Computer selected {comp}')
print(f'User selected {user}')

a = game(user, comp)
if a == 0:
    print("It's a tie")
elif a == 1:
    print("You win")
elif a == -1:
    print("Computer wins")
else:
    print("Invalid input")        

"""




# Write a Library class with no_of_books and books as two 
# instance variables. Write a program to create a library from 
# this Library class and show how you can print all books, add 
# a book and get the number of books using different methods. 
# Show that your program doesnt persist the books after the 
# program is stopped!


"""

class Library:

    def __init__(self):
        self.books = []
        self.no_of_books = 0

    def add_book(self,nbook):
        self.books.append(nbook)
        self.no_of_books += 1
        print(f'Book "{nbook}" added to the library.')


    def print_books(self):       
        if self.no_of_books == 0:
            print("No books in the library.")
        else:
            print("Books in the library:")
            for book in self.books:
                print(f'- {book}')

    def get_no_of_books(self):
        return self.no_of_books


a = Library()
a.add_book('Python Basics')
# a.add_book('Learn Java')
a.print_books()
print(f'Total number of books: {a.get_no_of_books()}')

"""










# class Library:
#     def __init__(self):
#         self.books = []
#         self.no_of_books = 0

#     def add_book(self, book_name):
#         self.books.append(book_name)
#         self.no_of_books += 1
#         print(f'Book "{book_name}" added to the library.')

#     def print_books(self):
#         if self.no_of_books == 0:
#             print("No books in the library.")
#         else:
#             print("Books in the library:")
#             for book in self.books:
#                 print(f'- {book}')

#     def get_no_of_books(self):
#         return self.no_of_books








































