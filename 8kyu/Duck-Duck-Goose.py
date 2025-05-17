# The objective of Duck, duck, goose is to walk in a circle, tapping on each
# player's head until one is chosen.
#
# Task:
#
# Given an array of Player objects and a position (first position is 1), return
# the name of the chosen Player.
# name is a property of Player objects, e.g Player.name
#
# Example:
#
# duck_duck_goose([a, b, c, d], 1) should return a.name
# duck_duck_goose([a, b, c, d], 5) should return a.name
# duck_duck_goose([a, b, c, d], 4) should return d.name
#
# Random input limits:
#
#     6≤Players≤506 \le \text{Players} \le 506≤Players≤50
#     5000≤Position≤500005000 \le \text{Position} \le 500005000≤Position≤50000


from dataclasses import dataclass


@dataclass
class Player:
    name: str


players = [Player(name) for name in "abcdcefghz"]


def duck_duck_goose(players, goose):
    return players[(goose - 1) % len(players)].name


if __name__ == '__main__':
    print(duck_duck_goose(players, 1))


# Best solutions:


def duck_duck_goose(players, goose):
    return players[(goose % len(players)) - 1].name


def duck_duck_goose(players, goose):
  idx = (goose-1) % len(players)
  return players[idx].name
