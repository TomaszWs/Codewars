# Define a method hello that returns "Hello, Name!" to a given name, or says
# Hello, World! if name is not given (or passed as an empty String).
#
# Assuming that name is a String and it checks for user typos to return a name
# with a first capital letter (Xxxx).
#
# Examples:
#
# * With `name` = "john"  => return "Hello, John!"
# * With `name` = "aliCE" => return "Hello, Alice!"
# * With `name` not given
#   or `name` = ""        => return "Hello, World!"


def hello(name = None):
    if name == "" or name is None:
        return "Hello, World!"
    else:
        return f"Hello, {name[0].upper() + name[1:].lower()}!"


if __name__ == '__main__':
    print(hello("alICE"))


# Best solutions:


def hello(name=''):
    return f"Hello, {name.title() or 'World'}!"


def hello(name=""):
    return f"Hello, {name.capitalize() if name else 'World'}!"


def hello(name=None):
    if not name:
        return "Hello, World!"
    return "Hello, %s!"%(name.capitalize())
