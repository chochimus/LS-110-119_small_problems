"""
Problem:
Some people believe that Fridays that fall on the 13th day of the month are unlucky days. 
Write a function that takes a year as an argument and returns the number of Friday the 
13ths in that year. You may assume that the year is greater than 1752, which is when 
the United Kingdom adopted the modern Gregorian Calendar. You may also assume that the 
same calendar will remain in use for the foreseeable future.

input: integer representing year
output: number of friday 13ths in that year

rules:
    explicit:
    - assume year is greater than 1752
    - gregorian calendar
    - same calendar will remain in use for forseeable future
    implicit:
    - expect a valid integer input

datastructure:
date

algorithm:
1.) check all months for year
2.) for each month check day that lands on 13th
3.) if friday increment count
4.) return count
"""

from datetime import datetime

def friday_the_13ths(year):
    return sum(datetime(year, month, 13).weekday() == 4 for month in range(1,13))
    

print(friday_the_13ths(1986) == 1)      # True
print(friday_the_13ths(2015) == 3)      # True
print(friday_the_13ths(2017) == 2)      # True