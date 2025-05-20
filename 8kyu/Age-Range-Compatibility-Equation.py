# Everybody knows the classic "half your age plus seven" dating rule that a lot
# of people follow (including myself). It's the 'recommended' age range in
# which to date someone.
#
#     Min=Age2+7\text{Min} = \dfrac{ \text{Age} } {2} + 7Min=2Age​+7
#
#     Max=2⋅(Age - 7)\text{Max} = 2 \cdot (\text{Age - 7})Max=2⋅(Age - 7)
#
#     Minimum age≤Your age≤Maximum age\text{Minimum age} \le \text{Your age}
#     \le \text{Maximum age}Minimum age≤Your age≤Maximum age
#
# Task
#
# Given an integer (1 <= n <= 100) representing a person's age, return their
# minimum and maximum age range.
#
# This equation doesn't work when the age <= 14, so if the age <= 14, use this
# equation instead:
#
# min = age - 0.10 * age
# max = age + 0.10 * age
#
# You should floor all your answers so that an integer is given instead of a
# float (which doesn't represent age). Return your answer in the form
# "[min]-[max]"
# Examples:
#
# age = 27   =>   "20-40"
# age = 5    =>   "4-5"
# age = 17   =>   "15-20"


from math import floor


def dating_range(age):
    if age <= 14:
        min_age = floor(age * 0.9)
        max_age = floor(age * 1.1)
    else:
        min_age = floor(age / 2 + 7)
        max_age = floor(2 * (age - 7))
    return f"{min_age}-{max_age}"


if __name__ == '__main__':
    print(dating_range(17))


# Best solutions:


def dating_range(age):
    if age <= 14:
        min = age - 0.10 * age
        max = age + 0.10 * age
    else:
        min = (age / 2) + 7
        max = (age - 7) * 2
    return str(int(min)) + '-' + str(int(max))


def dating_range(age):
  return f'{int(age/2+7)}-{(age-7)*2}' if age > 14 else \
      f'{int(0.9*age)}-{int(1.1*age)}'
