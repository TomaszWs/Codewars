# Description
#
# Everybody has probably heard of the animal heads and legs problem from the
# earlier years at school. It goes:
#
# “A farm contains chickens and cows.
# There are x heads and y legs.
# How many chickens and cows are there?”
#
# Where x <= 1000 and y <=1000
# Task
#
# Assuming there are no other types of animals, work out how many of each
# animal are there.
#
# Return a tuple in Python - (chickens, cows)
# or an array list - [chickens, cows]/{chickens, cows} in all other languages
#
# If either the heads & legs is negative, the result of your calculation is
# negative or the calculation is a float return "No solutions" (no valid
# cases), or [-1, -1] in COBOL.
#
# In the form:
#
# (Heads, Legs) = (72, 200)
#
# VALID - (72, 200) =>             (44 , 28)
#                              (Chickens, Cows)
#
# INVALID - (72, 201) => "No solutions"
#
# However, if 0 heads and 0 legs are given always return [0, 0] since zero
# heads must give zero animals.
#
# There are many different ways to solve this, but they all give the same
# answer.
#
# You will only be given integers types - however negative values (edge cases)
# will be given.
#
# Happy coding!


def animals(heads, legs):
    if heads == 0 and legs == 0:
        return (0, 0)
    if heads < 0 or legs < 0:
        return "No solutions"

    cows = (legs - 2 * heads) / 2
    chickens = heads - cows

    if cows < 0 or chickens < 0 or cows % 1 != 0 or chickens % 1 != 0:
        return "No solutions"
    return (int(chickens), int(cows))


if __name__ == '__main__':
    print(animals(72, 200))


# Best solutions:


def animals(heads, legs):
    chickens, cows = 2*heads-legs/2, legs/2-heads
    if (chickens < 0 or cows < 0 or not chickens == int(chickens)
            or not cows == int(cows)):
        return "No solutions"
    return chickens, cows


def animals(heads, legs):
    chickens = heads * 2 - legs / 2
    cows = heads - chickens
    if chickens < 0 or cows < 0 or chickens != int(chickens):
        return "No solutions"
    return (chickens, cows)


def animals(heads, legs):
    solution = (2 * heads - legs/2, legs/2 - heads)
    return solution if (legs % 2 == 0 and solution[0] >= 0
                        and solution[1] >= 0) else "No solutions"
