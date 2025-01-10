# Wolves have been reintroduced to Great Britain. You are a sheep farmer, and
# are now plagued by wolves which pretend to be sheep. Fortunately, you are
# good at spotting them.
#
# Warn the sheep in front of the wolf that it is about to be eaten. Remember
# that you are standing at the front of the queue which is at the end of the
# array:
#
# [sheep, sheep, sheep, sheep, sheep, wolf, sheep, sheep]      (YOU ARE HERE
# AT THE FRONT OF THE QUEUE)
#    7      6      5      4      3            2      1
#
# If the wolf is the closest animal to you, return "Pls go away and stop eating
# my sheep". Otherwise, return "Oi! Sheep number N! You are about to be eaten
# by a wolf!" where N is the sheep's position in the queue.
#
# Note: there will always be exactly one wolf in the array.
# Examples
#
# Input: ["sheep", "sheep", "sheep", "wolf", "sheep"]
# Output: "Oi! Sheep number 1! You are about to be eaten by a wolf!"
#
# Input: ["sheep", "sheep", "wolf"]
# Output: "Pls go away and stop eating my sheep"


def warn_the_sheep(queue):
    wolf_index = queue[::-1].index('wolf')
    if wolf_index == 0:
        return "Pls go away and stop eating my sheep"
    else:
        return (f"Oi! Sheep number {wolf_index}! You are about to be eaten by "
                f"a wolf!")


if __name__ == '__main__':
    print(warn_the_sheep(['sheep', 'wolf', 'sheep']))


# Best solutions:


def warn_the_sheep(queue):
    n = len(queue) - queue.index('wolf') - 1
    return f'Oi! Sheep number {n}! You are about to be eaten by a wolf!' if n else 'Pls go away and stop eating my sheep'


def warn_the_sheep(queue):
    queue.reverse()
    return 'Pls go away and stop eating my sheep' if queue[0] == 'wolf' else 'Oi! Sheep number {}! You are about to be eaten by a wolf!'.format(queue.index('wolf'))
