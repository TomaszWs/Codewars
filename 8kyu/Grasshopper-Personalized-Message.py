# Create a function that gives a personalized greeting. This function takes two
# parameters: name and owner.
#
# Use conditionals to return the proper message:
# case 	return
# name equals owner 	'Hello boss'
# otherwise 	'Hello guest'


def greet(name, owner):
    return "Hello boss" if name == owner else "Hello guest"


name = "Daniel"
owner = "Bill"
print(greet(name,owner))


# Best solutions:


def greet(name, owner):
    return "Hello {}".format("boss" if name == owner else "guest")


def greet(name, owner):
    return f"Hello {'boss' if name == owner else 'guest'}"
