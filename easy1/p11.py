"""
Problem:
In the previous exercise, you developed a function that converts non-negative numbers to strings. 
In this exercise, you're going to extend that function by adding the ability to represent negative numbers as well.

Write a function that takes an integer and converts it to a string representation.

You may not use any of the standard conversion functions available in Python, such as str. 
You may, however, use integer_to_string from the previous exercise.
input: integer number
output: integer as a string

rules:
    explicit:
    - positive or negative integer inputs
    - no standard conversion functions
    implicit:

questions:
- should bad input or empty value be handled?

datastructure:
- character map using dictionary

algorithm:
1.) determine whether the integer is positive or negative
2.) add sign to answer,
3.) use integer to string function and concatenate the value to the sign
4.) return the result
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

def signed_integer_to_string(number):
    if number > 0:
        return "+" + integer_to_string(number)
    elif number < 0:
        return '-' + integer_to_string(abs(number))
    else:
        return '0'
    
print(signed_integer_to_string(4321) == "+4321")  # True
print(signed_integer_to_string(-123) == "-123")   # True
print(signed_integer_to_string(0) == "0")         # True