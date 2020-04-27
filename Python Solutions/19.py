'''
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.

A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
'''

# set variables to represent Jan 1st, 1900
counter = 0
year = 1900
month = 1
day = 1
day_of_week = 1
is_leap_year = False

while year < 2001:
    if 1900 < year:
        if day == 1 and day_of_week == 7:
            counter += 1

    # increment day per loop
    day += 1
    day_of_week += 1

    # increment weeks
    if day_of_week == 8:
        day_of_week = 1

    # increment monthes
    if day == 32 and (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12):
        day = 1
        month += 1
    elif day == 31 and (month == 4 or month == 6 or month == 9 or month == 11):
        day = 1
        month += 1
    elif day == 30 and month == 2 and is_leap_year:
        day = 1
        month += 1
    elif day == 29 and month == 2 and not is_leap_year:
        day = 1
        month += 1

    # increment years
    if month == 13:
        month = 1
        year += 1
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            is_leap_year = True
        else:
            is_leap_year = False

print(counter)
