"""
Problem:
    Modify the word_sizes function from the previous exercise to exclude non-letters when determining word size. 
    For instance, the word size of "it's" is 3, not 4.

input: string consisting of zero or more space-separated words
output: dictionary that shows the number of words of different sizes    

Rules:
    explicit:
    - words consist of any sequence of non-space, non-punctuation characters
    - empty string returns empty dictionary

    implicit:
    - strings of only punctuation should not be counted

questions: which symbol characters count as @ symbol is counted, but ! is not
    
data structure:
dictionary

algorithm:
1.) split string on spaces
2.) add length of current element to dictionary
3.) repeat step 2 for each element of split string
4.) return dictionary
"""

def word_sizes(input_string):
    answer = {}
    word_list = input_string.split()
    for word in word_list:
        word_length = 0
        for char in word:
            if char.isalpha():
                word_length += 1
        
        if word_length == 0:
            continue
        answer[word_length] = answer.get(word_length, 0) + 1
    
    return answer

# All of these examples should print True

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 2, 3: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 3})

string = 'Humpty Dumpty sat on a w@ll'
print(word_sizes(string) == {6: 2, 3: 2, 2: 1, 1: 1})

string = "What's up doc?"
print(word_sizes(string) == {5: 1, 2: 1, 3: 1})

print(word_sizes('') == {})

print(word_sizes("./...,,") == {})