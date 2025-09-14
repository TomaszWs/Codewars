# Oh no! Timmy hasn't followed instructions very carefully and forgot how to
# use the new String Template feature, Help Timmy with his string template so
# it works as he expects!


def build_string(*args):
    return "I like {}!".format(", ".join(args))


if __name__ == '__main__':
    print(build_string('Cheese','Milk','Chocolate'))


# Best solutions:


def build_string(*args):
    return f"I like {', '.join(args)}!"


def build_string(*args):
    return "I like {0}!".format(", ".join(args))
