# This kata is inspired by Callum Macrae's Regex Challenges
#
# Create a regex to match the symbols of all 118 chemical elements.
#
# Your regex pattern can be maximum 210 characters long.
# My other katas
#
# If you enjoyed this kata then please try my other katas! :-)
# Translations are welcome!
#
# (except for Ruby, which is coming shortly)


# R = "^(H|He|Li|Be|B|C|N|O|F|Ne|Na|Mg|Al|Si|P|S|Cl|Ar|K|Ca|Sc|Ti|V|Cr|Mn|Fe|Co|Ni|Cu|Zn|Ga|Ge|As|Se|Br|Kr|Rb|Sr|Y|Zr|Nb|Mo|Tc|Ru|Rh|Pd|Ag|Cd|In|Sn|Sb|Te|I|Xe|Cs|Ba|La|Ce|Pr|Nd|Pm|Sm|Eu|Gd|Tb|Dy|Ho|Er|Tm|Yb|Lu|Hf|Ta|W|Re|Os|Ir|Pt|Au|Hg|Tl|Pb|Bi|Po|At|Rn|Fr|Ra|Ac|Th|Pa|U|Np|Pu|Am|Cm|Bk|Cf|Es|Fm|Md|No|Lr|Rf|Db|Sg|Bh|Hs|Mt|Ds|Rg|Cn|Nh|Fl|Mc|Lv|Ts|Og)$"


R=r"(A[cglmrsut]|B[aehikr]?|C[mnfadelorsu]?|D[bsy]|E[rsu]|F[elmr]?|G[ade]|H[efgos]?|I[nr]?|K[r]?|L[airuv]|M[cdgnot]|N[habdeiop]?\b|O[gs]?|P[abdmortu]?|R[gabefhnu]|S[bcegimnr]?|T[sabcehilm]|U|V|W|Xe|Yb?|Z[nr])$"

# Best solutions:


R="([IUVW]|[ACE][rsu]|[BFKPS]r?|[CGN][ade]|[IZ][nr]|A[cglmt]|B[aehik]|C[fl-o]?|D[bsy]|F[elm]|[HO][gs]?|H[efo]|L[airuv]|M[cdgnot]|N[bhiop]?|P[abdmotu]|R[abe-hnu]|S[bcegimn]|T[abcehilms]|Xe|Yb?)$"


R="^([ACE][rsu]|[CGN][ade]|[IZ][nr]|A[cglmt]|B[aehikr]?|C[fl-o]?|D[bsy]|F[elmr]?|H[efgos]?|Kr?|L[airuv]|M[cdgnot]|N[bhiop]?|O[gs]?|P[abdmortu]?|R[abe-hnu]|S[bcegimnr]?|T[abcehilms]|[IUVW]|Xe|Yb?)$"


