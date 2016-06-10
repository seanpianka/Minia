"""
entity
~~~~~~
Definition and implementation for anything that will be on the screen.
Anything, including an actor or a block, is an entity.

:author: Sean Pianka

"""
import pyglet

pyglet.resource.path = ["assets"]
pyglet.resource.reindex()


class Entity:
    def __init__(self, name, texture_path, texture_batch, movement=0, position=(0, 0)):
        self._name = name
        #  1 = Moving right, -1 = Moving left, 0 = Not moving
        #  Second element is the last movement, used for flipping
        self._movement = [movement, movement]
        # Current (x, y) position in the world, specified by floats
        self._position = position
        # Velocities in x axis and y axis
        self._dy = 0
        self._dx = 0
        self.texture = (texture_path, texture_batch)

    def move_to(self, x=None, y=None):
        """ Move to exact coordinates.

        """
        if isinstance(x, int):
            self.sprite.x = x
        if isinstance(y, int):
            self.sprite.y = y

    def move(self, x=None, y=None):
        """ Move to new coordinates based on provided offsets.

        """
        if isinstance(x, float):
            self.sprite.x += x
        if isinstance(y, float):
            self.sprite.y += y

    # Name
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if len(new_name) < 256:
            self._name = new_name

    # Texture
    @property
    def texture(self):
        return self._texture

    @texture.setter
    def texture(self, path_and_batch):
        """
        :param path_and_batch: Path to the asset and the batch to which the
            generated sprite should be added.
        :type path_and_batch: Tuple

        """
        # Create the anchor for where the sprite is drawn to be the
        #   center of the sprite.
        self._texture = pyglet.resource.image(path_and_batch[0])
        self._texture.anchor_x = self._texture.width/2

        self._sprite = pyglet.sprite.Sprite(self.texture,
                                            x=self.position[0],
                                            y=self.position[1],
                                            batch=path_and_batch[1])

    # Sprite
    @property
    def sprite(self):
        return self._sprite

    # Movement
    @property
    def movement(self):
        return self._movement

    @movement.setter
    def movement(self, new_movement):
        if new_movement in [-1, 0, 1]:
            if self._movement is not 0 and self._movement[0]*-1 is new_movement:
                self._movement[1] = self._movement[0]
                self.sprite.image = self.sprite.image.get_transform(flip_x=True)
            self._movement[0] = new_movement

    # Y-Axis Velocity
    @property
    def dy(self):
        return self._dy

    @dy.setter
    def dy(self, new_dy):
        self._dy = new_dy

    # X-Axis Velocity
    @property
    def dx(self):
        return self._dx

    @dx.setter
    def dx(self, new_dx):
        if new_dx > 0:
            self.movement = 1
        elif new_dx < 0:
            self.movement = -1
        else:
            self.movement = 0
        self._dx = new_dx

    # Position
    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, new_position):
        if isinstance(new_position, tuple) and len(new_position) is 2:
            self._position = new_position
