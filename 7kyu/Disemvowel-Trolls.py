# Trolls are attacking your comment section!

# A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.

# Your task is to write a function that takes a string and return a new string with all vowels removed.

# For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".

# Note: for this kata y isn't considered a vowel.

# My solution

def disemvowel(string_):
    string_l = []
    for i in string_:
        if i not in 'AaEeIiUuOo': string_l.append(i)
    return ''.join(string_l)

string_ = 'This website is for losers LOL!'
print(disemvowel(string_))

# Best practices

def disemvowel(string):
    return "".join(c for c in string if c.lower() not in "aeiou")

def disemvowel(s):
    for i in "aeiouAEIOU":
        s = s.replace(i,'')
    return s