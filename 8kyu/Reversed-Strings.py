# Complete the solution so that it reverses the string passed into it.

# 'world'  =>  'dlrow'
# 'word'   =>  'drow'

# My solution

# def solution(string):
#     string_l = list(string)
#     string_l.reverse()
#     x = ''.join(string_l)
#     return x

# string1 = 'world'
# string2 = 'word'

# print(solution(string2))

# Best practices

def solution(str):
  return str[::-1]