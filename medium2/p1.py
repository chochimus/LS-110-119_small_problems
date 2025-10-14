"""
Problem:
Write a function that takes a string and returns a dictionary containing the 
following three properties:

the percentage of characters in the string that are lowercase letters
the percentage of characters that are uppercase letters
the percentage of characters that are neither
All three percentages should be returned as strings whose numeric values lie 
between "0.00" and "100.00", respectively. Each value should be rounded to two decimal points.

You may assume that the string will always contain at least one character.

input: string
output: dictionary containing percentage of chars that are lowercase, 
        percentage that are uppercase
        percentage that are neither

rules:
    explicit:
    - straightforward rules in problem description
    - percentages should be rounded to two decimal places
    implicit:
    - assume good input
    - assume at least one char

data structure:
dictionary

algorithm:
1.) create lower total, upper total, neither total variables set to zero
2.) if char is upper increment upper, similar for lower and neither
3.) repeat for every char
4.) return formatted result
"""

def letter_percentages(string):
    lower = upper = neither = 0
    total = len(string)
    for char in string:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
        else:
            neither += 1
    return {'lowercase': f'{(lower/total)*100:.2f}',
            'uppercase': f'{(upper/total)*100:.2f}',
            'neither': f'{(neither/total)*100:.2f}'}

expected_result = {
    'lowercase': "50.00",
    'uppercase': "10.00",
    'neither': "40.00",
}
print(letter_percentages('abCdef 123') == expected_result)

expected_result = {
    'lowercase': "37.50",
    'uppercase': "37.50",
    'neither': "25.00",
}
print(letter_percentages('AbCd +Ef') == expected_result)

expected_result = {
    'lowercase': "0.00",
    'uppercase': "0.00",
    'neither': "100.00",
}
print(letter_percentages('123') == expected_result)