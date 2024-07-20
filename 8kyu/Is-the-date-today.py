# Write a simple function that takes as a parameter a date object and returns a
# boolean value representing whether the date is today or not.
#
# Make sure that your function does not return a false positive by only
# checking the day.


from datetime import datetime


def is_today(date: datetime) -> bool:
    today = datetime.today()
    return (date.year == today.year and date.month == today.month and date.day
            == today.day)


if __name__ == "__main__":
    print(is_today(datetime(2020, 10, 1, 1, 1, 1, 1)))
    print(is_today(datetime.today()))


# Best solutions:


from datetime import datetime

def is_today(date):
    return date.date() == datetime.today().date()


from datetime import datetime

def is_today(date):
    return date.strftime('%d-%m-%Y') == datetime.today().strftime('%d-%m-%Y')


from datetime import datetime

def is_today(date):
    currdate = datetime.today()
    return currdate.date() == date.date()
