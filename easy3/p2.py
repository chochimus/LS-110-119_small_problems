"""
Problem:
As seen in the previous exercise, the time of day can be represented as the number of 
minutes before or after midnight. If the number of minutes is positive, the time is after midnight. 
If the number of minutes is negative, the time is before midnight.

Write two functions that each take a time of day in 24 hour format, 
and return the number of minutes before and after midnight, respectively. 
Both functions should return a value in the range 0 through 1439.

You may not use Python's datetime module.

input: time of day in 24 hour format
output: number of minutes before and after midnight, respectively

rules:
    explicit:
    - input time is in form "hh:mm"
    - after midnight function will handle hours after
    - before midnight function will handle hours before
    - can't use datetime module
    implicit:
    - no bad input is expected

datastructure:
int

algorithm:
1.) convert string to hours and minutes
2.) if after midnight calculate starting from 0
3.) if before midnight calculate starting from 1440
"""

MINUTES_PER_HOUR = 60
HOURS_PER_DAY = 24
MINUTES_PER_DAY = HOURS_PER_DAY * MINUTES_PER_HOUR

def after_midnight(time):
    pieces = time.split(':')
    hours_as_minutes = int(pieces[0]) * MINUTES_PER_HOUR
    minutes = int(pieces[1]) + hours_as_minutes
    return 0 if minutes == MINUTES_PER_DAY else minutes
    
def before_midnight(time):
    pieces = time.split(':')
    hours_as_minutes = int(pieces[0]) * MINUTES_PER_HOUR
    minutes = int(pieces[1]) + hours_as_minutes
    return 0 if minutes == 0 else MINUTES_PER_DAY - minutes 

print(after_midnight("00:00") == 0)     # True
print(before_midnight("00:00") == 0)    # True
print(after_midnight("12:34") == 754)   # True
print(before_midnight("12:34") == 686)  # True
print(after_midnight("24:00") == 0)     # True
print(before_midnight("24:00") == 0)    # True
