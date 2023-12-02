# Character recognition software is widely used to digitise printed texts.
# Thus the texts can be edited, searched and stored on a computer.
#
# When documents (especially pretty old ones written with a typewriter),
# are digitised character recognition softwares often make mistakes.
#
# Your task is correct the errors in the digitised text. You only have to
# handle the following mistakes:
#
#     S is misinterpreted as 5
#     O is misinterpreted as 0
#     I is misinterpreted as 1
#
# The test cases contain numbers only by mistake.


def correct(s):
    correct_s = []
    for char in s:
        if char == "5": correct_s.append("S")
        elif char == "0": correct_s.append("O")
        elif char == "1": correct_s.append("I")
        else: correct_s.append(char)
    return "".join(correct_s)


s = "L0nd0n"
print(correct(s))

# Best solutions:


def correct(string):
    return string.translate(str.maketrans("501", "SOI"))


def correct(string):
    return string.replace('1','I').replace('0','O').replace('5','S')


tr=str.maketrans('015','OIS')

def correct(string):
    return string.translate(tr)
