"""
Problem:
Write a function that takes a string, doubles every character in the string, then returns the result as a new string.

input: string
output: string with every character doubled

rules:
    explicit:
    - all characters count
    implicit:
    - empty string should return empty string

datastructure:
text sequence

algorithm:
1.) create empty string answer
2.) add 2 of current char to answer
3.) repeat for every character

"""

def repeater(string):
    answer = ""
    for char in string:
        answer += char * 2
    return answer

print(repeater('Hello') == "HHeelllloo")              # True
print(repeater('Good job!') == "GGoooodd  jjoobb!!")  # True
print(repeater('') == "")                             # True