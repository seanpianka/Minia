# FPS
TICK_CYCLE = 60
FLYING_SPEED = 15
GRAVITY = 20.0
MAX_JUMP_HEIGHT = 1.0 # slightly higher than the height of a block
# formula for calculating jump speed:
# v_final = v_initial + accel * time_elapsed
# time = v_initial / accel
# displacement = initial_displacement + v_initial * time + (accel * time^2) / 2
JUMP_SPEED = math.sqrt(2 * GRAVITY * MAX_JUMP_HEIGHT)
TERMINAL_VELOCITY = 49
PLAYER_HEIGHT = 2


def square_vertices(x, y, n):
    """ Return the vertices of a square (block) at position x, y with size 2*n

    """
    vertex_data = []
    texture_date = []
    for row in range(rows):
        y2 = y1 + height
        x1 = x
        for col in range(cols):
            x2 = x1 + width
            vertex_data.extend(x1, y1, x2, y1, x2, y2, x1, x2)
            texture_data.extend(tex.tex_coords)
            x1 = x2
        y1 = y2
    return vertex_data, texture_data

    #return [[x-n, y-n],  # bottom-left
    #        [x+n, y-n],  # bottom-right
    #        [x-n, y+n],  # top-right
    #        [x+n, y+n]]  # top-left

vertex_data, texture_data = gen_vertex(0, 0)
v = batch


class WorldGenerator(object):
    def __init__(self, width, height):
        self.x_width = width
        self.y_height = height

    def generate(self):
        pass
        #world = [[None for x in range(self.
