"""
Problem: 
    Write a function that returns True if the string passed as an argument is a palindrome, False otherwise.
    A palindrome reads the same forwards and backwards. For this problem, the case matters and all characters matter.

input: string

output: boolean that determines whether or not input string is a palindrome

rules:
    explicit:
        - case matters in determining palindrome
        - all characters matter
    implicit:
    

questions:

should empty string case be handled?

data-struct:

string

alg:

1. return string == reversed(string)
    
"""

def is_palindrome(input_string):
    return input_string == input_string[::-1]

print(is_palindrome('madam') == True)
print(is_palindrome('356653') == True)
print(is_palindrome('356635') == False)

# case matters
print(is_palindrome('Madam') == False)

# all characters matter
print(is_palindrome("madam i'm adam") == False)
