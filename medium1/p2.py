"""
Problem:
Write a function that rotates the last count digits of a number. 
To perform the rotation, move the first of the digits that you want to 
rotate to the end and shift the remaining digits to the left.

input: intger, count
output: rotated digit

rules:
    explicit: positive integer input
    implicit: don't expect bad input

datastructure:
integers

algorithm:
we need to be able to easily flip the number at an index,
string is probably the best candidate

1.) create empty string answer
2.) set answer to input integer converted to string
3.) string sliced likes so: digits up to count +
    digits up to end starting at digit after count + digit at count
4.) return value converted to int
"""

def rotate_rightmost_digits(digit, count):
    if count == 1:
        return digit
    answer = str(digit)
    return int(answer[:-count] + answer[-count+1:] + answer[-count])

print(rotate_rightmost_digits(735291, 2) == 735219)  # True
print(rotate_rightmost_digits(735291, 3) == 735912)  # True
print(rotate_rightmost_digits(735291, 1) == 735291)  # True
print(rotate_rightmost_digits(735291, 4) == 732915)  # True
print(rotate_rightmost_digits(735291, 5) == 752913)  # True
print(rotate_rightmost_digits(735291, 6) == 352917)  # True
print(rotate_rightmost_digits(1200, 3) == 1002)      # True