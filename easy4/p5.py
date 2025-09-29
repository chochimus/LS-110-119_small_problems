"""
Problem:
From two list arguments, determine the elements that are unique to the first list. The return value should be a set.

input: two lists
output: set of elements that are unique to the first list

rules
    explicit:
    - return value should be a set
    implicit:
    - empty sets or bad input doesn't need to be handled

datastructure:
set

algorithm
1.) convert both lists to sets
2.) return set 1 - set 2
"""

def unique_from_first(list1, list2):
    return set(list1) - set(list2)

list1 = [3, 6, 9, 12]
list2 = [6, 12, 15, 18]
print(unique_from_first(list1, list2) == {9, 3})