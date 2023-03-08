from typing import Sequence
import pygame

from Ball import Ball
from BlockBase import BlockBase


class Paddle(BlockBase):
    """
    Class, representing paddle
    Attributes
    ----------
    width: float
        width of the paddle
    height: float
        height of teh paddle
    speed: float
        number of pixels the panel moves per frame while moving
    """
    def __init__(self, width: int, height: int, speed: float, screen_h: int, screen_w: int):
        """
        Parameters
        ----------
        width: int
            width of the paddle
        height: int
            height of the paddle
        speed: float
            number of pixels the panel moves per frame while moving
        screen_h:
            screen height in pixels
        screen_w: int
            screen width in pixels
        """
        self.width = width
        self.height = height
        self.speed = speed
        super().__init__(screen_w // 2 - width // 2, screen_h - height - 10, width, height)

    def process_keys(self, key: Sequence[bool], screen_width: int):
        """Update the paddle state based on the given user input.

            Args:
                key (pygame.key): The current state of the keyboard keys.
                screen_width (int): The width of the game screen, used to limit paddle movement.
        """
        if key[pygame.K_LEFT] and self.left > 0:
            self.left -= self.speed
        if key[pygame.K_RIGHT] and self.right < screen_width:
            self.right += self.speed

    def check_paddle_collision(self, ball: Ball):
        """Check if the ball collides with the given paddle and update the ball states accordingly.
            Args:
                ball (Ball): The ball object to check for collision.

            Returns:
                None: This method does not return anything, it only updates the paddle and/or ball states.
        """
        if ball.colliderect(self) and ball.direction_y > 0:
            self.process_collision(ball)

    pass
