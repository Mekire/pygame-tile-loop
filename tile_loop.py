import os
import sys
import itertools
import pygame as pg

class ArgumentError(Exception):
    pass

if len(sys.argv) != 3:
    raise ArgumentError("Must be called with filename and size arguments.")

FILENAME,SIZE = sys.argv[1],int(sys.argv[2])


class Control(object):
    def __init__(self):
        self.screen = pg.display.get_surface()
        self.screen_rect = self.screen.get_rect()
        self.clock = pg.time.Clock()
        self.done = False
        self.fps = 60.0

    def event_loop(self):
        for event in pg.event.get():
            keys = pg.key.get_pressed()
            if event.type == pg.QUIT or keys[pg.K_ESCAPE]:
                self.done = True

    def update(self):
        for i,j in itertools.product(range(SIZE),repeat=2):
            self.screen.blit(TILE,(i*TILE_WIDTH,j*TILE_HEIGHT))

    def main_loop(self):
        while not self.done:
            self.event_loop()
            self.update()
            pg.display.update()
            self.clock.tick(self.fps)


if __name__ == "__main__":
    os.environ["SDL_VIDEO_CENTERED"] = '1'
    pg.init()
    TILE = pg.image.load(FILENAME)
    TILE_WIDTH,TILE_HEIGHT = TILE.get_size()
    pg.display.set_mode((TILE_WIDTH*SIZE,TILE_HEIGHT*SIZE))
    run_it = Control()
    run_it.main_loop()
    pg.quit()
    sys.exit()