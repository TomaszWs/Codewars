# Create a function that converts US dollars (USD) to Chinese Yuan (CNY) . The input is the amount of USD as an integer, and the output should be a string that states the amount of Yuan followed by 'Chinese Yuan'
# Examples (Input -> Output)
#
# 15  -> '101.25 Chinese Yuan'
# 465 -> '3138.75 Chinese Yuan'
#
# The conversion rate you should use is 6.75 CNY for every 1 USD. All numbers should be represented as a string with 2 decimal places. (e.g. "21.00" NOT "21.0" or "21")


def usdcny(usd):
    return f"{usd * 6.75:.2f} Chinese Yuan"


if __name__ == '__main__':
    print(usdcny(15))


# Best solutions:



COURSE = 6.75  # CNY == 1 USD


def usdcny(usd):
    return f"{usd * COURSE:.2f} Chinese Yuan"


def usdcny(bucks):
    return '%.2f Chinese Yuan' %(bucks * 6.75)


def usdcny(usd):
    rate = 6.75
    return "{:.2f} Chinese Yuan".format(usd*rate)
