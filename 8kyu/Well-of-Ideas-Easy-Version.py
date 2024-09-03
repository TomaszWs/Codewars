# For every good kata idea there seem to be quite a few bad ones!
#
# In this kata you need to check the provided array (x) for good ideas 'good'
# and bad ideas 'bad'. If there are one or two good ideas, return 'Publish!',
# if there are more than 2 return 'I smell a series!'. If there are no good
# ideas, as is often the case, return 'Fail!'.


def well(x):
    gcounter = 0
    bcounter = 0
    for idea in x:
        if idea == "good":
            gcounter += 1
        elif idea == "bad":
            bcounter += 1
    if 2 >= gcounter >= 1:
        return "Publish!"
    elif gcounter > 2:
        return "I smell a series!"
    else:
        return "Fail!"


if __name__ == '__main__':
    print(well(['bad', 'bad', 'bad']))


# Best solutions:


def well(x):
    c = x.count('good')
    return 'I smell a series!' if c > 2 else 'Publish!' if c else 'Fail!'


def well(x):
    if x.count("good") == 0:
        return "Fail!"
    elif x.count("good") <= 2:
        return "Publish!"
    else:
        return "I smell a series!"


def well(x):
    if 'good' in x:
        return 'I smell a series!' if x.count('good') > 2 else 'Publish!'
    else:
        return 'Fail!'
