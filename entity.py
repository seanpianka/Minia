"""
entity
~~~~~~
Definition and implementation for anything that will be on the screen.
Anything, including an actor or a block, is an entity.

:author: Sean Pianka

"""
import pyglet
from unique_id import UniqueID

pyglet.resource.path = ["assets"]
pyglet.resource.reindex()


class Entity(UniqueID):
    _uid = UniqueID._uid
    def __init__(self, name, health, texture_path, texture_batch,
                 facing=[1, 1], movement=0, position=[0, 0]):
        """ Intialize a new instance of something that can be rendered to the
        screen.

        :param name: The name of of the Entity instance.
        :type name: str

        :param health: The health of the Entity instance.
        :type health: int

        :param texture_path: The path from CWD to the texture file.
        :type texture_path: str

        :param texture_batch: The batch for the sprite to be added to.
        :type texture_batch: pyglet.graphics.Batch

        :param facing: The first element indicates which direction the texture
            is initally facing on the x-axis. -1 to indicate leftward facing
            and 1 to indicate rightward facing.
            The second element indicates which direction the texture is
            initally facing on the y-axis. -1 to indicate upward (regular)
            facing or 1 to indicate upside-down facing.
        :type facing: list (int, int)

        :param movement: Which direction the entity is initially moving. 0 to
            indicate it is stopped, -1 to indicate leftward movement, and 1 to
            indicate rightward movement.
        :type movement: int

        :param position: A tuple of the (x, y) initial coordinates of the
            sprite.
        :type position: list

        """
        self._id = self.uid
        self.uid += 1

        self._name = name
        self._health = health
        # 1 = Moving right, -1 = Moving left, 0 = Not moving
        # Second element is the last movement, used for flipping. It is
        #   defaulted to facing[0] so that the first movement of the player
        #   in either direction won't unnecessarily flip the texture
        self._movement = [movement, facing[0]]
        # Current (x, y) position in the world, specified by floats
        self._position = position
        # Velocities in x axis and y axis
        self._dy = 0
        self._dx = 0
        self._facing = facing
        self.texture = (texture_path, texture_batch)

    # Name
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if len(new_name) < 256:
            self._name = new_name

    # Health
    @property
    def health(self):
        """ Return the current health for a specific Entity instance.

        :returns: int

        """
        return self._health

    @health.setter
    def health(self, new_health):
        """ Set the health for a specific Entity instance to a new health value.
        Checks ensure that the health cannot below 0 and above the upper
        bounding health for the Entity instance's role.

        :param new_health: The new health for the specific Entity instance.
        :type new_health: int

        """
        if new_health >= 0 and new_health <= self.role.health:
            self._health = new_health

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

    # Facing
    @property
    def facing(self):
        return self._facing

    def flip(self, x=False, y=False):
        if x:
            self.facing[0] *= -1
            self.sprite.image = self.sprite.image.get_transform(flip_x=True)
        if y:
            self.facing[1] *= -1
            self.sprite.image = self.sprite.image.get_transform(flip_y=True)

    # Movement
    @property
    def movement(self):
        return self._movement

    @movement.setter
    def movement(self, new_movement):
        if new_movement in [-1, 0, 1]:
            if (new_movement is not self._movement[1] and
                new_movement is not 0):
                self._movement[1] = self._movement[0] = new_movement
                self.flip(x=True)
            else:
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
