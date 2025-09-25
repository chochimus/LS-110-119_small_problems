"""
Problem:
Write a function that takes two list arguments, each containing a list of numbers, 
and returns a new list that contains the product of each pair of numbers from the 
arguments that have the same index. You may assume that the arguments contain the same number of elements.

input: two lists containing integers
ouput: a new list containing a product of each pair of numbers from input lists

rules:
    explicit: 
    - two lists containing integers
    - lists will contain same number of elements
    - lists will contain numbers
    - each result is a product of numbers at same index in both lists
    implicit:
    - lists are assumed to be non-empty
    - results should match input order
    - negative numbers are allowed

data structure:
list

algorithm:
1.) zip lists together
2.) return product of pair at current index
3.) repeat for all pairs
4.) return result
"""

def multiply_list(list1, list2):
    return [ele1 * ele2 for ele1,ele2 in zip(list1, list2)]

list1 = [3, 5, 7]
list2 = [9, 10, 11]
print(multiply_list(list1, list2) == [27, 50, 77])  # True
