# Our football team has finished the championship.
#
# Our team's match results are recorded in a collection of strings. Each match
# is represented by a string in the format "x:y", where x is our team's score
# and y is our opponents score.
#
# For example: ["3:1", "2:2", "0:1", ...]
#
# Points are awarded for each match as follows:
#
#     if x > y: 3 points (win)
#     if x < y: 0 points (loss)
#     if x = y: 1 point (tie)
#
# We need to write a function that takes this collection and returns the number
# of points our team (x) got in the championship by the rules given above.
#
# Notes:
#
#     our team always plays 10 matches in the championship
#     0 <= x <= 4
#     0 <= y <= 4


def points(games):
    # score = 0
    # for i in games:
    #     if i[0] > i[2]:
    #         score += 3
    #     elif i[0] == i[2]:
    #         score += 1
    # return score
    return sum(3 if x > y else 1 if x == y else 0 for x, y in (map(int, i.split(":")) for i in games))


if __name__ == '__main__':
    print(points(['1:0','2:0','3:0','4:0','2:1','3:1','4:1','3:2','4:2','4:3']))


# Best solutions:


def points(games):
    count = 0
    for score in games:
        res = score.split(':')
        if res[0]>res[1]:
            count += 3
        elif res[0] == res[1]:
            count += 1
    return count


def points(games):
    result = 0
    for item in games:
	    result += 3 if item[0] > item[2] else 0
	    result += 1 if item[0] == item[2] else 0
    return result


def points(a):
    return sum((x >= y) + 2 * (x > y) for x, y in (s.split(":") for s in a))


def points(games):
	return sum([0,1,3][1+(g[0]>g[2])-(g[0]<g[2])] for g in games)
