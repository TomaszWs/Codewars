# Intro
#
# There's a common mnemonic given to those learning English spelling
# which goes:
#
#     I before E except after C
#
# This suggests that when you have the letters i and e next to each
# other in a word, the i should come first, with the exception that if
# preceding the two vowels is the letter c in which case the e should
# go first.
#
# For example, this rule would tell you that the word for a close
# companion would be "friend" and not "freind". For the c case, this
# means that when a package is mailed to you, you will "receive" it
# rather than "recieve" it.
#
# However, besides being incorrect for many cases (my weird foreign
# scientist neighbor taught me a few examples), it's not clear from
# this rule what to do with more unusual cases with multiple is
# and es.
#
# For the purposes of this kata our rule will be:
#
#     For any contiguous sequence of i or e characters, all the is
#     should come before all the es. If, however, the sequence is
#     immediately preceeded by a c, all the es should come before all
#     the is.
#
# Task
#
# Write a function which takes in a lowercase word and applies our
# version of the "I before E except after C" rule.
# Examples
#
# "freind" --> "friend"
# "friend" --> "friend"
# "recieve" --> "receive"
#
# You'll also need to account for the weirder cases that may not exist
# in real English words.
#
# "eeiie" --> "iieee"
# "cieee" --> "ceeei"
# "eiicieeceie" --> "iieceeiceei"


import re


def i_before_e(s):
    def fix(m):
        seq = m.group()
        i_cnt = seq.count('i')
        e_cnt = seq.count('e')
        before_c = m.start() > 0 and s[m.start()-1] == 'c'
        return ('e'*e_cnt + 'i'*i_cnt) if before_c else ('i'*i_cnt + 'e'*e_cnt)
    return re.sub(r'[ie]+', fix, s)


if __name__ == '__main__':
    print(i_before_e('freind'))


# Best solutions:


from re import sub


def i_before_e(s):
    return sub(r'c?[ie]+', lambda g: ''.join(sorted(g[0], reverse=not g[0].startswith('c'))), s)


import re


def i_before_e(word):
    def replacer(match):
        seq = match.group(0)
        prefix = match.group(1)
        chars = seq.lstrip('c')
        if prefix == 'c':
            return prefix + ''.join(sorted(chars, key=lambda ch: 0 if ch == 'e' else 1))
        else:
            return prefix + ''.join(sorted(chars, key=lambda ch: 0 if ch == 'i' else 1))

    return re.sub(r'(c?)([ie]{2,})', replacer, word)


import re
i_before_e=lambda s:re.sub("c?[ei]+",lambda a:''.join(sorted(a[0],reverse=a[0]>"d")),s)
