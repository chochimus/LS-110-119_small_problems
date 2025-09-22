"""
Problem:

Given a string of words separated by spaces, write a function that swaps the first and last letters of every word.

You may assume that every word contains at least one letter, and that the string will always contain at least one word. 
You may also assume that each string contains nothing but words and spaces, and that there are no leading, trailing, 
or repeated spaces.

input: string of words separated by spaces
output: string of words with first and last letters of every word swapped

rules:
    explicit:
    - words will contain at least one letter
    - string will contain at least one word
    - string will contain only words and spaces
    - no leading/trailing/repeated spaces

    implicit:
    - single letter words are unchanged

question:
- strings contain only words and spaces, but can words contain other characters such as numbers or punctuation?

data-structure:
- string

algorithm:

1.) separate string into list of words
2.) for each word swap first and last letters

"""

def swap(input_string):
    word_list = input_string.split()
    for i,word in enumerate(word_list):
        if len(word) > 1:
            word_list[i] = word[-1] + word[1:-1] + word[0]
    return ' '.join(word_list)

print(swap('Oh what a wonderful day it is')
      == "hO thaw a londerfuw yad ti si")  # True
print(swap('Abcde') == "ebcdA")            # True
print(swap('a') == "a")                    # True