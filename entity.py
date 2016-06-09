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

entities_batch = pyglet.graphics.Batch()

class Entity:
    def __init__(self, name, texture_path, movement=0, position=(0, 0)):
        self._name = name

        #  1 = Moving right, -1 = Moving left, 0 = Not moving
        self._movement = movement
        # Current (x, y) position in the world, specified by floats
        self._position = position
        # Velocities in x axis and y axis
        self._dy = 0
        self._dx = 0

        self.texture = texture_path

    def move_to(self, x=None, y=None):
        if x:
            self.sprite.x = x
        if y:
            self.sprite.y = y

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
    def texture(self, new_texture_path):
        self._texture = pyglet.resource.image(new_texture_path)
        self._texture.anchor_x = self._texture.width/2

        self._sprite = pyglet.sprite.Sprite(
            self.texture,
            x=self.position[0],
            y=self.position[1],
            batch=entities_batch
        )

    # Sprite
    @property
    def sprite(self):
        return self._sprite

    # Movement
    @property
    def movement(self):
        return self.movement

    @movement.setter
    def movement(self, new_movement):
        if new_movement in range(-1, 2):
            self._movement = new_movement

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
        self._dx = new_dx

    # Position
    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, new_position):
        if isinstance(new_position, tuple) and len(new_position) is 2:
            self._position = new_position
