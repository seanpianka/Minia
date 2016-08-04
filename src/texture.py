class Texture(object):
    def __init__(self, texture):
        self.texture = texture
        self.parent = None

    def set_state(self):
        glEnable(self.texture.target)
        glBindTexture(self.texture.target, self.texture.id)

    def unset_state(self):
        glDisable(self.texture.target)
