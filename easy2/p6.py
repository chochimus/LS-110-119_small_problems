"""
Problem:
Write a function that takes a list of positive integers as input, 
multiplies all of the integers together, divides the result by the number 
of entries in the list, and returns the result as a string with the value 
rounded to three decimal places.

input: list of positive integers
output: multiplicative average of list as string rounded to three decimal places

rules:
    explicit:
    - positive integers
    - lists will not be empty
    - multiply all integers together, divide by number of integers, return that value
    - result is a string formatted to 3 decimals

    implicit:
    - output must always have 3 decimals
    - regular division
    - zero is excluded

datastructures:
lists

algorithm:
1.) create product variable equal to 1
2.) multiply product times current element
3.) repeat for all elements in the input list
4.) divide product by number of elements in input list 
5.) return result as string formatted to 3 decimals
"""

def multiplicative_average(nums):
    product = 1
    total = len(nums)
    for num in nums:
        product *= num
    
    avg = product / total
    return f"{avg:.3f}"

# All of these examples should print True
print(multiplicative_average([3, 5]) == "7.500")
print(multiplicative_average([2, 5, 8]) == "26.667")
print(multiplicative_average([2, 5]) == "5.000")
print(multiplicative_average([1, 1, 1, 1]) == "0.250")
print(multiplicative_average([2, 5, 7, 11, 13, 17]) == "28361.667")