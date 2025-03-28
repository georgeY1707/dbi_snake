import pygame as pg
from random import randrange


class Apple:
    def __init__(self, screen, width, height, tile):
        self.width = width
        self.height = height
        self.tile = tile
        self.screen = screen
        self.x = randrange(0, self.width - self.tile, self.tile)
        self.y = randrange(0, self.height - self.tile, self.tile)
        self.img = self.get_image()

    def get_image(self):
        im = pg.image.load('resource/apple.png')
        im = pg.transform.scale(im, (self.tile, self.tile))
        return im

    def draw(self):
        self.screen.blit(self.img, (self.x, self.y))