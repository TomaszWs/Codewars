# We all love to have some rest. Also we all hate the sound of our
# alarms but it's inevitable at the end of the day. However, one is
# definitely not enough to wake you up. You set multiple alarms, just
# to force yourself to get up and go back to work/studies or just
# anything. It is getting annoying, setting those up manually, so you
# decide to write a script for this task.
#
# Task
#
# Given the time to be set to wake up and the amount of alarms needed
# to be set, return an array of all timestamps for the alarms. The
# typical interval between the alarms is 5 minutes (at least, I think
# so).
#
# Examples
#
# set_the_alarms_up("08:00", 5)
# Should return ["08:00", "08:05", "08:10", "08:15", "08:20"]
# set_the_alarms_up("07:45", 8)
# Should return ["07:45", "07:50", "07:55", "08:00", "08:05",
# "08:10", "08:15", "08:20"]
# set_the_alarms_up("23:55", 2)
# Should return ["23:55", "00:00"]
#
# Input
#
# time - a string, representing the time. Will always be valid.
# (no 25:30, 08:65 and etc.)
#
# n - a number of alarms, needed to be set up. (n > 1, simply cause
# noone wakes up to one alarm)
# Output
#
# An array, consisting of all timestamps, an alarm is going to ring.
#
# Good luck!


def set_the_alarms_up(time, n):
    h, m = map(int, time.split(':'))
    l = []
    for i in range(n):
        l.append(f"{h:02d}:{m:02d}")
        m += 5
        if m >= 60:
            m -= 60
            h = (h + 1) % 24
    return l


if __name__ == '__main__':
    print(set_the_alarms_up("07:00", 3))


# Best solutions:


def set_the_alarms_up(time, n):
    h, m = [int(t) for t in time.split(':')]
    t = 60*h+m
    return [f'{(i//60)%24:02}:{i%60:02}' for i in range(t, t+5*n, 5)]


from datetime import datetime, timedelta


def set_the_alarms_up(time, n):
    time_obj = datetime.strptime(time, "%H:%M")
    time_range = [(time_obj + timedelta(minutes=5*_)).strftime("%H:%M") for _ in range(n)]
    return time_range
