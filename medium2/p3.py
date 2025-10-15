"""
Problem:
A triangle is classified as follows:

Right: One angle is a right angle (exactly 90 degrees).
Acute: All three angles are less than 90 degrees.
Obtuse: One angle is greater than 90 degrees.
To be a valid triangle, the sum of the angles must be exactly 180 degrees, 
and every angle must be greater than 0. If either of these conditions is not satisfied, 
the triangle is invalid.

Write a function that takes the three angles of a triangle as arguments and returns 
one of the following four strings representing the triangle's classification: 
'right', 'acute', 'obtuse', or 'invalid'.

You may assume that all angles have integer values, so you do not have to 
worry about floating point errors. You may also assume that the arguments are in degrees.

input: three integer values
output: string representing triangle's classification

rules:
    explicit:
    - acute triangle, all angles less than 90
    - right one angle is 90
    - obtuse, one angle greater than 90
    - to be valid sum of angles must be 180
    - every angle must be greater than 0
    - all input will be integers
    - arguments are in degrees
    implicit:
    - no bad invalid input should be expected
    - 0 should be handled

datastructure:
integer

algorithm:
1.) check if any angle == 0
2.) check if sum of angles > 180
3.) check if any angle == 90
4.) check if any angle > 90
5.) otherwise acute
6.) return string answer
"""

def triangle(angle1, angle2, angle3):
    if angle1 == 0 or angle2 == 0 or angle3 == 0:
        return "invalid"
    if sum((angle1, angle2, angle3)) != 180:
        return "invalid"
    if angle1 == 90 or angle2 == 90 or angle3 == 90:
        return "right"
    if angle1 > 90 or angle2 > 90 or angle3 > 90:
        return "obtuse"
    return "acute"

print(triangle(60, 70, 50) == "acute")      # True
print(triangle(30, 90, 60) == "right")      # True
print(triangle(120, 50, 10) == "obtuse")    # True
print(triangle(0, 90, 90) == "invalid")     # True
print(triangle(50, 50, 50) == "invalid")    # True