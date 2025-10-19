# Story
#
# A new task has come up in your team. An internal system needs to be
# able to check whether a number is a palindrome or not. You have been
# assigned the task to write the function, while the senior software
# engineer Bob wrote the tests. But when you try to write the
# function, you can't make it pass the tests as you expect! And worse
# still, Bob has gone on holiday! Maybe he slightly changed the
# meaning of "palindrome" in this task? Can you work out how to make
# the function work correctly?
# Examples
#
#  585  -->  True
# 1497  -->  False
#  891  -->  True
# 1001  -->  False
#
# Bob said it should work for really really big numbers.
#
# Good luck!


def is_palindrome(n: int) -> bool:
    r = bin(n)[2:]
    return r == r[::-1]


if __name__ == '__main__':
    print(is_palindrome(1001))


# Best solutions:


def is_palindrome(n: int) -> bool:
    return (s := f"{n:b}") == s[::-1]


def is_palindrome(n: int) -> bool:
    num = "{0:b}".format(n)

    left = 0
    right = len(num) - 1

    while left < right:
        if num[left] != num[right]:
            return False

        left += 1
        right -= 1

    return True


def is_palindrome(n):
    len = n.bit_length()
    return all(n>>i&1 == n>>len+~i&1 for i in range(len))
