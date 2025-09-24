"""
Problem:
Write a function that takes a list as an argument and returns a list that contains two elements, 
both of which are lists. Put the first half of the original list elements in the first element of 
the return value and put the second half in the second element. If the original list contains an 
odd number of elements, place the middle element in the first half list.


input: list
output: list that contains 2 lists, first half of input list in list one, second half in list 2

rules:
    explicit:
    - if odd, middle value goes in first list
    implicit
    - lists contain integers
    - empty input lists, return empty output lists

datastructure:
nested list

algorithm:
1.) determine split point of lists
2.) create a new list using a slice from beginning to midpoint and second list midpoint to endpoint
"""

def halvsies(numbers):
    midpoint = (len(numbers) + 1) // 2
    return [numbers[:midpoint], numbers[midpoint:]]

# All of these examples should print True
print(halvsies([1, 2, 3, 4]) == [[1, 2], [3, 4]])
print(halvsies([1, 5, 2, 4, 3]) == [[1, 5, 2], [4, 3]])
print(halvsies([5]) == [[5], []])
print(halvsies([]) == [[], []])
