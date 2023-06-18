# Create a function which answers the question "Are you playing banjo?".
# If your name starts with the letter "R" or lower case "r", you are playing banjo!

# The function takes a name as its only argument, and returns one of the following strings:

# name + " plays banjo" 
# name + " does not play banjo"

# Names given are always valid strings.

# My solution
import re
def are_you_playing_banjo(name): 
    if re.search("^r", name) or re.search("^R", name): return name + " plays banjo"
    else: return name + " does not play banjo"

name = 'Robert'
name2 = 'rabbit'
name3 = 'Adam'

print(are_you_playing_banjo(name3))

# Best practices

def areYouPlayingBanjo(name):
    if name[0].lower() == 'r':
        return name + ' plays banjo'
    else:
        return name + ' does not play banjo'
    
def areYouPlayingBanjo(name):
    return name + (' plays' if name[0].lower() == 'r' else ' does not play') + " banjo";