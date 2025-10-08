"""
Problem:
Write a function that takes a string as an argument and returns that string with a 
staggered capitalization scheme. Every other character, starting from the first, 
should be capitalized and should be followed by a lowercase or non-alphabetic character. 
Non-alphabetic characters should not be changed, but should be counted as characters for 
determining when to switch between upper and lower case.

input: string
ouput: staggered capitalization

rules:
    explicit:
    - every other character should be capitalized followed by a lowercase (or non-alphabetic) character
    - non alphabetic character will be normal but counted as chars
    implicit:
    - expect good input
    - empty string will return empty string

datastructure:
string

algorithm:
1.) check index of char, if even and alpha capitalize if odd and alpha lower case
2.) repeat for every char
"""

def staggered_case(string):
    answer = ""
    for idx,char in enumerate(string):
        answer += char.upper() if idx % 2 == 0 else char.lower()
    return answer

string = 'I Love Launch School!'
result = "I LoVe lAuNcH ScHoOl!"
print(staggered_case(string) == result)  # True

string = 'ALL_CAPS'
result = "AlL_CaPs"
print(staggered_case(string) == result)  # True

string = 'ignore 77 the 4444 numbers'
result = "IgNoRe 77 ThE 4444 nUmBeRs"
print(staggered_case(string) == result)  # True

print(staggered_case('') == "")          # True