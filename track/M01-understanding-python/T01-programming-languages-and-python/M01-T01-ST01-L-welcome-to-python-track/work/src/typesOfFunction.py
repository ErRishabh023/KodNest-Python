#1 no input and no output

def square():
    a = 5
    res = a*a
    print(f"the square of {a} is {res}")

square()

#2 no input and output

def square():
    a = 5
    res = a*a
    return res

print(square())

#3 input and no output

def square(a):
    res = a*a
    print(f"the square of {a} is {res}")

square(5)

#4 input and output

def square(a):
    res = a*a
    print(f"the square of {a} is {res}")

square(5)

c = 30 #global variable
def add():
    global a
    a = 10
    b = 20 # local variable
    print(a+b)
    print(c)
add()

x = 100
def display():
    x = 200
    print(x)
display()
print(x)

x = 10
def display():
    x = 20
    print(x)
display()
x = 30
print(x)

# default arguments

def add(a= 0, b=10, c=0):
    return a+b+c
print(add(10))
print(add(10,20))
print(add(1,1,1))
print(add())

# var-args (*args - (0 ...... n) variable number of arguments)

def add(*a):
    #print(a)
    print(sum(a))

add(10,20)
add(10,20,30)
add(10)
add()

# **kwargs (**kwargs - 0....n arguments can be passed)

def stu_info(**kwargs):
    print(f"Name is {kwargs.get('name')}", end = "")
    print(f"Age is {kwargs.get('age')}", end = "")
    print(f"Course is {kwargs.get('course')}")

stu_info(name = "Rishabh", age = 22, course = "Python")