# Write function bmi that calculates body mass index (bmi = weight / height2).
#
# if bmi <= 18.5 return "Underweight"
#
# if bmi <= 25.0 return "Normal"
#
# if bmi <= 30.0 return "Overweight"
#
# if bmi > 30 return "Obese"


def bmi(weight, height):
    bmi = weight/(height**2)
    if bmi <= 18.5: return "Underweight"
    elif bmi <= 25.0: return "Normal"
    elif bmi <= 30.0: return "Overweight"
    elif bmi > 30: return "Obese"


weight = 105
height = 2.3
result = bmi(weight, height)
print(result)


# Best solutions


def bmi(weight, height):
    b = weight / height ** 2
    return ['Underweight', 'Normal', 'Overweight', 'Obese'][(b > 30) + (b > 25) + (b > 18.5)]


def bmi(weight, height):
    bmi = weight / height ** 2
    return 'Underweight' if bmi <= 18.5 else 'Normal' if bmi <= 25.0 else 'Overweight' if bmi <= 30.0 else "Obese"