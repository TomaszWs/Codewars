# The following formula is called the Decibel Scale:
#
# β=10log⁡10(I10−12) \beta = 10\log_{10}\left(\dfrac{I}{10^{-12}}\right)
# β=10log10​(10−12I​)
#
# The Decibel Scale is used to determine the loudness of a sound, measured in
# dB:
#
#     β is the result we want, defined in dB;
#     We multiply the result of the logarithmic operation by 10, otherwise
#     it'll be called "Bel Scale";
#     We provide I, the intensity of the sound wave we need to find the
#     loudness of, which is, for the purposes of this Kata, measured in 2D
#     space and, hence, in Watts per square meter;
#     Finally, we divide the intensity by the threshold of human hearing, also
#     measured in Watts per square meter. This is the softest possible sound a
#     human ear can hear;
#     Since the threshold of human hearing involves an extremely small, long
#     number, we need to utilize a logarithmic operation that will provide us
#     the result in a convenient way.
#
# Your task is to simply calculate the loudness of a sound wave, given its
# intensity as a parameter to the dBScale function.
#
# Results are automatically rounded to the nearest integer by the test cases.


import math


def db_scale(intensity):
    return 10 * math.log10(intensity / 10**-12)


if __name__ == '__main__':
    print(db_scale(10 ** -9))
