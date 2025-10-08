"""
Problem:
Write a function that takes a list of strings and returns a list of the same string values, 
but with all vowels (a, e, i, o, u) removed

input: list of strings
output: list of same string values with all vowels removed

rules:
    explicit:
    - remove vowels from strings
    implicit:
    - expect good input
    - account for both cases

datastructure:
list

algorithm:
1.) create empty list answer
2.) get string in list
3.) replace all vowels with empty char
4.) put result in answer
5.) repeat for every string
6.) return answer
"""

def remove_vowels(original):
    answer = []
    for string in original:
        curr = ""
        for char in string:
            if char not in 'AEIOUaeiou':
                curr += char
        answer.append(curr)
    return answer

# All of these examples should print True
original = ['abcdefghijklmnopqrstuvwxyz']
expected = ['bcdfghjklmnpqrstvwxyz']
print(remove_vowels(original) == expected)        # True

original = ['green', 'YELLOW', 'black', 'white']
expected = ['grn', 'YLLW', 'blck', 'wht']
print(remove_vowels(original) == expected)        # True

original = ['ABC', 'AEIOU', 'XYZ']
expected = ['BC', '', 'XYZ']
print(remove_vowels(original) == expected)        # True