"""
Problem:
Write a function that takes a string argument consisting of a first name, a space, and a last name. 
The function should return a new string consisting of the last name, a comma, a space, and the first name.

input: string consisting of first name, space and last name
output: string consisting of last name, comma space and first name

rules:
    explicit:
    - format is given
    - names don't include middle names, initialz, or suffixes
    implicit:
    - no need to handle empty input or bad input

datastructure:
text sequence

algorithmn:
1.) split string on space
2.) using f string make {split[1]}, {split[0]}
"""

def swap_name(full_name):
    return ', '.join(full_name.split()[::-1])

print(swap_name('Joe Roberts') == "Roberts, Joe")   # True