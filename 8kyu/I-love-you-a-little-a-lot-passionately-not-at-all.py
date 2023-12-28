# Who remembers back to their time in the schoolyard, when girls would take a
# flower and tear its petals, saying each of the following phrases each time
# a petal was torn:
#
#     "I love you"
#     "a little"
#     "a lot"
#     "passionately"
#     "madly"
#     "not at all"
#
# If there are more than 6 petals, you start over with "I love you" for
# 7 petals, "a little" for 8 petals and so on.
#
# When the last petal was torn there were cries of excitement, dreams, surging
# thoughts and emotions.
#
# Your goal in this kata is to determine which phrase the girls would say at
# the last petal for a flower of a given number of petals. The number of
# petals is always greater than 0.


def how_much_i_love_you(nb_petals):
    petals = ["I love you", "a little", "a lot", "passionately", "madly", "not at all"]
    index = (nb_petals - 1) % len(petals)
    return petals[index]


nb_petals = 6
print(how_much_i_love_you(nb_petals))

# Best solutions:


def how_much_i_love_you(nb_petals):
    return ["I love you", "a little", "a lot", "passionately", "madly", "not at all"][nb_petals % 6 - 1]


def how_much_i_love_you(nb_petals):
    # your code
    words = {1: 'I love you', 2: 'a little', 3: 'a lot', 4: 'passionately',
            5: 'madly', 0: 'not at all'}
    return words[nb_petals%6]


def how_much_i_love_you(nb_petals):
    n = nb_petals % 6
    if n == 1:
        return "I love you"
    if n == 2:
        return "a little"
    if n == 3:
        return "a lot"
    if n == 4:
        return "passionately"
    if n == 5:
        return "madly"
    if n == 0:
        return "not at all"
