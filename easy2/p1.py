"""
Problem:
Write a function that takes a floating point number representing an angle between 0 and 360 degrees 
and returns a string representing that angle in degrees, minutes, and seconds. 
You should use a degree symbol (°) to represent degrees, a single quote (') to represent minutes, 
and a double quote (") to represent seconds. There are 60 minutes in a degree, and 60 seconds in a minute.

Note: You can use the following constant to represent the degree symbol:
DEGREE = "\u00B0"

input: floating point number representing angle between 0 and 360 degrees
output: string representing angle in degrees, minutes, and seconds

rules:
    explicit:
    - convert float to angle, minutes and seconds 
    - 60 minutes in a degree, 60 seconds in a minute
    - minutes and seconds should be integers
    implicit:
    - negative inputs
    - output format is 0-3 digit number, followed by 2 2-digit numbers (0 as placeholder)
    - degree is truncated rather than rounded

datastruct:
N/A

algorithm:
1.) convert float to integer, then string
2.) calculate minutes and seconds and concatenate them to the string
3.) return result
"""

DEGREE = "\u00B0"
MINUTES_IN_DEGREE = 60
SECONDS_IN_MINUTE = 60
SECONDS_IN_DEGREE = MINUTES_IN_DEGREE * SECONDS_IN_MINUTE

def dms(degree_float):
    degree_int = int(degree_float)
    minutes = int((degree_float - degree_int) * MINUTES_IN_DEGREE)
    seconds = int((degree_float - degree_int - (minutes / MINUTES_IN_DEGREE)) * SECONDS_IN_DEGREE)

    return (f"{degree_int}{DEGREE}{minutes:02d}'{seconds:02d}\"")

# All of these examples should print True
print(dms(30) == "30°00'00\"")
print(dms(76.73) == "76°43'48\"")
print(dms(254.6) == "254°35'59\"" or dms(254.6) == "254°36'00\"")
print(dms(93.034773) == "93°02'05\"")
print(dms(0) == "0°00'00\"")
print(dms(360) == "360°00'00\"" or dms(360) == "0°00'00\"")