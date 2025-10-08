"""
Problem:
Given a sequence of integers, filter out instances where the same value occurs successively, 
retaining only the initial occurrence. Return the refined sequence.

input: sequence of integers
output: sequence of integers where successive same values are filtered out

rules:
    explicit:
    - only initial occurance of successively same values should be added
    implicit:
    - only handle good input

datastucture
list

algorithm:
1.) create empty list answer
2.) check if previous == current value
3.) if not 2 add value to list and set previous == current else continue
4.) repeat for all values
5.) return answer
"""

def unique_sequence(nums):
    answer = []
    previous = None
    for num in nums:
        if num != previous:
            answer.append(num)
            previous = num
    return answer

# comprehension solution return [num for idx,num in enumerate(nums) if idx == 0 or nums[idx-1] != num]

original = [1, 1, 2, 6, 6, 6, 5, 5, 3, 3, 3, 4]
expected = [1, 2, 6, 5, 3, 4]
print(unique_sequence(original) == expected)      # True