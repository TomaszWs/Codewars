# Rock Paper Scissors
#
# Let's play! You have to return which player won! In case of a draw
# return Draw!.
#
# Examples(Input1, Input2 --> Output):
#
# "scissors", "paper" --> "Player 1 won!"
# "scissors", "rock" --> "Player 2 won!"
# "paper", "paper" --> "Draw!"
#
# rockpaperscissors


def rps(p1, p2):
    if p1 == p2:
        return "Draw!"
    elif (p1 == "scissors" and p2 == "paper") or (p1 == "rock" and p2 == "scissors") or (p1 == "paper" and p2 == "rock"):
        return "Player 1 won!"
    elif (p2 == "scissors" and p1 == "paper") or (p2 == "rock" and p1 == "scissors") or (p2 == "paper" and p1 == "rock"):
        return "Player 2 won!"


print(rps("paper", "paper"))


# Best solutions:


def rps(p1, p2):
    beats = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}
    if beats[p1] == p2:
        return "Player 1 won!"
    if beats[p2] == p1:
        return "Player 2 won!"
    return "Draw!"


def rps(p1, p2):
    hand = {'rock':0, 'paper':1, 'scissors':2}
    results = ['Draw!', 'Player 1 won!', 'Player 2 won!']
    return results[hand[p1] - hand[p2]]


def rps(p1, p2):
    if p1 == p2:
        return 'Draw!'
    elif (p1 == 'rock' and p2 == 'scissors') or (
            p1 == 'scissors' and p2 == 'paper') or (
            p1 == 'paper' and p2 == 'rock'):
        return 'Player 1 won!'
    else:
        return 'Player 2 won!'
