class World(object):
    def __init__(self):
        self.level = None
        self.entities = None
        self.player = None

    def new_world(self, width, height):
        pass

    @property
    def player(self):
        return self.player

    @player.setter
    def player(self, player):
        self.player = player
