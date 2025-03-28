## Микротаски:

1. Поганки (extends от класса Apple) *6

2. Препятствия (Змейка ударяется в стены как препятствие) --- Рекорды (объединить команды, чтоб одни сделали смерть, 
другие - рекорды) *4 *4

3. Раскраска змеи или поля (2 строки) *1

4. За каждое яблоко увеличивается скорости *3

5. Змея не может сама себя кусать *4

6. Порталы *7

7. сделать голову другим рисунком *2

8. регулировка скорости (нажатие на кнопки)

9. сделать вторую змейку *5
 
### Примечания
Цифры после звёздочки это уровень сложности от 1 до 10


## ЧТО НУЖНО:

- [PyCharm Community Edition](https://www.jetbrains.com/pycharm/download/?section=windows)

- [библиотека pygame](https://pypi.org/project/pygame/) ```pip install pygame```

- [python 3.12.8](https://www.python.org/downloads/)

- если делать пункт 5, то нудно сделать ```pip install tkinter``` 
(ткинтер обычно предустановленная библиотека но всё же стоит проверить)

## Код:
- код содержится в main.py
- картинка apple.png должна лежать в одном катологе с main.py иначе не будет ничего работать

```
import sys
import pygame as pg
from random import randrange


class Apple:
    def __init__(self, game):
        self.game = game
        self.x = 0
        self.y = 0
        self.img = self.get_image()

    def get_image(self):
        im = pg.image.load('apple.png')
        im = pg.transform.scale(im, (self.game.tile, self.game.tile))
        return im

    def draw(self):
        self.game.screen.blit(self.img, (self.x, self.y))


class Snake:
    def __init__(self, game):
        self.game = game
        self.angle = 0
        self.x = game.width // 2
        self.y = game.height // 2
        self.lx = self.x
        self.ly = self.y + self.game.tile
        self.tail = [[self.lx, self.ly], [self.x, self.ly + self.game.tile]]
        self.color = '#fff200'

    def step(self):
        self.lx, self.ly = self.x, self.y
        if self.angle == 1:
            if self.x != self.game.width - self.game.tile:
                self.x += self.game.tile
            else:
                self.x = 0
        elif self.angle == 3:
            if self.x != 0:
                self.x -= self.game.tile
            else:
                self.x = self.game.width - self.game.tile
        elif self.angle == 0:
            if self.y != 0:
                self.y -= self.game.tile
            else:
                self.y = self.game.height - self.game.tile
        elif self.angle == 2:
            if self.y != self.game.height - self.game.tile:
                self.y += self.game.tile
            else:
                self.y = 0
        self.tail = [[self.lx, self.ly]] + self.tail[:-1]

    def draw(self):
        self.step()
        for elem in self.tail:
            pg.draw.rect(self.game.screen, self.color, (elem[0], elem[1], self.game.tile, self.game.tile))


class Game:
    def __init__(self):
        pg.init()
        self.width, self.height = 600, 600
        self.screen = pg.display.set_mode((self.width, self.height))
        self.speed = 15
        self.tile = 20
        self.snake = Snake(self)
        self.apple = Apple(self)

        self.bg_color = '#778899'
        MOVE_DOWN_DELAY = 500
        MOVE_DOWN_EVENT = pg.USEREVENT + 1
        pg.time.set_timer(MOVE_DOWN_EVENT, MOVE_DOWN_DELAY)
        self.running = True

    def new_apple(self):
        if self.snake.x == self.apple.x and self.snake.y == self.apple.y:
            while self.apple.x == self.snake.x and self.apple.y == self.snake.y or [self.apple.x, self.apple.y] in self.snake.tail:
                self.apple.x = randrange(0, self.width - self.tile, self.tile)
                self.apple.y = randrange(0, self.height - self.tile, self.tile)
            self.snake.tail = [[self.snake.lx, self.snake.ly]] + self.snake.tail
        self.apple.draw()

    def control(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_UP] or keys[pg.K_w]:
            if self.snake.angle != 2:
                self.snake.angle = 0
        if keys[pg.K_DOWN] or keys[pg.K_s]:
            if self.snake.angle != 0:
                self.snake.angle = 2
        if keys[pg.K_LEFT] or keys[pg.K_a]:
            if self.snake.angle != 1:
                self.snake.angle = 3
        if keys[pg.K_RIGHT] or keys[pg.K_d]:
            if self.snake.angle != 3:
                self.snake.angle = 1

    def run(self):
        clock = pg.time.Clock()
        self.new_apple()

        while self.running:
            # Обработка событий Pygame
            for event in pg.event.get():
                if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                    self.running = False

            # Обновление состояния
            self.control()
            self.screen.fill(self.bg_color)
            self.snake.draw()
            self.new_apple()

            # Отрисовка
            pg.display.update()
            clock.tick(self.speed)  # 15 FPS

        pg.quit()
        sys.exit()


game = Game()
game.run()
```


