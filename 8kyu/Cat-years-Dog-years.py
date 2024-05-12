# Kata Task
#
# I have a cat and a dog.
#
# I got them at the same time as kitten/puppy. That was humanYears years ago.
#
# Return their respective ages now as [humanYears,catYears,dogYears]
#
# NOTES:
#
#     humanYears >= 1
#     humanYears are whole numbers only
#
# Cat Years
#
#     15 cat years for first year
#     +9 cat years for second year
#     +4 cat years for each year after that
#
# Dog Years
#
#     15 dog years for first year
#     +9 dog years for second year
#     +5 dog years for each year after that
#
# References
#
#     http://www.catster.com/cats-101/calculate-cat-age-in-cat-years
#     http://www.slate.com/articles/news_and_politics/explainer/2009/05/a_dogs_life.html


def human_years_cat_years_dog_years(human_years):
    if human_years == 1:
        cat_years = 15
        dog_years = 15
    elif human_years == 2:
        cat_years = 24
        dog_years = 24
    else:
        cat_years = 24 + (human_years-2)*4
        dog_years = 24 + (human_years-2)*5
    return [human_years,cat_years,dog_years]


print(human_years_cat_years_dog_years(10))


# Best solutions:


def human_years_cat_years_dog_years(human_years):
    catYears = 0
    dogYears = 0
    if human_years == 1:
        catYears += 15
        dogYears += 15
        return [human_years, catYears, dogYears]
    elif human_years == 2:
        catYears += 24
        dogYears += 24
        return [human_years, catYears, dogYears]
    elif human_years > 2:
        catYears += 24
        dogYears += 24
        years = human_years - 2
        catYears += years*4
        dogYears += years*5
        return [human_years, catYears, dogYears]
    return [0,0,0]


def human_years_cat_years_dog_years(n):
    cat_years = 15 + (9 * (n > 1)) + (4 * (n - 2) * (n > 2))
    dog_years = 15 + (9 * (n > 1)) + (5 * (n - 2) * (n > 2))
    return [n, cat_years, dog_years]


def human_years_cat_years_dog_years(x):
    return [x, 24+(x-2)*4 if (x != 1) else 15, 24+(x-2)*5 if (x != 1) else 15]