"""
Problem: 
Given a dictionary and a list of keys, produce a new dictionary that only 
contains the key/value pairs for the specified keys.

input: dictionary, list of keys
output: dictionary that contains the key/value pairs for specified keys

rules
    explicit:
    - input/output rules
    implicit:
    - expcect no bad input

datastructure
dictionary

algorithm:
1.) create empty dictionary answer
2.) check if key in dictionary
3.) if so add to answer
4.) repeat for all elements
"""

def keep_keys(input_dict, keys):
    return {key: input_dict[key] for key in input_dict if key in keys}

input_dict = {
    'red': 1,
    'green': 2,
    'blue': 3,
    'yellow': 4,
}

keys = ['red', 'blue']
expected_dict = {'red': 1, 'blue': 3}
print(keep_keys(input_dict, keys) == expected_dict) # True