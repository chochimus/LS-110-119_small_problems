"""
Problem:
In the previous two exercises, you developed functions that convert simple numeric strings to signed integers.
In this exercise and the next, you're going to reverse those functions.

Write a function that converts a non-negative integer value (e.g., 0, 1, 2, 3, and so on) to the string 
representation of that integer.

You may not use any of the standard conversion functions available in Python, such as str. 
Your function should do this the old-fashioned way and construct the string by analyzing and manipulating the number.

input: integer number
output: integer as a string

rules:
    explicit:
    - non-negative inputs
    - no standard conversion functions
    implicit:

questions:
- should bad input or empty value be handled?

datastructure:
- character map using dictionary

algorithm:
1.) create an empty string called answer
2.) get the rightmost digit
3.) convert to string
4.) prepend to answer
5.) repeat for all digits
6.) return string
"""

def integer_to_string(number):
    DIGITS = ['0','1','2','3','4','5','6','7','8','9']
    answer = ""
    digit = 0
    while number > 0:
        digit = number % 10
        answer = DIGITS[digit] + answer
        number //= 10
    
    return answer or '0'

print(integer_to_string(4321) == "4321")              # True
print(integer_to_string(0) == "0")                    # True
print(integer_to_string(5000) == "5000")              # True
print(integer_to_string(1234567890) == "1234567890")  # True

