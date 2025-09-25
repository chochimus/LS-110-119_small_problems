"""
Problems:
Write a function that takes one argument, a positive integer, and returns a list of the digits in the number.

input: positive integer
output: list of digits in number

rules:
    explicit:
    - input number is positive non-empty
    implicit:
    - number will be an integer
    - list elements should be in same order as in number

datastructure:
list

algorithm:
1.) create an empty list answer
2.) convert number to string
3.) convert element of string to integer and add it to list
4.) repeat for all elements
5.) return
"""

def digit_list(number):
    return [int(element) for element in str(number)]

print(digit_list(12345) == [1, 2, 3, 4, 5])       # True
print(digit_list(7) == [7])                       # True
print(digit_list(375290) == [3, 7, 5, 2, 9, 0])   # True
print(digit_list(444) == [4, 4, 4])               # True