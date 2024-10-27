# Nathan loves cycling.
#
# Because Nathan knows it is important to stay hydrated, he drinks 0.5 litres
# of water per hour of cycling.
#
# You get given the time in hours and you need to return the number of litres
# Nathan will drink, rounded to the smallest value.
#
# For example:
#
# time = 3 ----> litres = 1
#
# time = 6.7---> litres = 3
#
# time = 11.8--> litres = 5


from math import floor


def litres(time):
    return floor(time * 0.5)


if __name__ == '__main__':
    print(litres(3))


# Best solutions:


def litres(time):
    return time // 2


def litres(time):
    return int(time*0.5)


def litres(time):
    return int(time/2)
