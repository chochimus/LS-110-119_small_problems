"""
Problem:
Write a function that takes a list of numbers and returns a list with the same number of elements, 
but with each element's value being the running total from the original list.

input: list of numbers
output: list with same number of elements, but each elements value is running total from original list

rules:
    explicit:
        - empty list input should return empty list output
    implicit:
        - order is the same
    
datastructure:
-list

algorithm:

1. create empty list called answer and total integer
2. iterate over input list
3. for each element add value to total and append total to answer
4. return answer
"""

def running_total(nums):
    answer = []
    total = 0
    for num in nums:
        total += num
        answer.append(total)
    return answer

print(running_total([2, 5, 13]) == [2, 7, 20])    # True
print(running_total([14, 11, 7, 15, 20])
      == [14, 25, 32, 47, 67])                    # True
print(running_total([3]) == [3])                  # True
print(running_total([]) == [])                    # True