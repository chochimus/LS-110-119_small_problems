"""
Problem:
Write a function that takes a string, doubles every consonant in the string, 
and returns the result as a new string. The function should not double vowels 
('a','e','i','o','u'), digits, punctuation, or whitespace.

You may assume that only ASCII characters will be included in the argument.

input: string
output: string with every consonant doubled

rules:
    explicit:
    - only ascii characters included in the argument
    - only consonants are doubled
    implicit:
    - empty string returns empty
    - all non-consonant chars are singled

datastructure:
text-sequence

algorithm:
1.) create empty answer string
2.) if char is a consonant append it twice, else append it once
3.) repeat for all characters in input string
4.) return string
"""

def double_consonants(string):
    answer = ""
    for char in string:
        if char.isalpha() and char not in 'aeiouAEIOU':
            answer += char * 2
        else:
            answer += char
    return answer

# All of these examples should print True
print(double_consonants('String') == "SSttrrinngg")
print(double_consonants('Hello-World!') == "HHellllo-WWorrlldd!")
print(double_consonants('July 4th') == "JJullyy 4tthh")
print(double_consonants('') == "")