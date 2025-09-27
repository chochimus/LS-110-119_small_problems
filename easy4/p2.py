"""
Problem:
Given two lists, convert them to sets and return a new set which is the union of both sets.

input: two lists
output: union of lists

rules:
    explicit:
    - both lists should be converted to set
    - new set should be returned that is a union of both
    implicit:
    - no need to have special input handling

datastructure
set

algorithm:
1.) convert list1 to set
2.) convert list2 to set
3.) return set1.union(set2)
"""

def merge_sets(list1, list2):
    return set(list1) | set(list2)

list1 = [3, 5, 7, 9]
list2 = [5, 7, 11, 13]
print(merge_sets(list1, list2) == {3, 5, 7, 9, 11, 13})
# Prints True