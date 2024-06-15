# This kata is a submission to the EPIC Challenge 2024.
# The Hall
#
# You are a servant in The Great Hall of Ghosts. The purpose of this place is
# to hold the Day of Passing ceremony in honor of the deceased members of your
# society. The hall was carved directly out of the mountain rock to house a
# majestic square Grand Table surrounded by twelve magnificent Seats of Honor.
# Each corner of the hall is adorned by one of the four Culturally Significant
# Features. Going clockwise around the table, they are; a comforting
# arrangement of earthenware holding exotic plants in lucious soil, a natural
# waterfall of gentle sounds and sweet moisture, a roaring fireplace of
# tremendous warmth, and a breezy windowsill open to the freshest of air.
#
# Earthenware                            Waterfall
#
#      ( __1__ ) ( __2__ ) ( __3__ ) ( __4__ )
#
#      ( _12__ )                     ( __5__ )
#
#      ( _11__ )                     ( __6__ )
#
#      ( _10__ ) ( __9__ ) ( __8__ ) ( __7__ )
#
#  Windowsill                             Fireplace
#
# The Dead
#
# Every morning, the Elders give you a List of the Dead naming people who
# throughout the past had died on that date, although a person's name is only
# included on the list if currently living members of society have made any
# donations in their name for this year.
# Your Task
#
# The obligation in service to which you are assigned in the Great Hall is to
# set out the places in preparation for the ceremonial dinner at the Grand
# Table every evening, and the most important part of this task is to figure
# out exactly which Ghosts should sit at which Seats amongst the twelve!
#
# The seating arrangement will be based on the order in which they appear on
# your list and the most favored Culturally Significant Feature of each
# particular ghost. Their favorite feature is devised by using the initial
# letter of their name and the Four Ancient Names of the corner features:
#
#     they favor Earthenware if their first initial is one of the letters in the name "QUTHCRDMZ"
#     they favor Waterfall if their first initial is one of the letters in the name "WEVOXING"
#     they favor Fireplace if their first initial is one of the letters in the name "JFABKPLY"
#     they favor Windowsill if their first initial is one of the letters in the name "SSSSSSSSS"
#
# For the names on the list, one at a time, they each get an opportunity to be
# seated as close as possible to the corner they desire the most. Whenever
# there are two seats that are equidistant from the preferred corner seat, the
# ghost will always take the seat which is counter-clockwise to that corner.
#
# As the table gradually fills up, those later on the list will have fewer and
# notably less attractive seating options from which to choose.
#
# Depending on how many names made the list this year, there will often be days
# when there are too many ghosts to be seated, and only the first twelve can
# be seated. On other days there could be a number of empty seats if there
# were fewer applicants. In this case, those empty seats should be represented
# by a string of five underscores ("_____") in lieu of the name of a ghost.
# An Example
#
# Given this List of the Dead to be tasked with seating the Grand Table:
#
# the_dead = ['Yojne', 'Xenna', 'Verap', 'Ebyam', 'Teseb', 'Ycuag', 'Onets',
# 'Skcaw', 'Yrovi', 'Tpets', 'Lizuf', 'Girnu']
#
# The first name on the list is Yojne. Because their name starts with the
# letter Y, they are of the JFABKPLY clan and therefore want to sit as close
# as possible to the Fireplace. As the table is completely empty, they will
# get their first choice, and be assigned to Seat 7:
#
# Earthenware                            Waterfall
#
#      ( __1__ ) ( __2__ ) ( __3__ ) ( __4__ )
#
#      ( _12__ )                     ( __5__ )
#
#      ( _11__ )                     ( __6__ )
#
#      ( _10__ ) ( __9__ ) ( __8__ ) ( Yojne )
#
#  Windowsill                             Fireplace
#
# Next on the list is Xenna, who with the first letter X hails from the
# WEVOXING family and thus favors the Waterfall, and they also get their first
# choice in Seat 4:
#
# Earthenware                            Waterfall
#
#      ( __1__ ) ( __2__ ) ( __3__ ) ( Xenna )
#
#      ( _12__ )                     ( __5__ )
#
#      ( _11__ )                     ( __6__ )
#
#      ( _10__ ) ( __9__ ) ( __8__ ) ( Yojne )
#
#  Windowsill                             Fireplace
#
# Third on the list is Verap, who also has the Waterfall as their favorite
# feature, but since Xenna is sitting in the corner seat, Verap will have to
# take the next best option, which is a seat nearest to that corner.
#
# Here we have a case of two equidistant options; the two seats that are
# closest to the Waterfall are Seat 3 and Seat 5. Verap's ghost will be seated
# at Seat 3 because it is counter-clockwise from Seat 4 in the corner:
#
# Earthenware                            Waterfall
#
#      ( __1__ ) ( __2__ ) ( Verap ) ( Xenna )
#
#      ( _12__ )                     ( __5__ )
#
#      ( _11__ )                     ( __6__ )
#
#      ( _10__ ) ( __9__ ) ( __8__ ) ( Yojne )
#
#  Windowsill                             Fireplace
#
# Fourth in order we get Ebyam, and in also favoring the Waterfall, takes
# Seat 5:
#
# Earthenware                            Waterfall
#
#      ( __1__ ) ( __2__ ) ( Verap ) ( Xenna )
#
#      ( _12__ )                     ( Ebyam )
#
#      ( _11__ )                     ( __6__ )
#
#      ( _10__ ) ( __9__ ) ( __8__ ) ( Yojne )
#
#  Windowsill                             Fireplace
#
# Fifth is Teseb of the QUTHCRDMZ leaning, and easily takes the Earthenware
# corner seat:
#
# Earthenware                            Waterfall
#
#      ( Teseb ) ( __2__ ) ( Verap ) ( Xenna )
#
#      ( _12__ )                     ( Ebyam )
#
#      ( _11__ )                     ( __6__ )
#
#      ( _10__ ) ( __9__ ) ( __8__ ) ( Yojne )
#
#  Windowsill                             Fireplace
#
# Sixth is Ycuag who will want to be near the Fireplace, so they take Seat 6:
#
# Earthenware                            Waterfall
#
#      ( Teseb ) ( __2__ ) ( Verap ) ( Xenna )
#
#      ( _12__ )                     ( Ebyam )
#
#      ( _11__ )                     ( Ycuag )
#
#      ( _10__ ) ( __9__ ) ( __8__ ) ( Yojne )
#
#  Windowsill                             Fireplace
#
# Onets comes along in seventh place and also favors the very popular
# Waterfall. They take the best choice remaining which is Seat 2:
#
# Earthenware                            Waterfall
#
#      ( Teseb ) ( Onets ) ( Verap ) ( Xenna )
#
#      ( _12__ )                     ( Ebyam )
#
#      ( _11__ )                     ( Ycuag )
#
#      ( _10__ ) ( __9__ ) ( __8__ ) ( Yojne )
#
#  Windowsill                             Fireplace
#
# At last, we get a member of the Windowsill fan club in eighth place. Skcaw
# readily takes that corner at Seat 10:
#
# Earthenware                            Waterfall
#
#      ( Teseb ) ( Onets ) ( Verap ) ( Xenna )
#
#      ( _12__ )                     ( Ebyam )
#
#      ( _11__ )                     ( Ycuag )
#
#      ( Skcaw ) ( __9__ ) ( __8__ ) ( Yojne )
#
#  Windowsill                             Fireplace
#
# Ninth appears Yrovi, who wants to be near the Fireplace, and takes Seat 8:
#
# Earthenware                            Waterfall
#
#      ( Teseb ) ( Onets ) ( Verap ) ( Xenna )
#
#      ( _12__ )                     ( Ebyam )
#
#      ( _11__ )                     ( Ycuag )
#
#      ( Skcaw ) ( __9__ ) ( Yrovi ) ( Yojne )
#
#  Windowsill                             Fireplace
#
# Tpets in ten place is an Earthenware acolyte, and takes the closest place
# next to that corner at Seat 12:
#
# Earthenware                            Waterfall
#
#      ( Teseb ) ( Onets ) ( Verap ) ( Xenna )
#
#      ( Tpets )                     ( Ebyam )
#
#      ( _11__ )                     ( Ycuag )
#
#      ( Skcaw ) ( __9__ ) ( Yrovi ) ( Yojne )
#
#  Windowsill                             Fireplace
#
# In eleventh place we get Lizuf of Fireplace people, and now with only two
# places to choose from, obviously takes Seat 9:
#
# Earthenware                            Waterfall
#
#      ( Teseb ) ( Onets ) ( Verap ) ( Xenna )
#
#      ( Tpets )                     ( Ebyam )
#
#      ( _11__ )                     ( Ycuag )
#
#      ( Skcaw ) ( Lizuf ) ( Yrovi ) ( Yojne )
#
#  Windowsill                             Fireplace
#
# The final ghost coming in at twelfth place is Girnu, yet another ghost
# wanting to be near the Waterfall, but they are too late on the list to get
# a seat close to that corner, and must be satisfied to even be at the table
# in Seat 11:
#
# Earthenware                            Waterfall
#
#      ( Teseb ) ( Onets ) ( Verap ) ( Xenna )
#
#      ( Tpets )                     ( Ebyam )
#
#      ( Girnu )                     ( Ycuag )
#
#      ( Skcaw ) ( Lizuf ) ( Yrovi ) ( Yojne )
#
#  Windowsill                             Fireplace
#
# The table now being completely sat, we end up with a final seating
# arrangement in the form of a list taking the seats from the top left corner
# and going clockwise through the twelve seats:
#
# seating = ['Teseb', 'Onets', 'Verap', 'Xenna', 'Ebyam', 'Ycuag', 'Yojne',
# 'Yrovi', 'Lizuf', 'Skcaw', 'Girnu', 'Tpets']
#
# Input
#
# A list (0 <= size <= 18) of names (each size == 5 chars long).
# Output
#
# A list (always size == 12) of names (or placeholders: "_____" ),
# representing the final seating arrangement.
# Enjoy!
#
# ...and please consider one of the following kata to solve next:
#
#     Playing With Toy Blocks ~ Can you build a 4x4 square?
#     Four Letter Words ~ Mutations
#     Interlocking Binary Pairs
#     Crossword Puzzle! (2x2)
#     Is Sator Square?
#
# This kata is a submission to the EPIC Challenge 2024.


