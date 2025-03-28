import sys
import pygame as pg
from random import randrange
from apple import Apple
from snake import Snake
from mashroom import Mashroom


class Game:
    def __init__(self):
        pg.init()
        self.width, self.height = 600, 600
        self.screen = pg.display.set_mode((self.width, self.height))
        self.speed = 10
        self.tile = self.height // 30

        self.snake = Snake(self.screen, self.width, self.height, self.tile) # здесь не передаём параметр key, т.к.
        # используем клавиши по дефолту из класса и цвет тоже

        self.snake2 = Snake(self.screen, self.width, self.height, self.tile,
                            key={'up': pg.K_w, 'down': pg.K_s, 'left': pg.K_a, 'right': pg.K_d}, color='red')
        self.apple = Apple(self.screen, self.width, self.height, self.tile)

        col_mashrooms = 10
        self.mashrooms = [Mashroom(self.screen, self.width, self.height, self.tile) for _ in range(col_mashrooms)]

        self.bg_color = '#778899' # цвет поля
        MOVE_DOWN_DELAY = 500
        MOVE_DOWN_EVENT = pg.USEREVENT + 1
        pg.time.set_timer(MOVE_DOWN_EVENT, MOVE_DOWN_DELAY)
        self.running = True

    def new_mashroom(self):
        if (self.snake.x, self.snake.y) in [(elem.x, elem.y) for elem in self.mashrooms]:
            while ((self.snake.x, self.snake.y) in [(elem.x, elem.y) for elem in self.mashrooms]
                   or (self.apple.x, self.apple.y) in [(elem.x, elem.y) for elem in self.mashrooms]):
                for elem in self.mashrooms:
                    if (self.snake.x == elem.x and self.snake.y == elem.y
                            and [elem.x, elem.y] not in self.snake.tail):
                        index = self.mashrooms.index(elem)
                self.mashrooms[index].x = randrange(0, self.width - self.tile, self.tile)
                self.mashrooms[index].y = randrange(0, self.height - self.tile, self.tile)
            if len(self.snake.tail) > 2:
                self.snake.tail.pop()
        #отрисовка гриба
        for elem in self.mashrooms:
            elem.draw()

    def new_apple(self):
        if self.snake.x == self.apple.x and self.snake.y == self.apple.y:
            while (self.apple.x == self.snake.x and self.apple.y == self.snake.y
                   or [self.apple.x, self.apple.y] in self.snake.tail):
                self.apple.x = randrange(0, self.width - self.tile, self.tile)
                self.apple.y = randrange(0, self.height - self.tile, self.tile)
            self.snake.tail = [[self.snake.lx, self.snake.ly]] + self.snake.tail
        # отрисовка яблока
        self.screen.blit(self.apple.img, (self.apple.x, self.apple.y))

    def run(self):
        clock = pg.time.Clock()
        self.new_apple()
        self.new_mashroom()

        while self.running:
            # Обработка событий Pygame
            for event in pg.event.get():
                if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                    self.running = False

            # Обновление состояния
            self.screen.fill(self.bg_color)

            self.snake.control()
            self.snake2.control()
            self.new_apple()
            self.new_mashroom()

            self.snake.draw()
            self.snake2.draw()

            # Отрисовка
            pg.display.update()
            clock.tick(self.speed)

        pg.quit()
        sys.exit()


game = Game()
game.run()