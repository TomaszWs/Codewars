# Your job is to find the gravitational force between two spherical objects
# (obj1 , obj2).
# input
# Two arrays are given :
#     arr_val (value array), consists of 3 elements
#         1st element : mass of obj 1
#         2nd element : mass of obj 2
#         3rd element : distance between their centers
#     arr_unit (unit array), consists of 3 elements
#         1st element : unit for mass of obj 1
#         2nd element : unit for mass of obj 2
#         3rd element : unit for distance between their centers
# mass units are :
#     kilogram (kg)
#     gram (g)
#     milligram (mg)
#     microgram (μg)
#     pound (lb)
# distance units are :
#     meter (m)
#     centimeter (cm)
#     millimeter (mm)
#     micrometer (μm)
#     feet (ft)
# Note
# value of G = 6.67 × 10−11 N⋅kg−2⋅m2
# 1 ft = 0.3048 m
# 1 lb = 0.453592 kg
# return value must be Newton for force (obviously)
# μ copy this from here to use it in your solution


def solution(arr_val, arr_unit) :
    mass_units = {
        "kg": 1,
        "g": 1e-3,
        "mg": 1e-6,
        "μg": 1e-9,
        "lb": 0.453592
    }
    distance_units = {
        "m": 1,
        "cm": 1e-2,
        "mm": 1e-3,
        "μm": 1e-6,
        "ft": 0.3048
    }
    return (6.67e-11 *
            (arr_val[0] * mass_units[arr_unit[0]]) *
            (arr_val[1] * mass_units[arr_unit[1]]) /
            ((arr_val[2] * distance_units[arr_unit[2]]) ** 2))


if __name__ == '__main__':
    print(solution([1000, 1000, 100], ["g", "kg", "m"]))


# Best solutions:


units = {"kg": 1, "g": 1e-3, "mg": 1e-6, "μg": 1e-9, "lb": 0.453592,
         "m": 1, "cm": 1e-2, "mm": 1e-3, "μm": 1e-6, "ft": 0.3048,
         "G": 6.67e-11}


def solution(v, u):
    m1, m2, r = (v[i] * units[u[i]] for i in range(3))
    return units["G"] * m1 * m2 / r**2


def solution(arr_val, arr_unit):
    G = 6.67e-11

    weight = {
        "kg": 1,
        "g": 0.001,
        "mg": 1e-6,
        "μg": 1e-9,
        "lb": 0.453592
    }
    distance = {
        "m": 1,
        "cm": .01,
        "mm": .001,
        "μm": 1e-6,
        "ft": 0.3048
    }

    M1 = arr_val[0] * weight[arr_unit[0]]
    M2 = arr_val[1] * weight[arr_unit[1]]
    D = arr_val[2] * distance[arr_unit[2]]

    return G * M1 * M2 / D ** 2
