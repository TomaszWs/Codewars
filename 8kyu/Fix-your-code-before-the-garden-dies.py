# You have an award-winning garden and every day the plants need exactly 40mm
# of water. You created a great piece of JavaScript to calculate the amount of
# water your plants will need when you have taken into consideration the amount
# of rain water that is forecast for the day. Your jealous neighbour hacked
# your computer and filled your code with bugs.
#
# Your task is to debug the code before your plants die!


def rain_amount(mm):
    if mm < 40:
        return f"You need to give your plant {40 - mm} mm of water"
    else:
        return "Your plant has had more than enough water for today!"


if __name__ == '__main__':
    print(rain_amount(100))
