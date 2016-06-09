"""
block
~~~~~
desc

:author: Sean Pianka

"""
import pyglet

from entity import Entity

pyglet.resource.path = ["assets"]
pyglet.resource.reindex()

class Block(Entity, object):
    uid = 1

    def __init__(self, name, texture_path, solid=True, holdable=True):
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
        super(Block, self).__init__(name, texture_path)
        self.uid += 1

        self._solid = solid
        self._holdable = holdable

    @property
    def solid(self):
        return self._solid

    @property
    def holdable(self):
        return self._holdable
