# Philip's just turned four and he wants to know how old he will be in various
# years in the future such as 2090 or 3044. His parents can't keep up
# calculating this so they've begged you to help them out by writing a
# programme that can answer Philip's endless questions.
#
# Your task is to write a function that takes two parameters: the year of birth
# and the year to count years in relation to. As Philip is getting more curious
# every day he may soon want to know how many years it was until he would be
# born, so your function needs to work with both dates in the future and in the
# past.
#
# Provide output in this format: For dates in the future: "You are ... year(s)
# old." For dates in the past: "You will be born in ... year(s)." If the year
# of birth equals the year requested return: "You were born this very year!"
#
# "..." are to be replaced by the number, followed and proceeded by a single
# space. Mind that you need to account for both "year" and "years", depending
# on the result.
#
# Good Luck!


def calculate_age(year_of_birth, current_year):
    if current_year == year_of_birth:
        return "You were born this very year!"
    elif current_year < year_of_birth:
        if year_of_birth - current_year == 1:
            return f"You will be born in {year_of_birth - current_year} year."
        else:
            return f"You will be born in {year_of_birth - current_year} years."
    elif current_year > year_of_birth:
        if current_year - year_of_birth == 1:
            return f"You are {current_year - year_of_birth} year old."
        else:
            return f"You are {current_year - year_of_birth} years old."


if __name__ == '__main__':
    print(calculate_age(2011, 2012))


# Best solutions:


def calculate_age(year_of_birth, current_year):
    diff = abs(current_year - year_of_birth)
    plural = '' if diff == 1 else 's'
    if year_of_birth < current_year:
        return 'You are {} year{} old.'.format(diff, plural)
    elif year_of_birth > current_year:
        return 'You will be born in {} year{}.'.format(diff, plural)
    return 'You were born this very year!'


def calculate_age(year_of_birth, current_year):
    age = current_year - year_of_birth
    if age == 0:
       return "You were born this very year!"
    elif age > 0:
       return "You are {} year{} old.".format(age, 's' if age > 1 else '')
    else:
       return "You will be born in {} year{}.".format(abs(age), 's' if abs(age) > 1 else '')


def calculate_age(year_of_birth, current_year):
    """There is no need to complicate matters"""
    delta = current_year - year_of_birth
    if delta < -1:
        return f"You will be born in {abs(delta)} years."
    elif delta == -1:
        return f"You will be born in 1 year."
    elif delta == 0:
        return "You were born this very year!"
    elif delta == 1:
        return "You are 1 year old."
    elif delta > 1:
        return f"You are {delta} years old."
    return None
