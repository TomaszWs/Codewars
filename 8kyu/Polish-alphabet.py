# There are 32 letters in the Polish alphabet: 9 vowels and 23 consonants.
#
# Your task is to change the letters with diacritics:
#
# ą -> a,
# ć -> c,
# ę -> e,
# ł -> l,
# ń -> n,
# ó -> o,
# ś -> s,
# ź -> z,
# ż -> z
#
# and print out the string without the use of the Polish letters.
#
# For example:
#
# "Jędrzej Błądziński"  -->  "Jedrzej Bladzinski"


def correct_polish_letters(st):
    polish_neutral = {"ą": "a", "ć": "c", "ę": "e", "ł": "l", "ń": "n",
                      "ó": "o", "ś": "s", "ż": "z", "ź": "z"
    }
    return "".join(polish_neutral.get(letter, letter) for letter in st)


if __name__ == '__main__':
    print(correct_polish_letters("Jędrzej Błądziński"))


# Best solutions:


def correct_polish_letters(s):
    return s.translate(str.maketrans("ąćęłńóśźż", "acelnoszz"))


def correct_polish_letters(st):
    l = "ąćęłńóśźż"
    lt = "acelnoszz"
    for i in range(len(l)):
        st = st.replace(l[i], lt[i])
    return st
