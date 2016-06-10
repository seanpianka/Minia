"""
material
~~~~~~~~
"Attribute class", provide objects of material subclasses to Block objects to
create Block with specific properties.

Create an object of the "material" subclass called "Enemy" and give it attributes:
    WATER = Material(health=100, holdable=False, solid=False)
    WOOD = Material(health=100, holdable=True, solid=True)
Create a new Block and provide it the generic material of "WOOD" or "WATER".
    wood_243 = Block(material=WOOD, name="wood_243")
    water_1 = Block(material=WATER, name="water_1")

Composition model is simpler than using inheritance and many Block subclasses:
    See also: http://gameprogrammingpatterns.com/type-object.html

:author: Sean Pianka

"""
class Material:
    """ Defines implementation and generic behavior for all Blocks which are
    built from the specific material. Subclasses contain information that will
    be shared among Blocks which are built from the aforementioned material.

    """
    def __init__(self, family, health, durability,
                 texture_path, solid, holdable):
        """ Create a new Material with associated texture, name, id, and
        necessary properties.

        :param name: The name of the Material instance.
        :type name: str

        :param texture_path: The path to the texture for the Material instance.
        :type texture_path: str

        :param solid: A flag whether an Actor may walk through Block instance's
            composed of this Material instance or if other Block instance's can
            fall through this material.
        :type solid: bool

        :param holdable: A flag whether an Actor instance may hold the block
            in their inventory.
        :type holdable: bool

        """
        self._family = family
        self._health = health
        self._durability = durability
        self._texture_path = texture_path
        self._solid = solid
        self._holdable = holdable

    def __str__(self):
        return "{}: {}".format(self.__class__.__name__, self.family)

    # Family
    @property
    def family(self):
        """ Return the family name for the Material instance.

        :returns: str

        """
        return self._family

    # Health
    @property
    def health(self):
        """ Return the current health for the Material instance.

        :returns: int

        """
        return self._health

    # Durability
    @property
    def durability(self):
        """ Return the current durability for the Material instance.

        :returns: int

        """
        return self._durability

    # Texture Path
    @property
    def texture_path(self):
        """ Return the texture path for the Material instance.

        :returns: str

        """
        return self._texture_path

    # Solid
    @property
    def solid(self):
        """ Return the current solid state for a specific Block instance.

        :returns: bool

        """
        return self._solid

    # Holdable
    @property
    def holdable(self):
        """ Return the current holdable state for a specific Block instance.

        :returns: bool

        """
        return self._holdable

class Solid(Material, object):
    def __init__(self, family, health, durability,
                 texture_path):
        super(Solid, self).__init__(family, health,
                                    durability, texture_path,
                                    True, True)

class Liquid(Material, object):
    def __init__(self, family, health, durability,
                 texture_path):
        super(Liquid, self).__init__(family, health,
                                    durability, texture_path,
                                    False, False)

class Gas(Material, object):
    def __init__(self, family, health, durability,
                 texture_path):
        super(Gas, self).__init__(family, health,
                                    durability, texture_path,
                                    False, False)



