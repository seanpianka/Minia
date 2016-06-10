"""
actor
~~~~~
Container class for an "Actor", an object which will be rendered to the screen
and will have unique properties shared among all actors of that role.

Create an object of the "Role" subclass called "Enemy" and give it attributes:
    MONSTER = Enemy(health=100, attack=5, jump_height=1)
Create a new actor and provide it the generic role of "MONSTER".
    Cthulu = Actor(role=MONSTER, name="Cthulu")
    Diablo = Actor(role=MONSTER, name="Diablo")

Composition model is simpler than using inheritance and many actor subclasses:
    See also: http://gameprogrammingpatterns.com/type-object.html

:author: Sean Pianka

"""
import pyglet

from entity import Entity


class Actor(Entity, object):
    _uid = Entity._uid
    batch = pyglet.graphics.Batch()

    def __init__(self, name, role, texture_path=None,
                 facing=[1, 1], movement=0, position=[0, 0]):
        """ Initialize a new instance of an Actor (which is an entity).

        :param role: Object which contains the generic information assigned to
            the actor being instantiated.
        :type role: Role.Role

        :param name: The name of the actor.
        :type name: str

        :param texture_path: The path from CWD to the texture file.
        :type texture_path: str

        :param texture_batch: The batch for the sprite to be added to.
        :type texture_batch: pyglet.graphics.Batch

        :param movement: Which direction the entity is initially moving. 0 to
            indicate it is stopped, -1 to indicate leftward movement, and 1 to
            indicate rightward movement.
        :type movement: int

        :param position: A tuple of the (x, y) initial coordinates of the
            sprite.
        :type position: list

        """
        if not texture_path:
            texture_path = role.texture_path

        super(Actor, self).__init__(name, role.health,
                                    texture_path, self.batch,
                                    facing, movement, position)

        self._role = role
        self._attack = role.attack
        self._jump_height = role.jump_height
        self._inventory = role.inventory
        self._hostile = True if hasattr(role, 'hostile') else False

    # Attack
    @property
    def attack(self):
        """ Return the current attack for a specific Actor instance.

        :returns: int

        """
        return self._attack

    @attack.setter
    def attack(self, new_attack):
        """ Set the attack for a specific Actor instance to a new attack value.
        Checks ensure that the attack cannot below 0 and above the upper
        bounding attack for the Actor instance's role.

        :param new_attack: The new attack for the specific Actor instance.
        :type new_attack: int

        """
        if new_attack > 0 and new_attack <= self.role.attack:
            self._attack = new_attack

    # Jump Height
    @property
    def jump_height(self):
        """ Return the current jump_height for a specific Actor instance.

        :returns: int

        """
        return self._jump_height

    @jump_height.setter
    def jump_height(self, new_jump_height):
        """ Set the jump height for a specific Actor instance to a new jump
        height value. Checks ensure that the jump height cannot below 0 and
        above the upper bounding jump height for the Actor instance's role.

        :param new_jump height: The new jump height for the specific Actor
            instance.
        :type new_jump height: int

        """
        if new_jump_height > 0 and new_jump_height < self.role.jump_height:
            self._jump_height = new_jump_height

    # Inventory
    @property
    def inventory(self):
        """ Return the current inventory for a specific Actor instance.

        :returns: list

        """
        return self._inventory

    @inventory.setter
    def inventory(self, new_inventory_item):
        """ Append the provided item to an inventory for a specific Actor
        instance. Checks ensure that the item is not an Actor instance or a
        Role instance, allowing for a Block instance or an Item instance to be
        appended.

        :param new_inventory_item: The new item for the specific Actor
            instance's inventory.
        :type new_inventory_item: Entity

        """
        if not isinstance(item, Actor) and not isinstance(item, Role):
            self._inventory.append(item)

    # Hostile
    @property
    def hostile(self):
        """ Return the current hostile state for a specific Actor instance if
        its member Role instance is an instance of Enemy or NPC.

        :returns: bool

        """
        if str(role) == "Enemy" or str(role) == "NPC":
            return self._hostile

    @hostile.setter
    def hostile(self, new_hostile):
        """ Set the current hostile state for a specific Actor instance to a
        new hostile state. Checks ensure that the Actor instance's member Role
        instance is an instance of Enemy or NPC.

        :param new_hostile: The new hostile state for the specific Actor
            instance.
        :type new_hostile: bool

        """
        if str(role) == "Enemy" or str(role) == "NPC":
            self._hostile = new_hostile

    # Role
    @property
    def role(self):
        """ Return the member Role instance for a specific Actor instance.

        :returns: Role

        """
        return self._role
