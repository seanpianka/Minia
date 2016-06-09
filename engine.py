"""
engine
~~~~~~
Manages the rendering of objects and the physics calculations.

:author: Sean Pianka

"""
import math
import random
import time
import pyglet
import pprint

from collections import deque
from pyglet import image
from pyglet.gl import *
from pyglet.graphics import TextureGroup
from pyglet.window import key, mouse

from assets import *
from constants import *


# Rendering 6 blocks in positions around the screen.
all_blocks = list(BLOCKS.values())

t_x = 100
t_y = 100
for i in range(0, len(all_blocks)):
    all_blocks[i].move_to(x=t_x, y=t_y)
    print("Adding", str(all_blocks[i].name))
    t_x += 40
    t_y += 40
    i += 1

ACTORS['Player_1'].move_to(x=500, y=250)



class Window(pyglet.window.Window, object):
    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)

        # Set RGBA color of the sky
        glEnable(GL_BLEND)
        glClearColor(0.5, 0.69, 1.0, 1)
        # Flag for locking cursor inside of spawned window
        self.exclusive = False
        self.batch = pyglet.graphics.Batch()

    def render(self):
        self.clear()
        glClearColor(0.5, 0.69, 1.0, 1)
        entities_batch.draw()
        self.flip()

    def on_draw(self):
        self.render()

    def update(dt):
        pass

    def run(self):
        while True:
            event = self.dispatch_events()
            self.render()

def main():
    window = Window(width=1280, height=720, vsync=0, caption="Minia", resizable=True)
    window.set_exclusive_mouse(True)
    window.fps_display = pyglet.clock.ClockDisplay()
    window.fps_display.draw()

    pyglet.clock.set_fps_limit(60)
    pyglet.clock.schedule_interval(window.update, 1/60)
    window.run()


if __name__ == "__main__":
    main()
