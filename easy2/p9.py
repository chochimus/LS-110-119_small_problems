"""
Problem:
Write a function that counts the number of occurrences of each element in a given list. 
Once counted, print each element alongside the number of occurrences. 
Consider the words case sensitive e.g. ("suv" != "SUV").

input: list
output: element along with number of occurences

rules:
    explicit:
    - print statement is in form word => count
    - case matters
    implicit(from examples):
    - no empty strings
    - order of output doesn't matter
    
data structure:
text sequence

algorithm:
1.) create dictionary counts
2.) if element in counts increment its value, otherwise set it to 1
3.) for each element output its key and value
"""

def count_occurrences(word_list):
    counts = {}
    for word in word_list:
        counts[word] = counts.get(word, 0) + 1
    
    for word, count in counts.items():
        print(f'{word} => {count}')

vehicles = ['car', 'car', 'truck', 'car', 'SUV', 'truck',
            'motorcycle', 'motorcycle', 'car', 'truck']

count_occurrences(vehicles)