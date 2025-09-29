"""
Problem:
Write a function that returns a list of all substrings of a string. 
Order the returned list by where in the string the substring begins. 
This means that all substrings that start at index position 0 should come first, 
then all substrings that start at index position 1, and so on. 
Since multiple substrings will occur at each position, return the substrings at a given index from shortest to longest.

You may (and should) use the leading_substrings function you wrote in the previous exercise:

input: string
output: all substrings

rules:
    explicit:
    - all substrings that start at index position 0 should come first, then 1, and so on
    - should be shortest to longest
    implicit:
    - only good input

datastructure:
list

algorithm:
1.) create empty list answer
2.) call leading_substrings on input string
3.) repeat but pass in string starting from next index
4.) return answer
"""

def leading_substrings(string):
    return [string[:idx + 1] for idx in range(len(string))]

def substrings(string):
    answer = []
    for i in range(len(string)):
        answer.extend(leading_substrings(string[i:]))
    return answer

expected_result = [
    "a", "ab", "abc", "abcd", "abcde",
    "b", "bc", "bcd", "bcde",
    "c", "cd", "cde",
    "d", "de",
    "e",
]

print(substrings('abcde') == expected_result)  # True