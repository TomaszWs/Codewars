# For a pole vaulter, it is very important to begin the approach run at the
# best possible starting mark. This is affected by numerous factors and
# requires fine-tuning in practice. But there is a guideline that will help a
# beginning vaulter start at approximately the right location for the so-called
# "three-step approach," based on the vaulter's body height.
#
# This guideline was taught to me in feet and inches, but due to the
# international nature of Codewars, I am creating this kata to use metric units
# instead.
#
# You are given the following two guidelines to begin with: (1) A vaulter with
# a height of 1.52 meters should start at 9.45 meters on the runway. (2) A
# vaulter with a height of 1.83 meters should start at 10.67 meters on the
# runway.
#
# You will receive a vaulter's height in meters (which will always lie in a
# range between a minimum of 1.22 meters and a maximum of 2.13 meters). Your
# job is to return the best starting mark in meters, rounded to two decimal
# places.
#
# Hint: Based on the two guidelines given above, you will want to account for
# the change in starting mark per change in body height. This involves a linear
# relationship. (If you're not clear on that, search online for "linear
# equation.") But there is also a constant offset involved. If you can
# determine the rate of change described above, you should be able to determine
# that constant offset.


def starting_mark(height):
    return round(3.9355 * height + 3.4681, 2)


if __name__ == '__main__':
    print(starting_mark(1.52))


# Best solutions:


def starting_mark(height):
    return round(3.9355 * height + 3.4681, 2)


def starting_mark(height):
    x1, y1 = 1.52, 9.45
    x2, y2 = 1.83, 10.67
    slope = (y2-y1)/(x2-x1)
    offset = (x2*y1-x1*y2)/(x2-x1)
    return round(height * slope + offset, 2)


# The linear relashionship is obvious taking a couple a informations (L1,H1)
# and (L2,H2)
# One gets 3.9354838709677433 = (H1-H2)/(L1-L2) and
# beta = H1-3.9354838709677433*H1


def starting_mark(height):
    return round(3.9354838709677433*height+3.4680645161290293, 2)
