# Grade book

# Complete the function so that it finds the average of the three scores passed to it and returns the letter value associated with that grade.
# Numerical Score 	Letter Grade
# 90 <= score <= 100 	'A'
# 80 <= score < 90 	'B'
# 70 <= score < 80 	'C'
# 60 <= score < 70 	'D'
# 0 <= score < 60 	'F'

# Tested values are all between 0 and 100. Theres is no need to check for negative values or values greater than 100.

# My solution

def get_grade(s1, s2, s3):
    average = (s1+s2+s3)/3
    print(average)
    if average >= 90:
        grade = 'A'
    elif average >= 80:
        grade = 'B'
    elif average >= 70:
        grade = 'C'
    elif average >= 60:
        grade = 'D'
    else:
        grade = 'F'
    return grade

s1 = float(input())
s2 = float(input())
s3 = float(input())
final_grade = get_grade(s1,s2,s3)
print('Final grade:',final_grade)

# Best practices

def get_grade(s1, s2, s3):
    m = (s1 + s2 + s3) / 3.0
    if 90 <= m <= 100:
        return 'A'
    elif 80 <= m < 90:
        return 'B'
    elif 70 <= m < 80:
        return 'C'
    elif 60 <= m < 70:
        return 'D'
    return "F"
    
def get_grade(s1, s2, s3):
    mean = sum([s1,s2,s3])/3
    if mean>=90: return 'A'
    if mean>=80: return 'B'
    if mean>=70: return 'C'
    if mean>=60: return 'D'
    return 'F'
    