# Given the molecular mass of two molecules M1M_1M1​ and M2M_2M2​, their
# masses present m1m_1m1​ and m2m_2m2​ in a vessel of volume VVV at a
# specific temperature TTT, find the total pressure PtotalP_{total}Ptotal​
# exerted by the molecules. Formula to calculate the pressure is:
# Ptotal=(m1M1+m2M2)RTV\LARGE P_{total} = {{({{m_1} \over {M_1}} + {{m_2}
# \over {M_2}}) R T}
# \over V}Ptotal​=V(M1​m1​​+M2​m2​​)RT​
# Input
#
# Six values :
#
#     M1M_1M1​, M2M_2M2​: molar masses of both gases, in  g⋅mol−1\ g
#     \cdot mol^{-1} g⋅mol−1
#     m1m_1m1​ and m2m_2m2​: present mass of both gases, in grams (ggg)
#     VVV: volume of the vessel, in  dm3\ dm^3 dm3
#     TTT: temperature, in  °C\ \degree C °C
#
# Output
#
# One value: PtotalP_{total}Ptotal​, in units of atmatmatm.
# Notes
#
# Remember: Temperature is given in Celsius while SI unit is Kelvin (KKK).
# 0°C=273.15K\ 0\degree C = 273.15K 0°C=273.15K
#
# The gas constant  R=0.082dm3⋅atm⋅K−1⋅mol−1\ R = 0.082dm^3 \cdot atm
# \cdot K^{-1} \cdot mol^{-1} R=0.082dm3⋅atm⋅K−1⋅mol−1


def solution(molar_mass1, molar_mass2, given_mass1, given_mass2, volume, temp):
    n1 = given_mass1 / molar_mass1
    n2 = given_mass2 / molar_mass2
    return (n1 + n2) * 0.082 * (temp + 273.15) / volume


if __name__ == '__main__':
    print(solution(44, 30, 3, 2, 5, 50))


# Best solutions:


def solution(M1, M2, m1, m2, V, T) :
    return (m1/M1+m2/M2)*0.082*(T+273.15)/V


def solution(M1, M2, m1, m2, V, T):
    return (m1 / M1 + m2 / M2) * (T + 273.15) * .082 / V
