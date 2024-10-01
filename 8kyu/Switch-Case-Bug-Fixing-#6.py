# Switch/Case - Bug Fixing #6
#
# Oh no! Timmy's evalObject function doesn't work. He uses Switch/Cases to
# evaluate the given properties of an object, can you fix timmy's function?


def eval_object(v):
    operation = v["operation"]
    match operation:
        case "+":
            return v["a"] + v["b"]
        case "-":
            return v["a"] - v["b"]
        case "/":
            return v["a"] / v["b"]
        case "*":
            return v["a"] * v["b"]
        case "%":
            return v["a"] % v["b"]
        case "**":
            return v["a"] ** v["b"]
        case _:
            return 1


if __name__ == '__main__':
    print(eval_object({'a':1,'b':1,'operation':'+'}))


# Best solutions:


def eval_object(v):
    return {"+": v['a']+v['b'],
            "-": v['a']-v['b'],
            "/": v['a']/v['b'],
            "*": v['a']*v['b'],
            "%": v['a']%v['b'],
           "**": v['a']**v['b'], }.get(v['operation'])


def eval_object(v):
    return eval("{a}{operation}{b}".format(**v))


def eval_object(v):
    match v["operation"]:
        case "+":
            return v["a"] + v["b"]
        case "-":
            return v["a"] - v["b"]
        case "/":
            return v["a"] / v["b"]
        case "*":
            return v["a"] * v["b"]
        case "%":
            return v["a"] % v["b"]
        case "**":
            return v["a"] ** v["b"]
        case _:
            return 12
