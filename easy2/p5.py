"""
Problem:
Write a function that combines two lists passed as arguments and returns a new list
that contains all elements from both list arguments, with each element taken in alternation.

You may assume that both input lists are non-empty, and that they have the same number of elements.

input: two lists
output: one list with all elements from input lists in an alterating pattern

rules:
    explicit:
    - non-empty lists
    - same number of element
    implicit:


datastructure:
list

algorithm
1.) create an empty list answer
2.) create an index variable
3.) add element from list1 and list2 to answer
5.) increment index
6.) repeat until end of list is reached
7.) return answer
"""

def interleave(list1, list2):
    answer = []
    for i in range(len(list1)):
        answer.extend([list1[i], list2[i]])
    return answer

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
expected = [1, "a", 2, "b", 3, "c"]
print(interleave(list1, list2) == expected)      # True

def interleave_zip(list1, list2):
    return [elem for pair in zip(list1, list2) for elem in pair]

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
expected = [1, "a", 2, "b", 3, "c"]
print(interleave_zip(list1, list2) == expected)  