# Write a function that calculates the original product price, without VAT.
# Example
#
# If a product price is 200.00 and VAT is 15%, then the final product price
# (with VAT) is: 200.00 + 15% = 230.00
#
# Thus, if your function receives 230.00 as input, it should return 200.00
#
# Notes:
#
#     VAT is always 15% for the purposes of this Kata.
#     Round the result to 2 decimal places.
#     If null value given then return -1


def excluding_vat_price(price):
    return -1 if price is None else round(price / 1.15, 2)


if __name__ == '__main__':
    print(excluding_vat_price(230))


# Best solutions:


def excludingVatPrice(price):
    return round(price / 1.15, 2) if price else -1


def excluding_vat_price(price):
    try:
        return round(price / 1.15, 2)
    except TypeError:
        return -1
