# At the annual family gathering, the family likes to find the oldest living
# family member’s age and the youngest family member’s age and calculate the
# difference between them.
#
# You will be given an array of all the family members' ages, in any order.
# The ages will be given in whole numbers, so a baby of 5 months, will have
# an ascribed ‘age’ of 0. Return a new array (a tuple in Python) with
# [youngest age, oldest age, difference between the youngest and oldest age].


def difference_in_ages(ages):
    return (min(ages), max(ages), max(ages)-min(ages))


if __name__ == "__main__":
    print(difference_in_ages([16, 22, 31, 44, 3, 38, 27, 41, 88]))


# Best solutions:


def difference_in_ages(ages):
    x, y = min(ages), max(ages)
    return x, y, y-x


def difference_in_ages(ages):
    age = sorted(ages)
    return (age[0], age[-1], (age[-1]-age[0]))
