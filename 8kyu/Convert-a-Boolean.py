# Implement a function which convert the given boolean value into its string representation.

# Note: Only valid inputs will be given.

# My solution
def boolean_to_string(b):
    return str(b)

b = bool(input('Enter something: '))
print(boolean_to_string(b))

# Best practices

def boolean_to_string(b):
    return 'True' if b else 'False'

def boolean_to_string(b):
    if b:
        return "True"
    return "False"