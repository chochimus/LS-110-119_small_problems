"""
Problem:
Given a dictionary, return its keys sorted by the values associated with each key.

input:  dictionary
output: keys sorted by values associated with each key
rules: 
    explicit:
    - given a dictionary sort the keys by their values and return it as a list
    implicit: 
    - values are all the same type and sortable

datastructure:
list

algorithm:
1.) create a list from dictionary keys
2.) sort list on key= key[value]
"""

def sort_key(item):
    return item[1]

def order_by_value(to_sort):
    return [key for key,value in sorted(to_sort.items(), key=sort_key)]

my_dict = {'p': 8, 'q': 2, 'r': 6}
keys = ['q', 'r', 'p']
print(order_by_value(my_dict) == keys)  # True