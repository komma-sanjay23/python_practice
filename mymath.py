

def add(a,b):
    return a+b

def minus(a,b):
    return a-b



def count_vowels(s):
    return sum(1 for i in s if i in 'aeiou')



def cube(n):
    return n**3


def upper(s):
    return s.upper() + '!'





def main():
    print("Running script directly")
if __name__ == "__main__":
    main()

# main()



def greet():
    print("Hello from function!")

if __name__ == "__main__":
    greet()




def hello():
    print("Hello from helper!")

print("helper.py __name__ =", __name__)

if __name__ == "__main__":
    print("Running directly")
else:
    print("Imported as module")


# def add(a,b):
#     return a*b

# hello()





def add(a, b): 
    return a + b

def sub(a, b): 
    return a - b

if __name__ == "__main__":
    print("Add:", add(5, 3))
    print("Sub:", sub(5, 3))




def square(n): 
    return n*n

if __name__ == "__main__":
    print("Running as standalone script")
else:
    print("mymath.py imported")

# if __name__ == "__main__":
#     print(square(5))














