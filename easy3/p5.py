"""
Problem:
Write a function that takes a positive integer as an argument and returns that number with its digits reversed

input: positive integer
output: number with reversed digits

rules:
    explicit:
    - positive integer input only
    implicit:
    - no need to handle 0, negative or empty input

datastructure:
list

algorithm:
1.) convert to string
2.) reverse string
3.) convert to int
"""

def reverse_number(number):
    return int(str(number)[::-1])
print(reverse_number(12345) == 54321)   # True
print(reverse_number(12213) == 31221)   # True
print(reverse_number(456) == 654)       # True
print(reverse_number(1) == 1)           # True
print(reverse_number(12000) == 21)      # True