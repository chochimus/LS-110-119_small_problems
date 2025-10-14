"""
Problem:
The Fibonacci series is a sequence of numbers in which each number is the sum of 
the previous two numbers. The first two Fibonacci numbers are 1 and 1. 
The third number is 1 + 1 = 2, the fourth is 1 + 2 = 3, the fifth is 2 + 3 = 5, 
the sixth is 3 + 5 = 8, and so on. In mathematical terms, this can be represented as:

F(1) = 1
F(2) = 1
F(n) = F(n - 1) + F(n - 2)    (where n > 2)

Write a function called fibonacci that computes the nth Fibonacci number,
 where nth is an argument passed to the function:

print(fibonacci(1) == 1)                  # True
print(fibonacci(2) == 1)                  # True
print(fibonacci(3) == 2)                  # True
print(fibonacci(4) == 3)                  # True
print(fibonacci(5) == 5)                  # True
print(fibonacci(6) == 8)                  # True
print(fibonacci(12) == 144)               # True
print(fibonacci(20) == 6765)              # True
print(fibonacci(50) == 12586269025)       # True
print(fibonacci(75) == 2111485077978050)  # True

input: number
output: nth digit of fibbonacci

rules:
    explicit:
    - stated in problem
    - must use non-recursive solution
    implicit:
    - don't need to worry about bad input

datastructure:
int

algorithm:
1.) index = range(input)
2.) if input 1 return 1
3.) if input 2 return 1
4.) curr = 2
5.) index -= 1
6.) while index > 0 repeat

"""

def fibonacci(nth):
    if nth < 3:
        return 1
    fib1 = 1
    fib2 = 1
    for _ in range(3,nth + 1):
        fib1, fib2 = fib2, fib1 + fib2
    return fib2

print(fibonacci(1) == 1)                  # True
print(fibonacci(2) == 1)                  # True
print(fibonacci(3) == 2)                  # True
print(fibonacci(4) == 3)                  # True
print(fibonacci(5) == 5)                  # True
print(fibonacci(6) == 8)                  # True
print(fibonacci(12) == 144)               # True
print(fibonacci(20) == 6765)              # True
print(fibonacci(50) == 12586269025)       # True
print(fibonacci(75) == 2111485077978050)  # True


