# Create a combat function that takes the player's current health and the
# amount of damage received, and returns the player's new health. Health can't
# be less than 0.


def combat(health, damage):
    return health - damage if health - damage > 0 else 0


if __name__ == '__main__':
    print(combat(100, 5))


# Best solutions:


def combat(health, damage):
    return max(0, health-damage)


def combat(health, damage):
    return max(health - damage, 0)
