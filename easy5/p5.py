"""
Problem:
Given two lists of integers of the same length, 
return a new list where each element is the product of the corresponding elements from the two lists.

input: two lists
output: new list where each ellement is the product of the corresponding elements from the two lists

rules:
    explicit:
    - stated in output
    implicit:
    - expect good input

datastructure:
list

algorithm:
1.) zip lists
2.) create list comprehension that iterates zip
3.) for each pair in zip get product 
4.) return comprehension

"""

def multiply_items(list_a, list_b):
    return [a * b for a,b in zip(list_a, list_b)]

list_a = [1, 2, 3]
list_b = [4, 5, 6]
print(multiply_items(list_a, list_b) == [4, 10, 18]) # True