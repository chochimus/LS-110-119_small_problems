"""
Problem:
Write a function that takes a string as an argument and returns True if all 
parentheses in the string are properly balanced, False otherwise. 
To be properly balanced, parentheses must occur in matching '(' and ')' pairs.

input: string
output: boolean determined by all parentheses in the string being balanced

rules:
    explicit:
    - balanced parentheses means each '(' has a matching ')'
    implicit:
    - no parentheses is considered balanced

datastructure:

algorithm:
1.) curr = 0
2.) if char is '(' increment curr
3.) if char is ')' decrement curr
4.) if curr is negative return False
5.) return if curr == 0
"""

def is_balanced(input_str):
    curr = 0
    for char in input_str:
        if char == '(':
            curr += 1
        elif char == ')':
            curr -= 1
        if curr < 0:
            return False
    return curr == 0

print(is_balanced("What (is) this?") == True)        # True
print(is_balanced("What is) this?") == False)        # True
print(is_balanced("What (is this?") == False)        # True
print(is_balanced("((What) (is this))?") == True)    # True
print(is_balanced("((What)) (is this))?") == False)  # True
print(is_balanced("Hey!") == True)                   # True
print(is_balanced(")Hey!(") == False)                # True
print(is_balanced("What ((is))) up(") == False)      # True