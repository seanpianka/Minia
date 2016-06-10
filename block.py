"""
block
~~~~~

Container class for an "Material", an entity instance with properties shared
among all Blocks of that Material, makes up the terrain and world. It is
holdable and destrucible by the player (when its health reaches 0).

Create an object of the "material" subclass called "Material" and give it
attributes:
    WATER = Material(health=100, holdable=False, solid=False)
    WOOD = Material(health=100, holdable=True, solid=True)
Create a new Block and provide it the generic material of "WOOD" or "WATER".
    wood_243 = Block(material=WOOD, name="wood_243")
    water_1 = Block(material=WATER, name="water_1")

Composition model is simpler than using inheritance and many actor subclasses:
    See also: http://gameprogrammingpatterns.com/type-object.html

:author: Sean Pianka

"""
import pyglet

from entity import Entity

pyglet.resource.path = ["assets"]
pyglet.resource.reindex()

class Block(Entity, object):
    uid = Entity._uid
    batch = pyglet.graphics.Batch()

    def __init__(self, material, texture_path=None,
                 facing=[1, 1], movement=0, position=[0, 0]):
        """ Create a new block with associated texture, name, id, and
        properties as it refers to actor interactions.

        :param name: The name of the block.
        :type name: str

        :param texture: The path to the texture for the block.
        :type texture: str

        :param solid: A flag whether an actor may walk through the block.
        :type solid: bool

        :param holdable: A flag whether an actor may hold the block.
        :type holdable: bool

        """
        if not texture_path:
            texture_path = material.texture_path

        super(Block, self).__init__(material.family, material.health,
                                    texture_path, self.batch,
                                    facing, movement, position)

        #texture_path, solid=True, holdable=True
        self._material = material
        self._solid = material.solid
        self._holdable = material.holdable

    @property
    def solid(self):
        """ Return the current solid state for a specific Block instance.

        :returns: bool

        """
        return self._solid

    @property
    def holdable(self):
        """ Return the current holdable state for a specific Block instance.

        :returns: bool

        """
        return self._holdable
