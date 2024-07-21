# You are given a method called main, make it print the line Hello World!,
# (yes, that includes a new line character at the end) and don't return
# anything
#
# Note that for some languages, the function main is the entry point of the
# program.
#
# Here's how it will be tested:
#
#     Solution.main("parameter1", "parameter2","parametern")
#
# Hints:
#
#     Check your references
#     Think about the scope of your method
#     If you still don't get it probably you can define main as an attribute of
#     the Solution class that accepts a single argument, and that only prints
#     "Hello World!" without any return.


class Solution:
    def main(*args):
        print("Hello World!")


if __name__ == "__main__":
    Solution.main("parameter1", "parameter2", "parametern")


# Best solutions:


class Solution:

    @staticmethod
    def main(self, *args):
        print("Hello World!")


class Solution:
    #your code here
    def main(self):
        print('Hello World!')


class Solution(object):

    @staticmethod
    def main(*_):
        print("Hello World!")