# Disclaimer
#
# This kata is in accordance with the EPIC challenge in relation to Andela's
# 10 year anniversary celebration. You can find more info here
# Story
#
# ejini战神 has recently quit his programming job and is now opting in for a
# career change. He has decided to settle in the baking industry and is now a
# worker of a cake franchise designated for wedding celebrations. He has come
# up with a creative wedding cake model and a unique box that can modify the
# cake in a certain way that can blow away all the attendees!!! (How cool is
# that~ 😏)
# Task
#
# Given the cake model, your job is to help ejini战神 write a program that can
# instantly display the final visualization of the cake model after the unique
# box has been unfolded.
#
# Initial cake model below:
#
#     /|\
#    \/ \/
#   \ | | \
#   /\/\/\/
#  /       \
# /|||||||||\
#
# The final visualization:
#
#     /|\
#    \ | /
#   \  |  \
#   /  |  /
#  /   |   \
# /    |    \
#
# More examples:
#
#           \         \
#         // |||||||||\\/
#        \\\\\\\\\\\\\\\\\
#        / /| \ /\|\ /| |/
#     /||||||||\/| /\||||||\\
#
#     becomes
#
#           \    |    \
#         /      |      /
#        \       |       \
#        /       |       /
#     /          |          \
#
#        /         \
#        /         \
#        /         \
#        /         \
#        /         \
#        /         \
#
#     becomes
#
#        /    |    \
#        /    |    \
#        /    |    \
#        /    |    \
#        /    |    \
#        /    |    \
#
# Notes
#
#     Each cake model will have at least 1 layer (row), separated by a newline
#     character (\n)
#     Each layer will only consist of odd number of filling space
#     The lower layer will have equal or more filling space than the upper ones
#     Each layer will always start and end with / or \ fillings
#     Starting and ending position of each layer will not overlap
#     Inner fillings of the cake may be /, \ or |
#     Some part of the cake do not have fillings (due to the semi-functional
#     cake creation model...)
#     Trailing and leading spaces for the visualization above will not be
#     included in the cake model's input and final output.
#     \\ for visualization above only is considered as 2 fillings rather than
#     1.
#     Output should be the same as the given input except with all fillings of
#     each layer centralized whilst leaving a starting and ending filling to
#     prevent it from overflow ^^. (Refer to examples above)


def cake_visualizer(s):
    layers = s.split("\n")
    transformed_layers = []
    for layer in layers:
        if len(layer) <= 2:
            transformed_layers.append(layer)
        else:
            start_char, end_char = layer[0], layer[-1]
            new_layer = start_char + " " * (len(layer) - 2) + end_char
            middle_index = (len(layer) - 1) // 2
            new_layer = new_layer[:middle_index] + "|" + new_layer[
                                                         middle_index + 1:]
            transformed_layers.append(new_layer)
    return "\n".join(transformed_layers)


if __name__ == "__main__":
    print(cake_visualizer("/|\\\n\\/ \\/\n\\ | | \\\n/\\/\\/\\/\n/       "
                          "\\\n/|||||||||\\"))


# Best solutions:


cake_visualizer= lambda s:"\n".join(''.join([' ','|',d][(id==len(r)//2)+2*(id in [0,len(r)-1])] for id,d in enumerate(r)) for r in s.split("\n"))


def cake_visualizer(s):
    out = []
    for row in s.split("\n"):
        space = ' ' * (len(row) // 2 - 1)
        out.append(row[0] + space + '|' + space + row[-1])
    return '\n'.join(out)


def cake_visualizer(s):
    return '\n'.join(r[0] + ' '*(len(r)//2-1) + '|' + ' '*(len(r)//2-1) + r[-1] for r in s.split('\n'))


def cake_visualizer(s):
    s = s.split("\n")
    for i in range(len(s)):
        s[i] = s[i][0] + " " * (len(s[i])//2-1) + "|" + " " * (len(s[i])//2-1) + s[i][-1]
    return "\n".join(s)
