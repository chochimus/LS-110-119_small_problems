"""
Problem:
In the previous exercise, you developed a function that converts simple numeric strings to integers. 
In this exercise, you're going to extend that function to work with signed numbers.

Write a function that takes a string of digits and returns the appropriate number as an integer. 
The string may have a leading + or - sign; if the first character is a +, your function should return a positive number;
 if it is a -, your function should return a negative number. If there is no sign, return a positive number.

You may assume the string will always contain a valid number.

You may not use any of the standard conversion functions available in Python, such as int. 
You may, however, use the string_to_integer function from the previous exercise.

input: signed or unsigned string of digits
output: number as an integer

rules:
    explicit:
    - no use of standard conversion functions such as int
    - may have leading + or - sign
    - no invalid characters 
    implicit:

datastructure

none

algorithm:

1.) get first char
2.) check sign
3.) return string to integer of remaining numbers if there is a sign
4.) add sign to returned value if negative
"""

def string_to_integer(num_string):
    DIGITS = {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9
    }
    answer = 0
    for char in num_string:
        answer = (10 * answer) + DIGITS[char]

    return answer

print(string_to_integer("4321") == 4321)  # True
print(string_to_integer("570") == 570)    # True

def string_to_signed_integer(num_string):
    if num_string[0] == '-':
        return -string_to_integer(num_string[1:])
    elif num_string[0] == '+':
        return string_to_integer(num_string[1:])
    else:
        return string_to_integer(num_string)

print(string_to_signed_integer("4321") == 4321)  # True
print(string_to_signed_integer("-570") == -570)  # True
print(string_to_signed_integer("+100") == 100)   # True