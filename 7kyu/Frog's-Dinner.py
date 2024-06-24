# Thanks for checking out my kata - in the below problem - the highest n can be
# is 200.
#
# Example summation of a number - summation of the number 5 1+2+3+4+5 = 15
# summation of the number 6 1+2+3+4+5+6 = 21
#
# You are sat with two frogs on a log, Chris and Tom. They are arguing about
# who ate the most flies (Poor flies, but what you going to do!). Chris says
# "I ate the summation of n number of flies!".
#
# Tom replies "Take half the number you ate then round it down and work out the
# summation of that, that is how many I ate"!
#
# Cat then hops onto the log looking pleased with herself "Well, I ate the
# summation of both your dinners combined." Loz who came late to this meeting
# of amphibians is very confused, he asks "So how many did each of you eat?"
#
# Write a function called frogContest which returns a string "Chris ate
# {number} flies, Tom ate {number} flies and Cat ate {number} flies"
#
# {number} is the integer value of the amount of flies eaten by each.


def frog_contest(flies):
    return (f"Chris ate {sum(range(1,flies+1))} flies, Tom ate "
            f"{sum(range(1, (sum(range(1,flies+1)) // 2) + 1))} flies and Cat "
            f"ate {sum(range(1, 1+ sum(range(1,flies+1)) + sum(range(1, (sum(range(1,flies+1)) // 2) + 1))))} flies")


if __name__ == "__main__":
    print(frog_contest(5))


# Best solutions:


def frog_contest(x):
    f = lambda n: n * (n + 1) // 2

    a = f(x)
    b = f(a // 2)
    c = f(a + b)

    return f"Chris ate {a} flies, Tom ate {b} flies and Cat ate {c} flies"


def frog_contest(flies):
    chris_flies = sum(range(1, flies + 1))
    tom_flies = sum(range(1, chris_flies // 2 + 1))
    cat_flies = sum(range(1, chris_flies + tom_flies + 1))
    return f"Chris ate {chris_flies} flies, Tom ate {tom_flies} flies and Cat ate {cat_flies} flies"


def frog_contest(flies):
    chris = sum(flies)
    tom = sum(chris // 2)
    cat = sum(chris+tom)
    return "Chris ate {} flies, Tom ate {} flies and Cat ate {} flies".format(chris, tom, cat)


def sum(flies):
    return int(((1 + flies) / 2) * flies)
