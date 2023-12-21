# Task
#
# You will be given an array of numbers. You have to sort the odd numbers in
# ascending order while leaving the even numbers at their original positions.
# Examples
#
# [7, 1]  =>  [1, 7]
# [5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]
# [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  =>  [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]


def sort_array(source_array):
    odd_n = sorted(number for number in source_array if number % 2 != 0)
    return [number if number % 2 == 0 else odd_n.pop(0) for number in
            source_array]


source_array = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(sort_array(source_array))


# Best solutions:


def sort_array(arr):
  odds = sorted((x for x in arr if x%2 != 0), reverse=True)
  return [x if x%2==0 else odds.pop() for x in arr]


def sort_array(source_array):
    odds = []
    answer = []

    for i in source_array:
        if i % 2 > 0:
            odds.append(i)
            answer.append("X")

        else:
            answer.append(i)

    odds.sort()

    for i in odds:
        x = answer.index("X")
        answer[x] = i
    return answer


def sort_array(source_array):
    odds = iter(sorted(v for v in source_array if v % 2))
    return [next(odds) if i % 2 else i for i in source_array]