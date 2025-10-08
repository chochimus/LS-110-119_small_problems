"""
Problem:
Modify the function from the previous exercise so it ignores non-alphabetic 
characters when determining whether it should uppercase or lowercase each letter. 
The non-alphabetic characters should still be included in the return value; 
they just don't count when toggling the desired case.

input: string
ouput: string with every other alphabetic character case-swapped

rules:
    explicit:
    - same as previous but ignore non-alphabetic characters when making determination
    implicit:
    - expect good input

datastructure:
string

algorithm:
1.) create index variable and empty string answer
2.) check if index is even/odd and character is alpha
3.) change case depending on index odd/even
4.) increment index if char is alpha
5.) repeat for every character in input string
6.) return answer
"""

def staggered_case(string):
    answer = ""
    idx = 0
    for char in string:
        if char.isalpha():
            answer += char.upper() if idx % 2 == 0 else char.lower()
            idx += 1
        else:
            answer += char
    return answer

string = 'I Love Launch School!'
result = "I lOvE lAuNcH sChOoL!"
print(staggered_case(string) == result)  # True

string = 'ALL_CAPS'
result = "AlL_cApS"
print(staggered_case(string) == result)  # True

string = 'ignore 77 the 4444 numbers'
result = "IgNoRe 77 ThE 4444 nUmBeRs"
print(staggered_case(string) == result)  # True

print(staggered_case('') == "")          # True