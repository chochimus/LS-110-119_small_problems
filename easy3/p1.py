"""
Problem:
The time of day can be represented as the number of minutes before or after midnight. 
If the number of minutes is positive, the time is after midnight. 
If the number of minutes is negative, the time is before midnight.

Write a function that takes a time using this minute-based format and returns 
the time of day in 24-hour format (hh:mm). Your function should work with any integer input.

You may not use Python's datetime module.

input: integer input
output: time of day in 24-hour format hh:mm

rules:
    explicit:
    - if minutes is positive, time is after midnight
    - if minutes is negative, time is before midnight
    - format should always be in format hh:mm
    - should work for any integer input
    implicit:
    - zero is allowed
    - no need to handle non-integer input

datastructure
text-sequence

algorithm:
1.) mod out max time in a day
2.) while hours greater than 24 subtract 24 from it
3.) while hours less than 0 add 24 to it
4.) 
"""

HOURS_PER_DAY = 24
MINUTES_PER_HOUR = 60
MINUTES_PER_DAY = HOURS_PER_DAY * MINUTES_PER_HOUR

def time_of_day(time):
    while time < 0:
        time += MINUTES_PER_DAY
    
    time = time % MINUTES_PER_DAY
    hours = time // MINUTES_PER_HOUR
    minutes = time % MINUTES_PER_HOUR
    return f'{hours:02d}:{minutes:02d}'

print(time_of_day(0) == "00:00")        # True
print(time_of_day(-3) == "23:57")       # True
print(time_of_day(35) == "00:35")       # True
print(time_of_day(-1437) == "00:03")    # True
print(time_of_day(3000) == "02:00")     # True
print(time_of_day(800) == "13:20")      # True
print(time_of_day(-4231) == "01:29")    # True