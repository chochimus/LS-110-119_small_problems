"""
Problem:
Create a function that takes two integers as arguments. The first argument is a count, 
and the second is the starting number of a sequence that your function will create. 
The function should return a list containing the same number of elements as the count argument. 
The value of each element should be a multiple of the starting number.

You may assume that count will always be an integer greater than or equal to 0. 
The starting number can be any integer. If the count is 0, the function should return an empty list.

input: two integers, first is a count, second is starting number of sequence to create
ouput: list containing the same number of elements as count, each value will be a multiple of the starting number

rules:
    explicit:
    - count will always be an integer greater than or equal to 0
    - starting number can be any number
    - 0 count will return empty list
    implicit:
    - no need to handle non integer/ empty input

datastructure:
list

algorithm:
1.) create empty answer list
2.) starting from start number append to list
3.) increment by start value
4.) repeat for count ( if 0 steps 2-3 will not occur)
5.) return list
"""

def sequence(count, start):
    return [start * num for num in range(1, count + 1)]

print(sequence(5, 1) == [1, 2, 3, 4, 5])          # True
print(sequence(4, -7) == [-7, -14, -21, -28])     # True
print(sequence(3, 0) == [0, 0, 0])                # True
print(sequence(0, 1000000) == [])                 # True