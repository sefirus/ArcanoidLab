import unittest
import pygame
from Ball import Ball
from Paddle import Paddle

class TestBlock(unittest.TestCase):
    def setUp(self):
        self.ball = Ball(5, 5, 1200, 1200)
        self.paddle = Paddle(330, 35, 5, 1200, 1200)
    def test_direction_y_neg(self):
        self.ball.direction_y = -1
        self.paddle.check_paddle_collision(self.ball)
        self.assertFalse(self.paddle.process_collision(self.ball))
    def test_keys_not_pressed(self):
        key = {pygame.K_LEFT: False, pygame.K_RIGHT: False}
        self.paddle.left = 50
        self.paddle.process_keys(key, 1200)
        self.assertEqual(self.paddle.left, 50)
    def test_left_key_pressed(self):
        key = {pygame.K_LEFT: True, pygame.K_RIGHT: False}
        self.paddle.left = 50
        self.paddle.process_keys(key, 1200)
        self.assertEqual(self.paddle.left, 45)
    def test_left_key_pressed_b(self):
        key = {pygame.K_LEFT: True, pygame.K_RIGHT: False}
        self.paddle.left = 0
        self.paddle.process_keys(key, self.paddle.width)
        self.assertEqual(self.paddle.left, 0)
    def test_right_key_pressed(self):
        key = {pygame.K_LEFT: False, pygame.K_RIGHT: True}
        self.paddle.right = 50
        self.paddle.process_keys(key, self.paddle.width)
        self.assertEqual(self.paddle.right, 55)
    def test_right_key_pressed_b(self):
        key = {pygame.K_LEFT: False, pygame.K_RIGHT: True}
        self.paddle.right = 330
        self.paddle.process_keys(key, self.paddle.width)
        self.assertEqual(self.paddle.right, 330)
pass
