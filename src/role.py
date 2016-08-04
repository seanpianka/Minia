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
from unique_id import UniqueID


class Role(UniqueID):
    """ Defines implementation and generic behavior for all Actors which are
    built from the specific Role. Subclasses contain information that will be
    shared among Actors which are built from the aforementioned Role.

    """
    _uid = UniqueID._uid
    def __init__(self, family, health, attack, jump_height, texture_path):
        """ Create a new Role instance with associated family, health, attack,
        and jump_height.

        :param family: The name of the Role that was created.
        :type family: str

        :param health: The health that all Actors built from said Role will
            start with.
        :type health: int

        :param attack: The attack that all Actors built from said Role will
            start with.
        :type attack: int

        :param jump_height: The jump height that all Actors built from said
            Role will start with.
        :type jump_height: int

        """
        super(Role, self).__init__()
        self._family = family
        self._health = health
        self._attack = attack
        self._jump_height = jump_height
        self._texture_path = texture_path
        self._inventory = []
        # The current item that the actor is wielding.
        self._wielded = None if len(self._inventory) is 0 else self._inventory[0]

    def __str__(self):
        return "{}: {}".format(self.__class__.__name__, self.family)

    @property
    def family(self):
        return self._family

    @property
    def health(self):
        return self._health

    @property
    def attack(self):
        return self._attack

    @property
    def jump_height(self):
        return self._jump_height

    @property
    def texture_path(self):
        return self._texture_path

    @property
    def inventory(self):
        return self._inventory

    @property
    def wielded(self):
        return self._wielded


class Player(Role, object):
    """ The actor will be controlled by the player.

    """
    _uid = Role._uid
    def __init__(self, family, health, attack, jump_height, texture_path):
        super(Player, self).__init__(family, health, attack,
                                     jump_height, texture_path)


class Enemy(Role, object):
    """ The actor will be an enemy to/able to be fought by the player.

    """
    _uid = Role._uid
    def __init__(self, family, health, attack, jump_height, texture_path):
        super(Enemy, self).__init__(family, health, attack,
                                    jump_height, texture_path)
        self._hostile = True

    @property
    def hostile(self):
        return self._hostile


class NPC(Role, object):
    """ The actor will be friendly and interactable by the player.

    """
    _uid = Role._uid
    def __init__(self, family, health, attack, jump_height, texture_path):
        super(NPC, self).__init__(family, health, attack,
                                  jump_height, texture_path)
        self._hostile = False

    @property
    def hostile(self):
        return self._hostile
