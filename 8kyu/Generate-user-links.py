# Generate user links
#
# Your task is to create userlinks for the url, you will be given a username
# and must return a valid link.
# Example
#
# generate_link('matt c')
# http://www.codewars.com/users/matt%20c
#
# reference
#
# use this as a reference encoding


from urllib.parse import quote


def generate_link(user):
    return f"http://www.codewars.com/users/{quote(user)}"


if __name__ == '__main__':
    print(generate_link('matt c'))
