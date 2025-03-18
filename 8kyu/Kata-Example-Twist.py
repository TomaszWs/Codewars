# This is an easy twist to the example kata (provided by Codewars when learning
# how to create your own kata).
#
# Add the value "codewars" to the array websites 1,000 times.


websites = ["codewars"] * 1000


# Best solutions:


websites = ['codewars' for _ in range(1000)]


websites = []
for index in range(0,1000):
    websites.append("codewars")
