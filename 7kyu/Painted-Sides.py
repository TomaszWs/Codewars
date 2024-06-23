# Task
#
# You are given a big cube, made up of several little cubes. You paint the
# outside of the big cube and are now supposed to find out how many of the
# little cubes have zero faces painted, one face painted, two faces painted, etc.
#
# Write a function which accepts two parameters:
#
#     length: the side length of the big cube (in little cubes),
#     0 <= length <= 50
#     n: the number of faces painted, 0 <= n <= 7
#
# You have to figure out how many of the little cubes have n faces painted.
# Example
#
# painted_faces(4,3)
#
# => result: 8  # Only the vertices of the big cube will have three faces
# painted
#
# If n > 3 then return 0 as it is not possible for a painted cube to have more
# than 3 sides painted (unless s == 1, in that case it will have 6 faces
# painted).


def painted_faces(length, n):
    if n == 6:
        return 1 if length == 1 else 0
    if n == 0:
        return (length - 2) ** 3 if length > 2 else 0
    if n == 1:
        return 6 * (length - 2) ** 2 if length > 2 else 0
    if n == 2:
        return 12 * (length - 2) if length > 2 else 0
    if n == 3:
        return 8 if length > 1 else 0
    return 0


if __name__ == "__main__":
    print(painted_faces(1, 3))


# Best solutions:


def painted_faces(sides,n):
    if sides == 0 :
        return 0;
    elif sides == 1 :
        if n == 6:
            return 1;
        else:
            return 0;
    else:
        if n == 0:
            return (sides-2)**3;     # inside cubes
        elif n == 1:
            return 6 * (sides-2)**2; # face cubes
        elif n == 2:
            return 12 * (sides-2);   # rib cubes
        elif n == 3:
            return 8;                # corner cubes
        else:
            return 0;


def painted_faces(length, n):
    if length == 1:  return int(n == 6)
    s = length - 2
    return {
        0:    s**3,
        1:  6*s**2,
        2: 12*s,
        3:  8,
    }.get(n, 0)


def painted_faces(s, n):
    if not s: return 0

    if s == 1: return int(n == 6)

    match n:
        case 0:
            return s * s * s - ((s - 1) * (s - 1) * 6 + 2)
        case 1:
            return ((s - 1) * (s - 1) * 6 + 2) - ((s - 2) * 12) - 8
        case 2:
            return (s - 2) * 12
        case 3:
            return 8
        case _:
            return 0
    return "ejini战神's solution!!!"


def painted_faces(length, n):
    match n:
        case 0 if length >= 3: return (length - 2) ** 3
        case 1 if length >= 3: return (length - 2) ** 2 * 6
        case 2 if length >= 3: return (length - 2) * 12
        case 3 if length >= 2: return 8
        case 6 if length == 1: return 1
    return 0
