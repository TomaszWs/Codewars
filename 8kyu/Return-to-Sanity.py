# This function should return an object, but it's not doing what's intended.
# What's wrong?


def mystery():
    results = {'sanity': 'Hello'}
    return results


if __name__ == '__main__':
    print(mystery())


# Best solutions:


def mystery():
    return {'sanity': 'Hello'}
