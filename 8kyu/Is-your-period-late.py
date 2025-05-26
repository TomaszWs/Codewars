# In this kata, we will make a function to test whether a period is late.
#
# Our function will take three parameters:
#
# last - The Date object with the date of the last period
#
# today - The Date object with the date of the check
#
# cycleLength - Integer representing the length of the cycle in days
#
# Return true if the number of days passed from last to today is greater than
# cycleLength. Otherwise, return false.


from datetime import date


def period_is_late(last,today,cycle_length):
    return (today - last).days > cycle_length


if __name__ == '__main__':
    print(period_is_late(date(2016, 6, 13), date(2016, 7, 16), 35))


# Best solutions:


def period_is_late(last,today,cycle_length):
    return cycle_length < (today - last).days


def period_is_late(last,today,cycle_length):
    delta = today - last
    if delta.days > cycle_length:
        return True
    else:
        return False
#Completed by Ammar on 31/7/2019 at 04:37PM.


import datetime


def period_is_late(last,today,c):
    d = (today - last).days
    return d > c
