# Implement a function that adds two numbers together and returns their sum in binary. The conversion can be done before, or after the addition.

# The binary number returned should be a string.

# Examples:(Input1, Input2 --> Output (explanation)))

# 1, 1 --> "10" (1 + 1 = 2 in decimal or 10 in binary)
# 5, 9 --> "1110" (5 + 9 = 14 in decimal or 1110 in binary)

# My solution

def add_binary(a,b):
    c = bin(a+b)
    z = list(c)
    y = ''.join(z[2:])
    return y

a = 5
b = 9
print(add_binary(a,b))

# Best practices

def add_binary(a,b):
    return bin(a+b)[2:]

def add_binary(a,b):
    return '{0:b}'.format(a + b)