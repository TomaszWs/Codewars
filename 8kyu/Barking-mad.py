# Teach snoopy and scooby doo how to bark using object methods. Currently only
# snoopy can bark and not scooby doo.
#
# snoopy.bark() #return "Woof"
# scoobydoo.bark() #undefined
#
# Use method prototypes to enable all Dogs to bark.


class Dog():
    def __init__(self, breed):
        self.breed = breed

    def bark(self):
        return "Woof"


snoopy = Dog("Beagle")

snoopy.bark = lambda: "Woof"

scoobydoo = Dog("Great Dane")


if __name__ == '__main__':
    print(snoopy.bark())
    print(scoobydoo.bark())


# Best solutions:


class Dog():
    def __init__(self, breed):
        self.breed = breed
        self.bark = lambda: "Woof"


snoopy = Dog("Beagle")

scoobydoo = Dog("Great Dane")


