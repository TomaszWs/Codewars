# Terminal Game - Create Hero Prototype
#
# In this first kata in the series, you need to define a Hero prototype to be
# used in a terminal game. The hero should have the following attributes:
# attribute 	value
# name 	user argument or 'Hero'
# position 	'00'
# health 	100
# damage 	5
# experience 	0


class Hero(object):
    def __init__(self, name = "Hero"):
        self.name = name
        self.position = "00"
        self.health = 100
        self.damage = 5
        self.experience = 0


if __name__ == '__main__':
    hero_1 = Hero("Bob")
    print(vars(hero_1))


# Best solutions:


class Hero(object):
    def __init__(self, name="Hero", position="00",
        health=100, damage=5, experience=0):
        self.name = name
        self.position = position
        self.max_health = health #trust me, you want to have this as well
        self.health = health
        self.damage = damage
        self.experience = experience


class Hero(object):
    def __init__(self, name='Hero'):
        self._name = name
        self._experience = 0
        self._health = 100
        self._position = '00'
        self._damage = 5

    @property
    def name(self):
        return self._name

    @property
    def experience(self):
        return self._experience

    @property
    def health(self):
        return self._health

    @property
    def position(self):
        return self._position

    @property
    def damage(self):
        return self._damage
