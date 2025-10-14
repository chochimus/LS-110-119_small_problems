"""
Problem:
A triangle is classified as follows:

Equilateral: All three sides have the same length.
Isosceles: Two sides have the same length, while the third is different.
Scalene: All three sides have different lengths.
To be a valid triangle, the sum of the lengths of the two shortest sides must be 
greater than the length of the longest side, and every side must have 
a length greater than 0. If either of these conditions is not satisfied, the triangle is invalid.

Write a function that takes the lengths of the three sides of a triangle as 
arguments and returns one of the following four strings representing the 
triangle's classification: 'equilateral', 'isosceles', 'scalene', or 'invalid'.

input: length of three sides of triangle
output: string representing triangle's classification

rules:
    explicit
    - sum of the lengths of the two shortest sides must be greater than the length of the longest
    side and every side must have a length greater than 0
    - equilateral all three sides have same length
    - isoceles two sides have same length third is different
    - scalene all three sides have differnt lengths
    implicit:
    - expect good input
    - 0 is valid
    - can be float or int

datastructure:
int

algorithm:
1.) first check if any side == 0
2.) next find longest side, check if two remaining sides sum > longest
3.) check all sides equal
4.) check two sides equal and third different
5.) else scalene
6.) return result
"""

def triangle(s1, s2, s3):
    sides = sorted([s1, s2, s3])
    if sides[0] <= 0:
        return "invalid"
    if sides[0] + sides[1] < sides[2]:
        return "invalid"
    if s1 == s2 == s3:
        return "equilateral"
    if s1 == s2 or s2 == s3 or s1 == s3:
        return "isosceles"
    else:
        return "scalene"
    
print(triangle(3, 3, 3) == "equilateral")  # True
print(triangle(3, 3, 1.5) == "isosceles")  # True
print(triangle(3, 4, 5) == "scalene")      # True
print(triangle(0, 3, 3) == "invalid")      # True
print(triangle(3, 1, 1) == "invalid")      # True