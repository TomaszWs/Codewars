# My washing machine uses water amount of water to wash load (in JavaScript and
# Python) or max_load (in Ruby) amount of clothes. You are given a clothes
# amount of clothes to wash. For each single item of clothes above the load,
# the washing machine will use 10% more water (multiplicative) to clean.
#
# For example, if the load is 10, the amount of water it requires is 5 and the
# amount of clothes to wash is 14, then you need 5 * 1.1 ^ (14 - 10) amount of
# water.
#
# Write a function howMuchWater (JS)/how_much_water (Python and Ruby) to work
# out how much water is needed if you have a clothes amount of clothes. The
# function will accept 3 arguments: - water, load (or max_loadin Ruby) and
# clothes.
#
# My washing machine is an old model that can only handle double the amount of
# load (or max_load). If the amount of clothes is more than 2 times the
# standard amount of load (max_load), return 'Too much clothes'. The washing
# machine also cannot handle any amount of clothes less than load (max_load).
# If that is the case, return 'Not enough clothes'.
#
# The answer should be rounded to the nearest 2 decimal places.


def how_much_water(water, load, clothes):
    if clothes < load:
        return "Not enough clothes"
    if clothes > load * 2:
        return "Too much clothes"
    i = clothes - load
    return round(water * (1.1 ** i), 2)


if __name__ == '__main__':
    print(how_much_water())


# Best solutions:


def how_much_water(water, clothes, load):
    if load > 2 * clothes:
        return "Too much clothes"

    if load < clothes:
        return "Not enough clothes"

    for i in range(load - clothes):
        water *= 1.1

    return round(water, 2)


def how_much_water(l, x, n):
    return "Too much clothes" if n > 2*x else "Not enough clothes" if n < x \
        else round(1.1**(n-x)*l, 2)
