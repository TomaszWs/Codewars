# Count the number of Duplicates
#
# Write a function that will return the count of distinct case-insensitive
# alphabetic characters and numeric digits that occur more than once in the
# input string. The input string can be assumed to contain only alphabets
# (both uppercase and lowercase) and numeric digits.

# Example

# "abcde" -> 0 # no characters repeats more than once
# "aabbcde" -> 2 # 'a' and 'b'
# "aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
# "indivisibility" -> 1 # 'i' occurs six times
# "Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
# "aA11" -> 2 # 'a' and '1'
# "ABBA" -> 2 # 'A' and 'B' each occur twice


def duplicate_count(text):
    text = text.lower()
    characters = {}
    Duplicates = []
    for character in text:
        if character not in characters:
            characters[character] = 1
        else:
            characters[character] += 1
    for character, number in characters.items():
        if number > 1:
            Duplicates.append(character)
    return len(Duplicates)


text = "aabbcde"
print(duplicate_count(text))


# Best solutions

def duplicate_count(s):
  return len([c for c in set(s.lower()) if s.lower().count(c)>1])


def duplicate_count(text):
    seen = set()
    dupes = set()
    for char in text:
        char = char.lower()
        if char in seen:
            dupes.add(char)
        seen.add(char)
    return len(dupes)


def duplicate_count(text):
    count = 0
    for c in set(text.lower()):
        if text.lower().count(c) > 1:
            count += 1
    return count
