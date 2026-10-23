# largest of three numbers

def largest():
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    z = int(input("Enter third number: "))
    
    if x >= y and x >= z:
        print(x)
    elif y >= x and y >= z:
        print(y)
    else:
        print(z)

largest()

# number is even

def even_odd():
    a = 10
    if a%2 == 0:
        print("even")
    else:
        print("odd")

even_odd()

# greet good morning

def greet():
    name = "Rishabh"
    print(f"Good Morning {name}!")

greet()

# square of a number

def square(n):
    res = n*n
    print(f"the square of {n} is {res}")

square(5)

