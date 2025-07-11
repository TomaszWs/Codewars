# Your Task
#
# Given an array of Boolean values and a logical operator, return a Boolean
# result based on sequentially applying the operator to the values in the
# array.
# Examples
#
#     booleans = [True, True, False], operator = "AND"
#
#     True AND True -> True
#     True AND False -> False
#     return False
#
#     booleans = [True, True, False], operator = "OR"
#
#     True OR True -> True
#     True OR False -> True
#     return True
#
#     booleans = [True, True, False], operator = "XOR"
#
#     True XOR True -> False
#     False XOR False -> False
#     return False
#
# Input
#
#     an array of Boolean values (1 <= array_length <= 50)
#     a string specifying a logical operator: "AND", "OR", "XOR"
#
# Output
#
# A Boolean value (True or False).


from functools import reduce


def logical_calc(array, op):
    if op == "AND":
        return all(array)
    elif op == "OR":
        return any(array)
    elif op == "XOR":
        return reduce(lambda x, y: x ^ y, array)


if __name__ == '__main__':
    print(logical_calc())


# Best solutions:


def logical_calc(array, op):
    res = array[0]
    for x in array[1:]:
        if op == "AND":
            res &= x
        elif op == "OR":
            res |= x
        else:
            res ^= x

    return res  # boolean


def logical_calc(array, op):
    ops = {
        "AND": lambda x, y: x & y,
        "OR": lambda x, y: x | y,
        "XOR": lambda x, y: x ^ y
    }

    from functools import reduce
    return reduce(ops[op], array)