def set_table(the_dead):
    seats = ["_____", "_____", "_____", "_____", "_____", "_____", "_____",
             "_____", "_____", "_____", "_____", "_____", "_____"]
    corner_plan = {
        "QUTHCRDMZ": (1, [1, 12, 2, 11, 3, 10, 4, 9, 5, 8, 7, 7]),
        "WEVOXING": (4, [4, 3, 5, 2, 6, 1, 7, 12, 8, 11, 9, 10]),
        "JFABKPLY": (7, [7, 6, 8, 5, 9, 4, 10, 3, 11, 2, 12, 1]),
        "SSSSSSSSS": (10, [10, 9, 11, 8, 12, 7, 1, 6, 2, 5, 3, 4])
    }

    def preferred_seat(name):
        for clan, (corner, closest_seats) in corner_plan.items():
            if name[0] in clan:
                return corner, closest_seats
        return None

    table_seated = {}
    for name in the_dead:
        preferred_corner, priority_seats = preferred_seat(name)
        for seat in priority_seats:
            if seat not in table_seated:
                table_seated[seat] = name
                break
    for seat, name in table_seated.items():
        seats[seat - 1] = name
    return seats[:12]


if __name__ == "__main__":
    print(set_table(["Yojne", "Xenna", "Verap", "Ebyam", "Teseb", "Ycuag", "Onets", "Skcaw", "Yrovi", "Tpets", "Lizuf", "Girnu"]))


