"""
role
~~~~
"Attribute class", provide objects of Role subclasses to Actor objects to
create Actor with specific properties.

Create an object of the "Role" subclass called "Enemy" and give it attributes:
    MONSTER = Enemy(health=100, attack=5, jump_height=1)
Create a new actor and provide it the generic role of "MONSTER".
    Cthulu = Actor(role=MONSTER, name="Cthulu")
    Diablo = Actor(role=MONSTER, name="Diablo")

Composition model is simpler than using inheritance and many actor subclasses:
    See also: http://gameprogrammingpatterns.com/type-object.html

:author: Sean Pianka

"""
class Role:
    """ Defines implementation and generic behavior for all Actors which are
    built from the specific role. Subclasses contain information that will be
    shared among all actors which are built from the aforementioned role.

    """
    def __init__(self, **kwargs):
        self._health = kwargs['health']
        self._attack = kwargs['attack']
        self._jump_height = kwargs['jump_height']
        self._inventory = []
        # The current item that the actor is wielding.
        self._wielded = None if len(self._inventory) is 0 else self._inventory[0]

    def __str__(self):
        return "{}".format(self.__class__.__name__)

    @property
    def health(self):
        return self._health

    @property
    def wielded(self):
        return self._wielded

    @property
    def attack(self):
        return self._attack

    @property
    def jump_height(self):
        return self._jump_height

    @property
    def inventory(self):
        return self._inventory


class Player(Role, object):
    """ The actor will be controlled by the player.

    """
    count = 0
    def __init__(self, **kwargs):
        Player.count += 1

        super(Player, self).__init__(**kwargs)


class Enemy(Role, object):
    """ The actor will be an enemy to/able to be fought by the player.

    """
    count = 0
    def __init__(self, **kwargs):
        Enemy.count += 1

        super(Enemy, self).__init__(**kwargs)
        self._hostile = True

    @property
    def hostile(self):
        return self._hostile


class NPC(Role, object):
    """ The actor will be friendly and interactable by the player.

    """
    count = 0
    def __init__(self, **kwargs):
        NPC.count += 1

        super(NPC, self).__init__(**kwargs)
        self._hostile = False

    @property
    def hostile(self):
        return self._hostile
