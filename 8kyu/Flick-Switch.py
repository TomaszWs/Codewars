# Task
#
# Create a function that always returns True/true for every item in a given
# list.
# However, if an element is the word 'flick', switch to always returning
# the opposite boolean value.
# Examples
#
# ['codewars', 'flick', 'code', 'wars'] ➞ [True, False, False, False]
#
# ['flick', 'chocolate', 'adventure', 'sunshine'] ➞ [False, False, False, False]
#
# ['bicycle', 'jarmony', 'flick', 'sheep', 'flick'] ➞ [True, True, False, False, True]
#
# Notes
#
#     "flick" will always be given in lowercase.
#     A list may contain multiple flicks.
#     Switch the boolean value on the same element as the flick itself.


def flick_switch(lst):
    switch = []
    current_val = True
    for i in lst:
        if i == "flick":
            current_val = not current_val
        switch.append(current_val)
    return switch


if __name__ == "__main__":
    print(flick_switch(['codewars', 'flick', 'code', 'wars']))


# Best solutions:


def flick_switch(lst):
	res, state = [], True
	for i in lst:
		if i == 'flick':
			state = not state
		res.append(state)
	return res


def flick_switch(lst):
    flick = True
    return [ (flick := flick ^ (v=='flick')) for v in lst]
