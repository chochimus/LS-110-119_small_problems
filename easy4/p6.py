"""
Problem:
Write a function that takes a string argument and returns a list of substrings of that string. 
Each substring should begin with the first letter of the word, and the list should be ordered from shortest to longest.

input: string
ouput: list of substrings

rules:
    explicit:
    - begin with first letter of word
    - shortest to longest
    implicit:
    - only expect good input

datastructure
list

algorithm:
1.) create empty list answer and empty string curr
2.) add character to curr
3.) add curr to answer
4.) repeat for every character
5.) return answer
"""

def leading_substrings(string):
    return [string[:idx + 1] for idx in range(len(string))]

# All of these examples should print True
print(leading_substrings('abc') == ['a', 'ab', 'abc'])
print(leading_substrings('a') == ['a'])
print(leading_substrings('xyzy') == ['x', 'xy', 'xyz', 'xyzy'])