# Best solutions:


CORNERS = {letter: 3 * i for i, letters in enumerate(("QUTHCRDMZ", "WEVOXING", "JFABKPLY", "S")) for letter in letters}


def set_table(the_dead):
    n = 12
    table = ['_____'] * n
    def find_seat(i, d):
        for j in range(n):
            k = (i + d * j) % n
            if table[k] == '_____':
                return k, j
    for name in the_dead[:12]:
        p = CORNERS[name[0]]
        p1, d1 = find_seat(p, -1)
        p2, d2 = find_seat(p, 1)
        table[p1 if d1 <= d2 else p2] = name
    return table


class Node:
    def __init__(self, seatNumber):
        self.seatNumber = seatNumber
        self.occupant = None
        self.next = None
        self.previous = None


class LinkedTable:

    def __init__(self):

        self.head = Node(1)
        self.lastNode = self.head
        self.earthenware = self.head

        for x in range(2, 13):
            newNode = Node(x)

            if x == 4:
                self.waterfall = newNode
            elif x == 7:
                self.fireplace = newNode
            elif x == 10:
                self.windowsill = newNode

            self.lastNode.next = newNode
            newNode.previous = self.lastNode
            self.lastNode = newNode

        # Links 12 and 1 together
        self.lastNode.next = self.head
        self.head.previous = self.lastNode

    def seatBest(self, preference, name):
        if preference == "earthenware":
            startSeat = self.earthenware
        elif preference == "waterfall":
            startSeat = self.waterfall
        elif preference == "windowsill":
            startSeat = self.windowsill
        else:
            startSeat = self.fireplace

        if startSeat.occupant == None:
            startSeat.occupant = name
            return

        seated = False

        leftSeat = startSeat.previous
        rightSeat = startSeat.next
        attempts = 0
        while seated == False and attempts < 12:
            if leftSeat.occupant == None:
                leftSeat.occupant = name
                seated = True
            elif rightSeat.occupant == None:
                rightSeat.occupant = name
                seated = True

            if seated == False:
                leftSeat = leftSeat.previous
                rightSeat = rightSeat.next

            attempts += 1

    def outputTable(self):
        tableContent = []
        currentNode = self.head
        for x in range(12):
            if currentNode.occupant != None:
                tableContent.append(currentNode.occupant)
            else:
                tableContent.append("_____")

            currentNode = currentNode.next

        return tableContent


