# count from 5 to 1

def count(n):
    if n == 0:
        return
    else:
        print(n)
        count(n-1)
count(5)

#count from 1 to 5

def count(n):
    if n <6:
        print(n)
        count(n+1)
count(1)

#factorial number

def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n-1)
print(fact(5))

# sum of numbers

def sum(n):
    if n == 0:
        return 0
    else:
        return n + sum(n-1)
print(sum(5))

#Fibonacci series

def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
print(fib(5))
