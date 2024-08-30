# You need to write a function that reverses the words in a given string. Words
# are always separated by a single space.
#
# As the input may have trailing spaces, you will also need to ignore
# unneccesary whitespace.
#
# Example (Input --> Output)
#
# "Hello World" --> "World Hello"
# "Hi There." --> "There. Hi"
#
# Happy coding!


def reverse(st):
    st2 = st.split()
    st2.reverse()
    return " ".join(st2)


if __name__ == '__main__':
    print(reverse("Hello World"))


# Best solutions:


def reverse(st):
    # Your Code Here
    return " ".join(st.split()[::-1])


def reverse(st):
    return " ".join(reversed(st.split())).strip()


def reverse(st):
    s = st.split()
    return ' '.join(s[::-1])
