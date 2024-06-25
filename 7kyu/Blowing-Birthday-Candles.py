# Background
#
# Today is the special day you've been waiting for — it's your birthday! It's 8
# AM and you're setting up your birthday cake for the party. It's time to put
# the candles on top.
#
# You take out all the candles you've bought. As you are about to put them on
# the cake, you just realize that there are numbers on each candles. What are
# these numbers?! After searching about it on the internet, turns out these are
# special candles. These candles need to be blown a certain number of times
# before they're finally extinguished, and those numbers on the candles are the
# required times to blow them.
#
# Being one who plans meticulously, you want to determine the total number of
# blows you need to extinguish all the candles once you've put them on the
# cake.
# Task
#
# Given a string containing digits (representing the strength of the candles),
# calculate the number of blows you need to extinguish all the candles.
#
# Starting at the beginning of the string, each blow can only reach 3 candles,
# reducing their strength by one each. You can only reach more candles once
# those directly in front of you are extinguished.
# Examples
#
# Input: "1321"
#
# Move 1 | "(132)1" -> "0211"
# Move 2 | "0(211)" -> "0100"
# Move 3 | "0(100)" -> "0000"
#
# This should return 3.
#
# Input: "0323456"
#
# Move 1 | "0(323)456" -> "0212456"
# Move 2 | "0(212)456" -> "0101456"
# Move 3 | "0(101)456" -> "0000456"
# Move 4 | "0000(456)" -> "0000345"
# Move 5 | "0000(345)" -> "0000234"
# Move 6 | "0000(234)" -> "0000123"
# Move 7 | "0000(123)" -> "0000012"
# Move 8 | "00000(12)" -> "0000001"
# Move 9 | "000000(1)" -> "0000000"
#
# This should return 9.
#
# Input: "2113"
#
# Move 1 | "(211)3" -> "1003"
# Move 2 | "(100)3" -> "0003"
# Move 3 | "000(3)" -> "0002"
# Move 4 | "000(2)" -> "0001"
# Move 5 | "000(1)" -> "0000"
#
# This should return 5.
#
# Good luck blowing all those candles ;-)
#
# This kata is created for The EPIC Challenge in honor of Andela's 10-year
# anniversary.
#
# This kata is also created on my birthday 🥳


def blow_candles(st):
    st = [int(i) for i in st]
    counter = 0
    while any(st):
        i = 0
        while i < len(st) and st[i] == 0:
            i += 1
        for j in range(i, min(i + 3, len(st))):
            if st[j] > 0:
                st[j] -= 1
        counter += 1
    return counter


if __name__ == "__main__":
    print(blow_candles("0323456"))


# Best solutions:


def blow_candles(st):
    a, b, res = 0, 0, 0
    for x in map(int, st):
        a, b = max(x - a - b, 0), a
        res += a
    return res


def blow_candles(st):
    blow2 = blow1 = blows = 0
    for candle in map(int, st):
        blow0 = max(0, candle - blow1 - blow2)
        blows += blow0
        blow2, blow1 = blow1, blow0
    return blows


def blow_candles(st):
    digits = [int(num) for num in st]
    blows = 0
    while sum(digits) > 0:
        while digits[0] == 0:
            digits = digits[1:]
        digits = [max(0, num - 1) for num in digits[:3]] + digits[3:]
        blows += 1
    return blows
