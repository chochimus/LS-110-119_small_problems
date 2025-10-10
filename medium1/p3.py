"""
Problem:
Take the number 735291 and rotate it by one digit to the left, getting 352917. 
Next, keep the first digit fixed in place and rotate the remaining digits to get 329175. 
Keep the first two digits fixed in place and rotate again to get 321759. 
Keep the first three digits fixed in place and rotate again to get 321597. 
Finally, keep the first four digits fixed in place and rotate the final two digits to get 321579. 
The resulting number is called the maximum rotation of the original number.

Write a function that takes an integer as an argument and returns the maximum rotation of that integer. 
You can (and probably should) use the rotate_rightmost_digits function from the previous exercise.

input: digit
output: maximally rotated number

rules:
    explicit:
    for given example
    - rotate by one digit to the left
    - keep first digit fixed and rotate remaining
    - keep first two digits fixed and rotate remaining
    - repeat len - 1 times
    implicit:
    - don't expect bad input

datastructure:
integer

algorithm:

"""

def rotate_rightmost_digits(digit, count):
    if count == 1:
        return digit
    answer = str(digit)
    return int(answer[:-count] + answer[-count+1:] + answer[-count])

def max_rotation(digit):
    index = len(str(digit))
    while index > 0:
        digit = rotate_rightmost_digits(digit, index)
        index -=1
    return digit

print(max_rotation(735291) == 321579)          # True
print(max_rotation(3) == 3)                    # True
print(max_rotation(35) == 53)                  # True
print(max_rotation(8703529146) == 7321609845)  # True

# Note that the final sequence here is `015`. The leading
# zero gets dropped, though, since we're working with
# an integer.
print(max_rotation(105) == 15)                 # True