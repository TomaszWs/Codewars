# Finish the uefaEuro2016() function so it return string just like in the
# examples below:
#
# uefa_euro_2016(['Germany', 'Ukraine'],[2, 0]) # "At match Germany - Ukraine,
# Germany won!"
# uefa_euro_2016(['Belgium', 'Italy'],[0, 2]) # "At match Belgium - Italy,
# Italy won!"
# uefa_euro_2016(['Portugal', 'Iceland'],[1, 1]) # "At match Portugal -
# Iceland, teams played draw."


def uefa_euro_2016(teams, scores):
    if scores[0] > scores[1]:
        result = f"{teams[0]} won!"
    elif scores[0] < scores[1]:
        result = f"{teams[1]} won!"
    else:
        result = "teams played draw."
    return f"At match {teams[0]} - {teams[1]}, {result}"


if __name__ == '__main__':
    print(uefa_euro_2016(['Germany', 'Ukraine'], [2, 0]))


# Best solutions:


def uefa_euro_2016(teams, scores):
    return (f"At match {teams[0]} - {teams[1]}, "
            f"{'teams played draw.' if scores[0] == scores[1] 
            else teams[scores.index(max(scores))] + ' won!'}")


def uefa_euro_2016(teams, scores):
    s1, s2 = scores
    result = "teams played draw." if s1 == s2 else f"{teams[s1 < s2]} won!"
    return f"At match {teams[0]} - {teams[1]}, {result}"
