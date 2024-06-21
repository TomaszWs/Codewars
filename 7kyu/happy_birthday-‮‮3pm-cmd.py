# You're part of a security research group investigating a malware campaign
# following a recent breach at A.C.M.E.com, where hackers obtained user data.
# While passwords were safely hashed, attackers now use stolen emails and
# birthdates to trick users into running malware.
#
# Attackers send emails with attachments disguised as innocent files, timed
# around the victim's birthday. The attachments pretend to be related to the
# birthday event in some form: posing as a postcard with birthday wishes, as a
# package of photos from the party, or as a restaurant bill to split. These
# attachments exploit system features, such as hiding file extensions and using
# a Right-to-Left Override character (RTLO) in the filename. This conceals the
# true file type and can obfuscate part of the filename, making the malware
# appear harmless when viewed.
# Obfuscation Techniques
#
# Some operating systems have a setting to hide file extensions from users.
# This setting aims to enhance user experience by concealing potentially
# confusing technical details from non-technical users. On a computer with this
# option enabled, for instance, a file named cute_kittens.jpg would have its
# extension hidden, with only its name, cute_kittens, being visible.
#
# However, even if the extensions are hidden in folders, they can still be
# visible when showing attachments in email clients or browsers. That’s why the
# attackers use an additional obfuscation technique: Right-to-Left Override.
#
# The Right-to-Left Override marker is a special Unicode character with code
# U+202E, capable of producing confusing effects. When present in a filename
# visible in a folder on a system using a left-to-right locale, the name can
# be presented misleadingly: anything preceding the marker is displayed
# normally, the marker itself is not displayed, and anything following the
# marker is displayed in reverse.
#
# When both features are exploited by a malware author, a user can be tricked
# into running malware on their machine while they believe they are opening a
# legitimate, innocent file:
#
# confusing_files
#
# You might think that icons would give away the whole trick, right?
# Unfortunately, icons can be easily changed too! However, changing icons is
# beyond the scope of this challenge.
# Task
#
# To further investigate the malware campaign, you need to create a function
# that mimics the method of the attack and simulates the operating system. It
# should accept a crafted, malicious name and return the name users would see
# in their folder, with the extension hidden and applying the confusing effect
# of the Right-to-Left Override marker.
#
# The campaign targets users from Europe, and you can assume that users will
# have their computers initially set to a left-to-right language.
# Examples
#
# An example malware file to be distributed is an executable named
# birthday_balloons.[RTLO]gpj.exe. When it's viewed in a folder, the following
# sequence of events will occur:
#
#     First, the RTLO character will obfuscate the file name, presenting the
#     part following it in reverse, resulting in the visible file name
#     birthday_balloons.exe.jpg.
#     Afterwards, the file extension will be hidden by the operating system,
#     leaving the visible portion as birthday_balloons.jpg.
#
# Rules
#
#     Input filenames will always have exactly one RTLO character. It can be
#     placed anywhere in the filename except in the real extension.
#     Filenames can contain one or more dots. Only the part after the last dot
#     constitutes an extension and is hidden.
#
# References
#
#     Interesting video presenting the technique.
#     Description of the RIGHT-TO-LEFT OVERRIDE Unicode character.
#     xkcd #1137.
#
# This kata is a submission to the EPIC Challenge 2024.


def get_visible_name(malicious_name):
    if "\u202E" in malicious_name:
        elements = malicious_name.split("\u202E", 1)
        prefix = elements[0]
        affix = elements[1]
        true_ext = affix.rfind(".")
        if true_ext != -1:
            part_to_reverse = affix[:true_ext]
            reversed_part = part_to_reverse[::-1]
            visible = prefix + reversed_part
        else:
            visible = prefix
    else:
        visible = malicious_name
    return visible


if __name__ == "__main__":
    print(get_visible_name("birthday_balloons.[RTLO]gpj.exe"))


# Best solutions:


from pathlib import Path


def get_visible_name(name):
    name = Path(name).stem
    l, r = name.split('\u202E')
    return l + r[::-1]


RTLO = '\u202E'


def get_visible_name(malicious_name):
    without_extension = malicious_name[:malicious_name.rindex('.')]
    [left_to_right, right_to_left] = without_extension.split(RTLO)
    return left_to_right + right_to_left[::-1]


def get_visible_name(malicious_name):
    a, rest = malicious_name.split("\u202e")

    return a + ".".join(rest.split(".")[:-1])[::-1]