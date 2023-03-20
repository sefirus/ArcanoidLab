import pygame
from random import randrange as rnd


class Ball(pygame.Rect):
    """
    Class, representing flying ball
    Attributes
    ----------
    direction_x: int
        Can be 1(->) or -1(<-). Represents horizontal direction of the ball
    direction_y: int
        Can be 1(v) or -1(^). Represents vertical direction of the ball
    radius: int
        radius of the ball
    speed: float
        number of pixels the block moves along each axis per frame while moving
    box_dimension: float
        diagonal size of ball`s box
    """
    def __init__(self, radius: int, default_speed: int,  screen_h: int, screen_w: int):
        """
        Constructor
        Parameters
        ----------
        radius: int
            radius of the ball
        default_speed: int
            default number of pixels the block moves on each axe per frame while moving
        screen_h:
            screen height in pixels
        screen_w: int
            screen width in pixels
        """
        self.direction_x = 1
        self.direction_y = -1
        self.radius = radius
        self.speed = default_speed
        self.box_dimension = int(radius * 2 ** 0.5)
        super().__init__(rnd(self.box_dimension, screen_h - self.box_dimension), screen_w // 2, self.box_dimension,
                         self.box_dimension)

    def check_bounds_collision(self, screen_width: int, screen_height: int):
        """Check if the ball collides with the screen boundaries and update its direction and/or state accordingly.

        Args:
            screen_width (int): The width of the game screen in pixels.
            screen_height (int): The height of the game screen in pixels.

        Returns:
            bool: Returns True if the ball collides with the bottom of the screen, indicating that the game is over.
                  Otherwise, returns False
        """
        if self.centerx < self.radius - self.speed \
                or self.centerx > screen_width - self.radius + self.speed:
            self.direction_x = -self.direction_x
        if self.centery < self.radius - self.speed:
            self.direction_y = -self.direction_y
        if self.bottom > screen_height:
            print('Game over!')
            return True
        return False

    def move_to_next_frame(self):
        """Update the ball position based on its speed and direction.

            Returns:
                None: This method does not return anything, it only updates the ball position.
        """
        self.x += self.speed * self.direction_x
        self.y += self.speed * self.direction_y

    pass
