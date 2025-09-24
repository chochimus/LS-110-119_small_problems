"""
Problem:
Given an unordered list and the information that exactly one value in the list occurs twice 
(every other value occurs exactly once), determine which value occurs twice. 
Write a function that finds and returns the duplicate value.

You may assume that the input list will always have exactly one duplicate value.

input: unordered list
output: integer that occurs twice

rules:
    explicit:
    - one value will occur twice
    implicit:
    - list elements are integers
    - list will not be empty

datastructure:
list

algorithm:
1.) create set
2.) if variable in set return variable otherwise add element to set
3.) repeat for every element in list
"""

def find_dup(dup_list):
    counts = set()
    for num in dup_list:
        if num in counts:
            return num
        counts.add(num)
        
print(find_dup([1, 5, 3, 1]) == 1) # True
print(find_dup([
                  18,  9, 36, 96, 31, 19, 54, 75, 42, 15,
                  38, 25, 97, 92, 46, 69, 91, 59, 53, 27,
                  14, 61, 90, 81,  8, 63, 95, 99, 30, 65,
                  78, 76, 48, 16, 93, 77, 52, 49, 37, 29,
                  89, 10, 84,  1, 47, 68, 12, 33, 86, 60,
                  41, 44, 83, 35, 94, 73, 98,  3, 64, 82,
                  55, 79, 80, 21, 39, 72, 13, 50,  6, 70,
                  85, 87, 51, 17, 66, 20, 28, 26,  2, 22,
                  40, 23, 71, 62, 73, 32, 43, 24,  4, 56,
                   7, 34, 57, 74, 45, 11, 88, 67,  5, 58,
              ]) == 73)       # True