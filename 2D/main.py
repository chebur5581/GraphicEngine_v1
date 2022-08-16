import pygame as pg
import numpy as np
import math

class App():
    def __init__(self, WIDTH=1300, HEIGHT=700):
        pg.init()
        self.screen = pg.display.set_mode([WIDTH, HEIGHT])
        self.clock = pg.time.Clock()

    def run(self):
        while True:
            self.screen.fill((50, 50, 50))
            [exit() for i in pg.event.get() if i.type == pg.QUIT]

            pg.display.set_caption(str(self.clock.get_fps()))

            pg.display.flip()
            self.clock.tick(60)


if __name__ == '__main__':
    app = App()
    app.run()