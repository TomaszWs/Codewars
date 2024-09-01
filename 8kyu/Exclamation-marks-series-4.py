# Description:
#
# Remove all exclamation marks from sentence but ensure a exclamation mark at the end of string. For a beginner kata, you can assume that the input data is always a non empty string, no need to verify it.
# Examples
#
# "Hi!"     ---> "Hi!"
# "Hi!!!"   ---> "Hi!"
# "!Hi"     ---> "Hi!"
# "!Hi!"    ---> "Hi!"
# "Hi! Hi!" ---> "Hi Hi!"
# "Hi"      ---> "Hi!"


from re import sub


def remove(st):
    return sub("!", "", st) + "!"


if __name__ == '__main__':
    print(remove("Hi!!!"))


# Best solutions:


def remove(s):
    return '{}!'.format(s.replace('!', ''))


def remove(s):
  return f'{s.replace("!", "")}!'
