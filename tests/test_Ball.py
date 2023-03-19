import unittest

from Ball import Ball


class TestBlock(unittest.TestCase):
    def setUp(self):
        self.ball = Ball(5, 5, 1200, 1200)
        self.ball.centerx = 1201
        self.ball.centery = 1
        self.ball.direction_x = 1

    def test_r_bounce(self):
        self.ball.check_bounds_collision(1200, 1200)
        self.assertEqual(self.ball.direction_x, -1)

    def test_l_bounce(self):
        self.ball.centerx = -1
        self.ball.direction_x = -1
        self.ball.check_bounds_collision(1200, 1200)
        self.assertEqual(self.ball.direction_x, 1)

    def test_g_bounce(self):
        self.ball.bottom = 1300
        self.ball.check_bounds_collision(1200, 1200)
        exit = self.ball.check_bounds_collision(1200, 1200)
        self.assertEqual(exit, True)

pass
