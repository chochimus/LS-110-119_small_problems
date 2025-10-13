"""
Problem:
Write a function that takes a string as an argument and returns that string with 
every occurrence of a "number word" -- 'zero', 'one', 'two', 'three', 
'four', 'five', 'six', 'seven', 'eight', 'nine' -- converted to its corresponding digit character.

You may assume that the string does not contain any punctuation.

input: string
output: string with every occurance of a number word converted to its corresponding digit character

rules:
    explicit:
    - convert numeric strings to their single digit form
    implicit:
    - expect good input
    - assume digits to be separated by space
    - expect lowercase value
datastructure:
string

algorithm:
1.) split string
2.) check if current token is a number word
3.) add string to answer, if numeric word add integer string instead
4.) return
"""

def word_to_digit(message):
    answer = []
    for token in message.split():
        match token:
            case 'zero':
                answer.append('0')
            case 'one':
                answer.append('1')
            case 'two':
                answer.append('2')
            case 'three':
                answer.append('3')
            case 'four':
                answer.append('4')
            case 'five':
                answer.append('5')
            case 'six':
                answer.append('6')
            case 'seven':
                answer.append('7')
            case 'eight':
                answer.append('8')
            case 'nine':
                answer.append('9')
            case _:
                answer.append(token)
    return ' '.join(answer) 

message = 'Please call me at five five five one two three four'
print(word_to_digit(message) == "Please call me at 5 5 5 1 2 3 4")
# Should print True