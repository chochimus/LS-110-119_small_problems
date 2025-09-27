"""
Problem:
Transform two lists into frozen sets and find their common elements.

input: two lists
output: intersection of the two lists converted to frozen sets

rules:
    explicit:
    - lists must first be converted to frozen sets
    implicit:
    - no bad input should be expected

datastructure:
frozenset

algorithm:
1.) convert list1 and list2 to frozensets
2.) return the intersection of both lists
"""

def intersection(list1, list2):
    return frozenset(list1) & frozenset(list2)

list1 = [2, 4, 6, 8]
list2 = [1, 3, 5, 7, 8]
expected_result = frozenset({8})
print(intersection(list1, list2) == expected_result) # True