"""
Problem:
Write a function that takes an integer argument and returns a list containing
all integers between 1 and the argument (inclusive), in ascending order.

You may assume that the argument will always be a positive integer.

input: integer
output: list containing all integers between 1 and the argument inclusive in ascending order

rules:
    explicit:
    - integer argument
    - ascending order list
    implicit:
    - no need to worry about empty or non integer input

datastructure:
list

algorithm:
1.) create range from 1 to input + 1
2.) convert range to list
3.) return list
"""

def sequence(num):
    return list(range(1, num + 1))

print(sequence(5) == [1, 2, 3, 4, 5])   # True
print(sequence(3) == [1, 2, 3])         # True
print(sequence(1) == [1])               # True