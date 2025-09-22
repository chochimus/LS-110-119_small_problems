"""
Problem: 
    Write another function that returns True if the string passed as an argument is a palindrome, or False otherwise. 
    This time, however, your function should be case-insensitive, and should ignore all non-alphanumeric characters. 
    If you wish, you may simplify things by calling the is_palindrome function you wrote in the previous exercise.

input: string

output: boolean that determines whether or not input string is a palindrome

rules:
    explicit:
        - case doesn't matter in determining palindrome
        - ignore non-alphanumeric characters
    implicit:
    

questions:


data-struct:

string

alg:

1. remove non-alphanumeric chars
2. casefold
3. input == reversed_string
    
"""

def is_real_palindrome(input_string):
    test_str = ""
    for char in input_string:
        if char.isalnum():
            test_str += char.casefold()
    return test_str == test_str[::-1]

print(is_real_palindrome('madam') == True)           # True
print(is_real_palindrome('356653') == True)          # True
print(is_real_palindrome('356635') == False)         # True
print(is_real_palindrome('356a653') == True)         # True
print(is_real_palindrome('123ab321') == False)       # True

# case doesn't matter
print(is_real_palindrome('Madam') == True)           # True

# only alphanumerics matter
print(is_real_palindrome("Madam, I'm Adam") == True) # True