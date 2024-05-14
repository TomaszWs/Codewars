# Your task is to create a change machine.
#
# The machine accepts a single coins or notes, and returns change in 20p and
# 10p coins. The machine will try to avoid returning its exact input, but will
# otherwise return as few coins as possible. For example, a 50p piece should
# become two 20p pieces and one 10p piece, but a 20p piece should become
# two 10p pieces.
#
# The machine can exclusively process these coins and notes: £5, £2, £1, 50p,
# 20p. Any coins and notes which are not accepted by the machine will be
# returned unprocessed. For example, if you were to put a £20 note into
# the machine, it would be returned to you and not broken into change.
# (Note that £1 is worth 100p.)
#
# This change machine is programmed to accept and distribute strings rather
# than numbers. The input will be a string containing the coin or note to be
# processed, and the change should be returned as one string with the coin
# names separated by single spaces with no commas. The values of the string
# should be in descending order. For example, an input of "50p" should yield
# the exact string "20p 20p 10p".


def change_me(money):
    p = {
        "£5": 500,
        "£2": 200,
        "£1": 100,
        "50p": 50,
        "20p": 20
    }
    if money not in p:
        return money
    value = p[money]
    n_20p = value // 20
    rest = value % 20
    n_10p = rest // 10
    if money == "20p":
        n_20p = 0
        n_10p = 2
    change = []
    change.extend(["20p"] * n_20p)
    change.extend(["10p"] * n_10p)
    return " ".join(change)


print(change_me("50p"))


# Best solutions:


def change_me(money):
    match money:
        case "£5":
            return " ".join(["20p"] * 25)
        case "£2":
            return " ".join(["20p"] * 10)
        case "£1":
            return " ".join(["20p"] * 5)
        case "50p":
            return "20p 20p 10p"
        case "20p":
            return "10p 10p"
        case _:
            return money


def change_me(money):
    nominals = ['£5', '£2', '£1', '50p', '20p']
    if money not in nominals:
        return money
    if money == nominals[-1]:
        return '10p 10p'
    if money == nominals[-2]:
        return '20p 20p 10p'

    coins = int(money[1]) * 5
    return ' '.join(['20p'] * coins)


def change_me(money):
    if money == "£5":
        return ("20p " * 25).strip()
    elif money == "£2":
        return ("20p " * 10).strip()
    elif money == "£1":
        return ("20p " * 5).strip()
    elif money == "50p":
        return (("20p " * 2) + "10p").strip()
    elif money == "20p":
        return ("10p " * 2).strip()
    else:
        return money