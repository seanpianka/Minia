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

from pyglet.gl import *
from pyglet.window import key, mouse

from assets import *
from constants import *


# Rendering test sprites onto the screen.
t_x = 32
t_y = 32
for i in range(MAX_ROWS):
    for j in range(MAX_COLS):
        if j < MAX_COLS / 3:
            print("stone")
            BLOCKS.append(Block(material=MATERIALS["Stone"], position=[i*t_x, j*t_x]))
        elif j < MAX_COLS - 1:
            print("dirt")
            BLOCKS.append(Block(material=MATERIALS["Dirt"], position=[i*t_x, j*t_x]))
        else:
            print("grass")
            BLOCKS.append(Block(material=MATERIALS["Grass"], position=[i*t_x, j*t_x]))
PLAYERS[0].move_to(x=500, y=GROUND_LEVEL)
PLAYERS[1].move_to(x=466, y=GROUND_LEVEL)


class MiniaGame(pyglet.window.Window, object):
    def __init__(self, *args, **kwargs):
        super(MiniaGame, self).__init__(*args, **kwargs)

        # Set RGBA color of the sky
        glEnable(GL_BLEND)
        glClearColor(0.5, 0.69, 1.0, 1)
        # Flag for locking cursor inside of spawned window
        self.active = PLAYERS[0]
        self.exclusive = False
        self.schedule = pyglet.clock.schedule_interval(self.update, 1.0/60.0)
        self.fps_display = pyglet.clock.ClockDisplay()

    def render(self):
        self.clear()
        glClearColor(0.5, 0.69, 1.0, 1)
        # What's drawn latest is on top
        Block.batch.draw()
        Actor.batch.draw()
        self.flip()

    def on_draw(self):
        self.render()

    def on_key_press(self, symbol, modifiers):
        if symbol == key.A:
            self.active.dx = -SPEED
            self.active.dy = 0
        if symbol == key.D:
            self.active.dx = SPEED
            self.active.dy = 0
        if symbol == key.W:
            self.active.dx = 0
            self.active.dy = SPEED
        if symbol == key.S:
            self.active.dx = 0
            self.active.dy = -SPEED

    def on_key_release(self, symbol, modifiers):
        if symbol == key.A:
            self.active.dx = 0
            self.active.dy = 0
        if symbol == key.D:
            self.active.dx = 0
            self.active.dy = 0
        if symbol == key.W:
            self.active.dx = 0
            self.active.dy = 0
        if symbol == key.S:
            self.active.dx = 0
            self.active.dy = 0

    def update(self, dt):
        self.active.move(x=self.active.dx * dt, y=self.active.dy * dt)

    def main_loop(self):
        pass
        #while not self.has_exit:
        #    self.dispatch_events('on_draw')
        #    self.flip()


def main(width, height):
    window = MiniaGame(width=width, height=height, vsync=0, caption="Minia", resizable=True)
    window.set_exclusive_mouse(True)
    #window.main_loop()
    pyglet.app.run()


if __name__ == "__main__":
    main(width=1280, height=720)
