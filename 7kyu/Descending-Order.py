# Your task is to make a function that can take any non-negative integer as 
# an argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.
# Examples:

# Input: 42145 Output: 54421

# Input: 145263 Output: 654321

# Input: 123456789 Output: 987654321

# My solution

def descending_order(num):
    y = str(num)
    z = list(y)
    z.sort(reverse=True)
    x = int(''.join(z))
    return x

num_1 = 42145
num_2 = 145263
num_3 = 123456789
num_4 = 0
x = descending_order(num_4)
print(x)

# Best practices

def Descending_Order(num):
    return int("".join(sorted(str(num), reverse=True)))

def Descending_Order(num):
    if isinstance(num, int) and num >= 0:
        return int(''.join(sorted(str(num),reverse=True)))
    else:
        raise ValueError('Non-negative integer expected')