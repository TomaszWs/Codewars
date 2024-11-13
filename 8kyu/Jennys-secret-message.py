# Jenny has written a function that returns a greeting for a user. However,
# she's in love with Johnny, and would like to greet him slightly different.
# She added a special case to her function, but she made a mistake.
#
# Can you help her?


def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    else:
        return f"Hello, {name}!"


if __name__ == '__main__':
    print(greet("Johnny"))


# Best solutions:


def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return "Hello, {name}!".format(name=name)


def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    else:
    	return "Hello, {name}!".format(name=name)def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    else:
    	return "Hello, {name}!".format(name=name)


def greet(name):
    return "Hello, my love!" if name == 'Johnny' else "Hello, {name}!".format(name=name)
