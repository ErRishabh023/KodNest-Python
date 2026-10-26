# Part 1 - if, if-else, if-elif-else

#program 1: chech whether a number is positive.

number = int(input("Enter a number: "))

if number > 0:
    print("The number is positive")

#program 2: Chech if a person is eligible to donate blood(age>=18)

age = int(input("Enter the Age"))

if age >= 18:
    print("Eligible to donate blood")

#program 3: chech if the temperature is above 30 celsius print("hot day")

temperature = int(input("Enter the temperature: "))

if temperature >30:
    print("Hot day")

#program 4: Check whether a student has attended atleast 75% of the classes

classes_attended = int(input("Enter the number of classes attended: "))

if classes_attended >= 75:
    print("The student has attended atleast 75% attendance")


#program 5: check whether a number is even or odd.

number = int(input("Enter a number: "))

if number % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")
    
#program 6: check whether a person in eligible tpo apply for driving license or not.

age = int(input("Enter the age: "))

if age >= 18:
    print("Eligible for driving license")
else:
    print("Not eligible for driving license")

#program 7: check if a year is a leap year

year = int(input("Enter the year: "))

if year % 400 ==0:
    print("Leap year")
elif year % 100 ==0:
    print("Not a leap year")
elif year % 4 ==0: 
    print("Leap year")
else:
    print("Not a leap year")

#program 8: compare two number and print the greatest number.

number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

if number1 > number2:
    print("The greatest number is", number1)
else:
    print("The greatest number is", number2)

#program 9: Assign grades based on marks.

marks = int(input("Enter the marks: "))

if marks >= 90 and marks <=100:
    print("Grade A")
elif marks >= 80 and marks < 90:
    print("Grade B")
elif marks >= 70 and marks < 80:
    print("Grade C")
elif marks >= 60 and marks < 70:
    print("Grade D")
else:
    print("Fail")

#program 10: Categorize electricty consumption as per units.

units = int(input("Enter the units consumed: "))

if units > 500:
    print("High")
elif units >= 301 and units < 500:
    print("Medium")
elif units >= 101 and units <300:
    print("Low")
elif units >= 0 and units < 100:
    print("Very Low")

#program 11: Scholarship eligibility.

marks = int(input("Enter the marks: "))
family_income = int(input("Enter the family income: "))

if marks >= 85 and family_income < 300000:
    print("Eligible for scholarship")
else:
    print("Not eligible for scholarship")

#program 12: user Login.

username = str(input("Enter the username: "))
password = int(input("Enter the password: "))

if username == "kodnest" and password == 123456:
    print("Login successful")
else:
    print("Login failed")

#SWITCH CASE(match case)
#program 13: Display weekday using numbers(1-7).

weekday = int(input("Enter a number between 1 and 7: "))

match weekday:
    case 1:
        print("Sunday")
    case 2:
        print("Monday")
    case 3:
        print("Tuesday")
    case 4:
        print("Wednesday")
    case 5:
        print("Thursday")
    case 6:
        print("Friday")
    case 7:
        print("Saturday")
    case _:
        print("Invalid Day!")


#program 14: Display season based on months.

month_number = int(input("Enter the month number (1-12): "))

match month_number:
    case 12 | 1 | 2:
        print("Winter")
    case 3 | 4 | 5:
        print("Summer")
    case 6 | 7 | 8:
        print("Rainy")
    case 9 | 10 | 11:
        print("Autumn")
    case _:
        print("Invalid month!")

#FOR LOOP
#program 15: print number from 1 to 20.

for i in range(1, 21):
    print(i)

#program 16: print table of a number.

number = int(input("Enter the number: "))

for i in range(1, 11):
    print(number, "*", i, "=", number * i)

#WHILE LOOP
#program 17: print the number from 10 to 1.

count = 10
while count >= 1:
    print(count)
    count = count - 1

#program 18: Find the factorial of number.

factorial = 1
number = int(input("Enter a number: "))

while number > 0:
    factorial = factorial * number
    number = number -1
print("The factorial of the number: ", factorial)

#FOR LOOP
factorial = 1
number = int(input("Enter a number: "))
for i in range(1, number+1):
    factorial = factorial * number
    number = number -1
print("The factorial of the number: ", factorial)

#program 19: print the number from 1 to 20 but stop at 15.

for i in range(1, 21):
    print(i)
    if i == 15:
        break

#program 20:search a number in a list using break.

num = [10,20,30,40,50]
for i in num:
    if i == 40:
        print("Found")   
        break
    print(i)

#program 21:print the number from 1 to 20, skipping multiple of 3.

for i in range(1,21):
    if i % 3 == 0:
        continue
    print(i)

#program 22: print odd number from 1 to 50.

for i in range(1, 50):
    if i % 2 != 0:
        print(i)

#FUNCTIONs
#program 23: find the cube of a number.

def cube(n):
    return n*n*n
print(f"The Cube of the number is: {cube(5)}")

#program 24: Find the maximum of two numbers.

def maximum(a,b):
    if a > b:
        return a
    else:
        return b
print(f"The maximum number is: {maximum(5,6)}")

#Pass Statement
#program 25: create an empty function display().

def display():
    pass
print(display())

#program 26:create an empty class named Student.

class Student:
    pass
print(Student)
