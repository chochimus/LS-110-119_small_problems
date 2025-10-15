"""
Problem:
A featured number (something unique to this exercise) is an odd number that is a
 multiple of 7, with all of its digits occurring exactly once each. For example, 49 
 is a featured number, but 98 is not (it is not odd), 97 is not 
 (it is not a multiple of 7), and 133 is not (the digit 3 appears twice).

Write a function that takes an integer as an argument and returns the next 
featured number greater than the integer. Issue an error message if there 
is no next featured number.

NOTE: The largest possible featured number is 9876543201.


input: int
output: the next featured number greater than the integer

rules:
    explicit
    - odd number that is a multiple of 7 with all of its digits occuring once
    - 9876543201 is the largest possible
    implicit:
    - expect integer input

datastructure:
integer

algorithm:
1.) create answer = input
2.) check if answer % 7 is == 0 otherwise add remainder to number
3.) if every digit doesn't occur once and number isn't odd add 7
4.) repeat until featured number is found
"""

def next_featured(number):
    answer = number + 1
    while answer % 7 != 0 or answer % 2 == 0:
        answer += 1
    
    while answer <= 9876543202:
        if len(str(answer)) == len(set(str(answer))):
            return answer
        answer += 14
    return "There is no possible number that fulfills those requirements."

print(next_featured(12) == 21)                  # True
print(next_featured(20) == 21)                  # True
print(next_featured(21) == 35)                  # True
print(next_featured(997) == 1029)               # True
print(next_featured(1029) == 1043)              # True
print(next_featured(999999) == 1023547)         # True
print(next_featured(999999987) == 1023456987)   # True
print(next_featured(9876543186) == 9876543201)  # True
print(next_featured(9876543200) == 9876543201)  # True

error = ("There is no possible number that "
         "fulfills those requirements.")
print(next_featured(9876543201) == error)       # True