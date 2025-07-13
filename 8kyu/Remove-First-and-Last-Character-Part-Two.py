# This is a spin off of my first kata.
#
# You are given a string containing a sequence of character sequences separated
# by commas.
#
# Write a function which returns a new string containing the same character
# sequences except the first and the last ones but this time separated by
# spaces.
#
# If the input string is empty or the removal of the first and last items would
# cause the resulting string to be empty, return an empty value (represented as
# a generic value NULL in the examples below).
# Examples
#
# "1,2,3"      =>  "2"
# "1,2,3,4"    =>  "2 3"
# "1,2,3,4,5"  =>  "2 3 4"
#
# ""     =>  NULL
# "1"    =>  NULL
# "1,2"  =>  NULL


def array(string):
    p = string.split(',')
    return ' '.join(p[1:-1]) if len(p) > 2 else None


if __name__ == '__main__':
    print(array('1,2,3,4'))


# Best solutions:


def array(strng):
    return ' '.join(strng.split(',')[1:-1]) or None


def array(s):
    r = ' '.join(s.split(',')[1:-1])
    return r if r else None
