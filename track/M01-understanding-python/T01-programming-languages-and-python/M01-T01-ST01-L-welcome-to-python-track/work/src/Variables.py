name = "Rishabh"
print(name)
age = 22
print(id(name))
print(type(name))

print("Hello Python", end=" ")
print("Thank you Python")

print("Hello Python \nThank you Python")

# my name is Rishabh and age s 22
print("My name is " + name + " age is " + str(age))

# string formatting with f-strings
print(f"My name is {name} and age is {age}")

# single line comment

"""
Multi line comment, it is used for documentation.
"""

a = 10
b = 20
c = 30

# a,b,c = 10,20,30  => This is a better way to declare multiple variables

print(a+b+c)
a, b, c = "Abhi", "Rishabh", "Kumar"
print(b)
print(a + b + c)

x,y,z = 30,4,8
print(x+z) #38
print(a+ str(x)) #Abhi30
print(b+c) #RishabhKumar
print(a, x) #Abhi 30

a = 19
print(type(a),a)