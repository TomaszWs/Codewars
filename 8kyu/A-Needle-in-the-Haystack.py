# Can you find the needle in the haystack?

# Write a function findNeedle() that takes an array full of junk but containing one "needle"

# After your function finds the needle it should return a message (as a string) that says:

# "found the needle at position " plus the index it found the needle, so:

# Example(Input --> Output)

# ["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"] --> "found the needle at position 5" 

# Note: In COBOL, it should return "found the needle at position 6"

# My solution

def find_needle(haystack):
    for i in haystack:
        if i == 'needle': return f'found the needle at position {haystack.index(i)}'

haystack = ["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"]
print(find_needle(haystack))

# Best practices

def find_needle(haystack): return 'found the needle at position %d' % haystack.index('needle')

def find_needle(haystack):
    return f'found the needle at position {haystack.index("needle")}'