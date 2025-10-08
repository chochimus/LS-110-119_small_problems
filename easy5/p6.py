"""
Problem:
Write a function that takes a list of numbers and returns the sum of the 
sums of each leading subsequence in that list. Examine the examples to see what we mean. 
You may assume that the list always contains at least one number.

input: list of numbers
output: returns sum of the sums of each leading subsequence in that list

rules:
    explicit:
    - sum every subsequence, then sum each sum
    - list will contain at least one number
    implicit:
    - no need to handle bad or empty input

datastructure:
int

algorithm:
1.) create empty total
2.) total current list
3.) iterate
4.) repeat for length of list
5.) return total
"""

def sum_of_sums(nums):
    total = 0
    prefix = 0
    for num in nums:
        prefix += num
        total += prefix
    return total

print(sum_of_sums([3, 5, 2]) == 21)               # True
# (3) + (3 + 5) + (3 + 5 + 2) --> 21

print(sum_of_sums([1, 5, 7, 3]) == 36)            # True
# (1) + (1 + 5) + (1 + 5 + 7) + (1 + 5 + 7 + 3) --> 36

print(sum_of_sums([1, 2, 3, 4, 5]) == 35)         # True
# (1) + (1+2) + (1+2+3) + (1+2+3+4) + (1+2+3+4+5) --> 35

print(sum_of_sums([4]) == 4)                      # True