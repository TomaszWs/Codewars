# Given 2 elevators (named "left" and "right") in a building with 3 floors
# (numbered 0 to 2), write a function elevator accepting 3 arguments
# (in order):
#
#     left - The current floor of the left elevator
#     right - The current floor of the right elevator
#     call - The floor that called an elevator
#
# It should return the name of the elevator closest to the called floor
# ("left"/"right").
#
# In the case where both elevators are equally distant from the called floor,
# choose the elevator to the right.
#
# You can assume that the inputs will always be valid integers between 0-2.
#
# Examples:
#
# elevator(0, 1, 0) # => "left"
# elevator(0, 1, 1) # => "right"
# elevator(0, 1, 2) # => "right"
# elevator(0, 0, 0) # => "right"
# elevator(0, 2, 1) # => "right"


def elevator(left, right, call):
    if left == call == right:
        return "right"
    elif left == call:
        return "left"
    elif right == call:
        return "right"
    elif abs(left - call) < abs(right - call):
        return "left"
    elif abs(left - call) >= abs(right - call):
        return "right"


if __name__ == '__main__':
    print(elevator(0, 2, 1))


# Best solutions:


def elevator(left, right, call):
    return "left" if abs(call - left) < abs(call - right) else "right"


def elevator(left, right, call):
    if abs(left-call) >= abs(right-call):
        return "right"
    else:
        return "left"


def elevator(left, right, call):
    return "left" if abs(left - call) < abs(right - call) else "right"
