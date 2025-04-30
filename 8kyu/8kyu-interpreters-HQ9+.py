# You task is to implement an simple interpreter for the notorious esoteric
# language HQ9+ that will work for a single character input:
#
#     If the input is 'H', return 'Hello World!'
#     If the input is 'Q', return the input
#     If the input is '9', return the full lyrics of 99 Bottles of Beer. It
#     should be formatted like this:
#
# 99 bottles of beer on the wall, 99 bottles of beer.
# Take one down and pass it around, 98 bottles of beer on the wall.
# 98 bottles of beer on the wall, 98 bottles of beer.
# Take one down and pass it around, 97 bottles of beer on the wall.
# 97 bottles of beer on the wall, 97 bottles of beer.
# Take one down and pass it around, 96 bottles of beer on the wall.
# ...
# ...
# ...
# 2 bottles of beer on the wall, 2 bottles of beer.
# Take one down and pass it around, 1 bottle of beer on the wall.
# 1 bottle of beer on the wall, 1 bottle of beer.
# Take one down and pass it around, no more bottles of beer on the wall.
# No more bottles of beer on the wall, no more bottles of beer.
# Go to the store and buy some more, 99 bottles of beer on the wall.
#
#     For everything else, don't return anything (return null in C#, None in
#     Rust, and "" in Haskell).
#
# (+ has no visible effects so we can safely ignore it.)


def HQ9(code):
    if code == 'H':
        return 'Hello World!'
    elif code == 'Q':
        return 'Q'
    elif code == '9':
        lyrics = []
        for i in range(99, 0, -1):
            bottle = 'bottle' if i == 1 else 'bottles'
            next_i = i - 1
            next_bottle = 'bottle' if next_i == 1 else 'bottles'
            if next_i == 0:
                next_line = "no more bottles of beer on the wall."
            else:
                next_line = f"{next_i} {next_bottle} of beer on the wall."

            lyrics.append(
                f"{i} {bottle} of beer on the wall, {i} {bottle} of beer.")
            lyrics.append(f"Take one down and pass it around, {next_line}")
        lyrics.append(
            "No more bottles of beer on the wall, no more bottles of beer.")
        lyrics.append(
            "Go to the store and buy some more, 99 bottles of beer on "
            "the wall.")
        return "\n".join(lyrics)
    else:
        return None


if __name__ == '__main__':
    print(HQ9('H'))


# Best solutions:


LINES = "{0} of beer on the wall, {0} of beer.\nTake one down and pass it around, {1} of beer on the wall."
SONG = '\n'.join( LINES.format("{} bottles".format(n), "{} bottle".format(n-1)+"s"*(n!=2)) for n in range(99,1,-1) )
SONG += """
1 bottle of beer on the wall, 1 bottle of beer.
Take one down and pass it around, no more bottles of beer on the wall.
No more bottles of beer on the wall, no more bottles of beer.
Go to the store and buy some more, 99 bottles of beer on the wall."""


def HQ9(code):
    return {'H': 'Hello World!', 'Q': 'Q', '9': SONG}.get(code, None)


def HQ9(code):
    if code == "H":
        return "Hello World!"
    if code == "Q":
        return "Q"
    if code == "9":
        result = ""
        for n in range(99,2,-1):
            result += f"{n} bottles of beer on the wall, {n} bottles of beer.\nTake one down and pass it around, {n-1} bottles of beer on the wall.\n"
        result += "2 bottles of beer on the wall, 2 bottles of beer.\nTake one down and pass it around, 1 bottle of beer on the wall.\n1 bottle of beer on the wall, 1 bottle of beer.\nTake one down and pass it around, no more bottles of beer on the wall.\nNo more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, 99 bottles of beer on the wall."
        return result
    return None
