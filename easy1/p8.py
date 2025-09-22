"""
Problem:
Write a function that takes a string of digits and returns the appropriate number as an integer.
You may not use any of the standard conversion functions available in Python, such as int. 
Your function should calculate the result by using the characters in the string.

For now, do not worry about leading + or - signs, nor should you worry about invalid characters; 
assume all characters are numeric.

input: string of digits
output: number as an integer

rules:
    explicit:
    - no use of standard conversion functions such as int
    - no leading + or - signs
    - no invalid characters 
    implicit:

datastructure

none

algorithm:

1.) get numeric
2.) depending on the place of the value add necessary 0's
3.) total the result
4.) return result
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

def hexadecimal_to_integer(hex_string):
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
        '9': 9,
        'a': 10,
        'b': 11,
        'c': 12,
        'd': 13,
        'e': 14,
        'f': 15
    }
    hex_string = hex_string.lower()
    answer = 0
    for char in hex_string:
        answer = (16 * answer) + DIGITS[char.casefold()]
    
    return answer

print(hexadecimal_to_integer('4D9f') == 19871)  # True