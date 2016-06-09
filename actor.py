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
    def __init__(self, role, name, texture_path, movement=0, position=(0, 0)):
        super(Actor, self).__init__(name, texture_path)

        self._role = role
        self._health = role.health
        self._attack = role.attack
        self._jump_height = role.jump_height
        self._inventory = role.inventory
        self._hostile = True if hasattr(role, 'hostile') else False

    # Health
    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, new_health):
        if new_health > 0 and new_health < self.role.health:
            self._health = new_health

    # Attack
    @property
    def attack(self):
        return self._attack

    @attack.setter
    def attack(self, new_attack):
        if new_attack > 0 and new_attack < self.role.attack:
            self._attack = new_attack

    # Jump Height
    @property
    def jump_height(self):
        return self._jump_height

    @jump_height.setter
    def jump_height(self, new_jump_height):
        if new_jump_height > 0 and new_jump_height < self.role.jump_height:
            self._jump_height = new_jump_height

    # Inventory
    @property
    def inventory(self):
        return self._inventory

    @inventory.setter
    def inventory(self, new_inventory_item):
        self._inventory.append(item)


    # Hostile
    @property
    def hostile(self):
        return self._hostile

    @hostile.setter
    def hostile(self, new_hostile):
        if str(role) == "Enemy" or str(role) == "NPC":
            self._hostile = new_hostile

    # Role
    @property
    def role(self):
        return self._role
