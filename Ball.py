import pygame
from random import randrange as rnd

from Paddle import Paddle


class Ball(pygame.Rect):

    def __init__(self, radius: int, default_speed: int,  screen_h: int, screen_w: int):
        self.direction_x = 1
        self.direction_y = -1
        self.radius = radius
        self.speed = default_speed
        self.box_dimension = int(radius * 2 ** 0.5)
        super().__init__(rnd(self.box_dimension, screen_h - self.box_dimension), screen_w // 2, self.box_dimension,
                         self.box_dimension)

    def check_bounds_collision(self, screen_width: int, screen_height: int):
        if self.centerx < self.radius - self.speed \
                or self.centerx > screen_width - self.radius + self.speed:
            self.direction_x = -self.direction_x
        if self.centery < self.radius - self.speed:
            self.direction_y = -self.direction_y
        if self.bottom > screen_height:
            print('Game over!')
            exit()

    def check_paddle_collision(self, paddle: Paddle):
        if self.colliderect(paddle) and self.direction_y > 0:
            paddle.process_collision(self)

    def move_to_next_frame(self):
        self.x += self.speed * self.direction_x
        self.y += self.speed * self.direction_y

    pass