def set_table(the_dead):
    earthenware = ["Q", "U", "T", "H", "C", "R", "D", "M", "Z"]
    waterfall = ["W", "E", "V", "O", "X", "I", "N", "G"]
    fireplace = ["J", "F", "A", "B", "K", "P", "L", "Y"]
    windowsill = ["S"]

    table = LinkedTable()
    counter = 0
    for name in the_dead:

        if counter > 12:
            break

        if name[0].upper() in earthenware:
            table.seatBest("earthenware", name)
        elif name[0].upper() in waterfall:
            table.seatBest("waterfall", name)
        elif name[0].upper() in fireplace:
            table.seatBest("fireplace", name)
        elif name[0].upper() in windowsill:
            table.seatBest("windowsill", name)

        counter += 1

    return table.outputTable()


def set_table(the_dead):
    res = ['_____'] * 12

    for x in the_dead[:12]:
        st = 0 if x[0] in 'QUTHCRDMZ' else 3 if x[0] in 'WEVOXING' else 6 if x[
                                                                                 0] in 'JFABKPLY' else 9
        shift = next(dst * dir for dst in range(7) for dir in (-1, 1) if
                     res[(st + dst * dir) % 12] == '_____')
        res[(st + shift) % 12] = x

    return res


def get_corner(name):
    name_corners = {
        'Earthenware': 'QUTHCRDMZ',
        'Waterfall': 'WEVOXING',
        'Fireplace': 'JFABKPLY',
        'Windowsill': 'S'
    }
    corners_map = {
        'Earthenware': 0,
        'Waterfall': 3,
        'Fireplace': 6,
        'Windowsill': 9
    }
    first_letter = name[0]
    for key, value in name_corners.items():
        if first_letter in value:
            return corners_map[key]
    return


def set_table(the_dead):
    seats = ['_____'] * 12
    preference_map = [0, -1, 1, -2, 2, -3, 3, -4, 4, -5, 5, -6]
    for name in the_dead:
        best_seat = get_corner(name)
        for i in preference_map:
            if seats[(12 + (best_seat + i)) % 12] == '_____':
                seats[(12 + (best_seat + i)) % 12] = name
                break
    return seats