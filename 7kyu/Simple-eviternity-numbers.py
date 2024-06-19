# An eviternity number is a number which:
#
#     contains only digits 8, 5 and 3, and
#     the count of the digit 8 >= count of digit 5 >= count of digit 3.
#
# The first few eviternity numbers are as follows.
#
# [8, 58, 85, 88, 358, 385, 538, 583, 588, 835, 853, 858, 885, 888]
#
# You will be given two integers, a and b, and your task is to return the
# number of eviternity numbers in the range >= a and < b.
#
# For example:
# a=0, b=1000 => 14, because they are [8, 58, 85, 88, 358, 385, 538, 583, 588,
# 835, 853, 858, 885, 888]
#
# The upper bound will not exceed 500,000.
#
# More examples in test cases. Good luck!


# def solve(a, b):
#     def eviternity(num):
#         count_8 = str(num).count('8')
#         count_5 = str(num).count('5')
#         count_3 = str(num).count('3')
#         return count_8 >= count_5 >= count_3 and all(digit in '853' for digit in str(num))
#     return len([num for num in range(a, b) if eviternity(num)])


# def solve(a, b):
#     return len([
#         num for num in range(a, b)
#         if str(num).count('8') >= str(num).count('5') >= str(num).count('3')
#         and all(digit in '853' for digit in str(num))
#     ])


from itertools import product


def solve(a, b):
    def is_eviternity(s):
        count_8 = s.count('8')
        count_5 = s.count('5')
        count_3 = s.count('3')
        return count_8 >= count_5 >= count_3

    def generate_eviternity_numbers():
        eviternity_numbers = set()
        max_length = len(str(500000))
        for length in range(1, max_length + 1):
            for combo in product('853', repeat=length):
                num_str = ''.join(combo)
                if is_eviternity(num_str):
                    eviternity_numbers.add(int(num_str))
        return sorted(eviternity_numbers)
    eviternity_numbers = generate_eviternity_numbers()
    count = sum(1 for num in eviternity_numbers if a <= num < b)
    return count


if __name__ == "__main__":
    print(solve(0, 1000))


# Best solutions:


u = [8, 58, 85, 88, 358, 385, 538, 583, 588, 835, 853, 858, 885, 888, 3588,
     3858, 3885, 5388, 5588, 5838, 5858, 5883, 5885, 5888, 8358, 8385, 8538,
     8558, 8583, 8585, 8588, 8835, 8853, 8855, 8858, 8885, 8888, 35588, 35858,
     35885, 35888, 38558, 38585, 38588, 38855, 38858, 38885, 53588, 53858,
     53885, 53888, 55388, 55838, 55883, 55888, 58358, 58385, 58388, 58538,
     58583, 58588, 58835, 58838, 58853, 58858, 58883, 58885, 58888, 83558,
     83585, 83588, 83855, 83858, 83885, 85358, 85385, 85388, 85538, 85583,
     85588, 85835, 85838, 85853, 85858, 85883, 85885, 85888, 88355, 88358,
     88385, 88535, 88538, 88553, 88558, 88583, 88585, 88588, 88835, 88853,
     88855, 88858, 88885, 88888, 335588, 335858, 335885, 338558, 338585,
     338855, 353588, 353858, 353885, 355388, 355838, 355883, 355888, 358358,
     358385, 358538, 358583, 358588, 358835, 358853, 358858, 358885, 358888,
     383558, 383585, 383855, 385358, 385385, 385538, 385583, 385588, 385835,
     385853, 385858, 385885, 385888, 388355, 388535, 388553, 388558, 388585,
     388588, 388855, 388858, 388885]

def solve(a, b):
    return sum(a <= x < b for x in u)


def solve(a,b):
    return len([num for num in range(a,b) if '0' not in str(num) and '1' not in
                str(num) and '2' not in str(num) and '4' not in str(num) and
                '6' not in str(num) and '7' not in str(num) and '9' not in
                str(num) and str(num).count('8') >= str(num).count('5') >=
                str(num).count('3')])


import itertools


def merge(l):
    return ''.join(l)


def solve(a, b):
    digits = ['3', '5', '8', '']
    c2 = set(map(merge,
                 itertools.product(digits, digits, digits, digits, digits,
                                   digits)))
    c2.remove('')
    c = 0
    for n in c2:
        if int(n) >= a and int(n) < b:
            if n.count('8') >= n.count('5') and n.count('5') >= n.count('3'):
                c += 1
    return c

