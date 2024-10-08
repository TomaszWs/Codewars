# Write function parse_float which takes a string/list and returns a number or
# 'none' if conversion is not possible.


def parse_float(string):
    try:
        if isinstance(string, list):
            [float(i) for i in string]
        else:
            return float(string)
    except ValueError:
        return None


if __name__ == '__main__':
    print(parse_float("1.0"))


# Best solutions:


def parse_float(string):
    try:
        return float(string)
    except:
        return None


def parse_float(string):
    try:
        return float(string)
    except (ValueError, TypeError):
        return None
