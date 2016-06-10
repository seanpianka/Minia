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
    _uid = 1
    batch = pyglet.graphics.Batch()

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
        super(Block, self).__init__(name, texture_path, self.batch)

        self._id = self.uid
        self.uid += 1  # count of created actors

        self._solid = solid
        self._holdable = holdable

    # Unique ID count
    @property
    def uid(self):
        return self._uid

    @uid.setter
    def uid(self, new_uid):
        self._uid = new_uid

    # Block ID
    @property
    def id(self):
        return self._id

    @property
    def solid(self):
        return self._solid

    @property
    def holdable(self):
        return self._holdable
