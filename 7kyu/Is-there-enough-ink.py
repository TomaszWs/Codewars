# Is there enough ink for printing the image?
#
# You will get an image and the level of ink for each primary color in the tank
# of the printer. The image is a matrix where each cell is the color of a
# pixel. The color is a string of a RGB hexadecimal notation (e.g white is
# 'ffffff' and black is '000000'). Each primary color is a integer.
#
# A pixel with the color code 'fefdfc' need 1 unit of Red, 2 units of Green and
# 3 units of Blue.
#
# A pixel with the color code '00ff01' need 255 units of Red, 0 units of Green
# and 254 units of Blue.
#
# The image is two dimensional. E.g: image = [["ffffff", "ffffff"], ["ffffff",
# "ffffff"]]
#
# Your task is to determine if they are enough ink in the tank to print the
# image.
#
# If the ink is enough, the "enough_ink()" function should return True. False
# otherwise.
#
# Have fun!


def enough_ink(image, r, g, b):
    total_red = 0
    total_green = 0
    total_blue = 0
    for row in image:
        for pixel in row:
            if pixel == "ffffff":
                continue
            elif pixel == "000000":
                total_red += 255
                total_green += 255
                total_blue += 255
            elif pixel == "fefefe":
                total_red += 1
                total_green += 1
                total_blue += 1
            else:
                red = int(pixel[0:2], 16)
                green = int(pixel[2:4], 16)
                blue = int(pixel[4:6], 16)
                total_red += red
                total_green += green
                total_blue += blue
    return total_red <= r and total_green <= g and total_blue <= b


if __name__ == "__main__":
    print(enough_ink([["fefefe", "fefefe", "fefefe"], ["fefefe", "fefefe", "fefefe"], ["fefefe", "fefefe", "fefefe"]], 9, 9, 9))


# Best solutions:


def enough_ink(image,R,G,B):
    for row in image:
        for a,b,c,d,e,f,*_ in row:
            R-=255-int(a+b,16)
            G-=255-int(c+d,16)
            B-=255-int(e+f,16)
    return R>=0 and G>=0 and B>=0


def enough_ink(a, r, g, b):
    for x in a:
        for y in x:
            r -= 255 - int(y[0:2], 16)
            g -= 255 - int(y[2:4], 16)
            b -= 255 - int(y[4:6], 16)
    return min(r, g, b) >= 0
