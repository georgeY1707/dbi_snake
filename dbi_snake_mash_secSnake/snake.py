import pygame as pg


class Snake:
    def __init__(self, screen, width, height, tile,
                 key={'up': pg.K_UP, 'down': pg.K_DOWN, 'left': pg.K_LEFT, 'right': pg.K_RIGHT}, color='yellow'):
        self.angle = 0
        self.width = width
        self.height = height
        self.tile = tile
        self.screen = screen
        self.x = self.width // 2
        self.y = self.height // 2
        self.lx = self.x
        self.ly = self.y + self.tile
        self.tail = [[self.lx, self.ly], [self.x, self.ly + self.tile]]
        self.color = color
        self.key = key

    def step(self):
        self.lx, self.ly = self.x, self.y
        if self.angle == 1:
            if self.x != self.width - self.tile:
                self.x += self.tile
            else:
                self.x = 0
        elif self.angle == 3:
            if self.x != 0:
                self.x -= self.tile
            else:
                self.x = self.width - self.tile
        elif self.angle == 0:
            if self.y != 0:
                self.y -= self.tile
            else:
                self.y = self.height - self.tile
        elif self.angle == 2:
            if self.y != self.height - self.tile:
                self.y += self.tile
            else:
                self.y = 0
        self.tail = [[self.lx, self.ly]] + self.tail[:-1]

    def control(self):
        keys = pg.key.get_pressed()
        if keys[self.key['up']]:
            if self.angle != 2:
                self.angle = 0
                print('up pressed')
        if keys[self.key['down']]:
            if self.angle != 0:
                self.angle = 2
        if keys[self.key['left']]:
            if self.angle != 1:
                self.angle = 3
        if keys[self.key['right']]:
            if self.angle != 3:
                self.angle = 1
        self.step()

    def draw(self):
        for elem in self.tail:
            pg.draw.rect(self.screen, self.color, (elem[0], elem[1], self.tile, self.tile))