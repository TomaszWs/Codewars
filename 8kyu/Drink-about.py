#     Kids drink toddy.
#     Teens drink coke.
#     Young adults drink beer.
#     Adults drink whisky.
#
# Make a function that receive age, and return what they drink.
#
# Rules:
#
#     Children under 14 old.
#     Teens under 18 old.
#     Young under 21 old.
#     Adults have 21 or more.
#
# Examples: (Input --> Output)
#
# 13 --> "drink toddy"
# 17 --> "drink coke"
# 18 --> "drink beer"
# 20 --> "drink beer"
# 30 --> "drink whisky"


def people_with_age_drink(age):
    if age < 14:
        drink = "toddy"
    elif 18 > age >= 14:
        drink = "coke"
    elif 21 > age >= 18:
        drink = "beer"
    elif age >= 21:
        drink = "whisky"
    return f"drink {drink}"


if __name__ == '__main__':
    print(people_with_age_drink(13))


# Best solutions:


def people_with_age_drink(age):
    if age > 20: return 'drink whisky'
    if age > 17: return 'drink beer'
    if age > 13: return 'drink coke'
    return 'drink toddy'


def people_with_age_drink(age):
    return 'drink ' + ('toddy' if age < 14 else 'coke' if age < 18 else 'beer' if age < 21 else 'whisky')
