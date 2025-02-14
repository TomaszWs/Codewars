# Write a function that returns the total surface area and volume of a box as
# an array: [area, volume]


def get_size(w,h,d):
    return [2*(w*h+w*d+d*h), w*h*d]


if __name__ == '__main__':
    print(get_size(4, 2, 6))


# Best solutions:


def get_size(w, h, d):
    area = 2*(w*h + h*d + w*d)
    volume = w*h*d
    return [area, volume]
