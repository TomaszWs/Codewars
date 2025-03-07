# Create a method that accepts a list and an item, and returns true if the item
# belongs to the list, otherwise false.


def include(arr, item):
    return item in arr


if __name__ == '__main__':
    print(include([0,1,2,3,5,8,13,2,2,2,11], 100))
