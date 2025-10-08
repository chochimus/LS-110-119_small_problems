"""
Problem:
Write a function that takes one argument, a positive integer, and returns the sum of its digits.

input: positive integer
output: sum of digits

rules:
    explicit:
    - positive integer input
    implicit:
    - no need to handle bad input

datastructure:
integer

algorithm:
1.) mod input by 10
2.) add value to total
3.) divide input by 10
4.) repeat until number == 0
5.) return total

"""

def sum_digits(number):
    total = 0
    while number > 0:
        total += number % 10
        number //= 10
    return total

print(sum_digits(23) == 5)              # True
print(sum_digits(496) == 19)            # True
print(sum_digits(123456789) == 45)      # True