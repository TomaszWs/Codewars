# You're writing code to control your town's traffic lights. You need a
# function to handle each change from green, to yellow, to red, and then to
# green again.
#
# Complete the function that takes a string as an argument representing the
# current state of the light and returns a string representing the state the
# light should change to.
#
# For example, when the input is green, output should be yellow.


def update_light(current):
    match current:
        case "green":
            return "yellow"
        case "red":
            return "green"
        case "yellow":
            return "red"

current = "green"
print(update_light(current))

# Best solutions:


def update_light(current):
    return {"green": "yellow", "yellow": "red", "red": "green"}[current]


def update_light(current):
    if current == "green":
        return "yellow"
    elif current == "yellow":
        return "red"
    elif current == "red":
        return "green"
    else:
        return "This is not a traffic light color."


def update_light(current):
    color = ['green', 'yellow', 'red']
    return color[(color.index(current)+1)%len(color)]