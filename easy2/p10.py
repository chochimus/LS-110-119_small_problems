"""
Problem:
Write a function that takes one argument, a list of integers, and returns the average of all the 
integers in the list, rounded down to the integer component of the average. 
The list will never be empty, and the numbers will always be positive integers.

input: list of integers
output: average of all the integers in the list rounded down to the integer component of the average

rules:
    explicit:
    - list will never be empty
    - numbers will always be positive integers

    implicit:
    - no need to handle negative or empty inputs

datastructure:
list

algorithm:
1.) sum all the values in the list
2.) integer division the sum over the number of elements in the list
3.) return the avg
"""

def average(nums):
    return sum(nums) // len(nums)

print(average([1, 5, 87, 45, 8, 8]) == 25)        # True
print(average([9, 47, 23, 95, 16, 52]) == 40)     # True
print(average([7]) == 7)                          # True