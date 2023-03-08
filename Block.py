from random import randrange as rnd
from BlockBase import BlockBase


class Block(BlockBase):
    """
    Class, representing one of the blocks at the top
    Attributes
    ----------
    width: float
        width of the block
    height: float
        height of the bloch
    color: tuple[int, int, int]
        color of the block
    """
    def __init__(self, poz_x: int, poz_y: int, cols: int, screen_width: int):
        """
        Args:
        poz_x: int
            x position of the block in the grid
        poz_y: int
            y position of the block in the grid
        cols: int
            number of columns in the grid
        """
        block_height = 50
        block_width = (screen_width - cols * 20) / cols
        super().__init__(10 + (block_width + 20) * poz_x, 10 + (block_height + 20) * poz_y, block_width, block_height)
        self.color = (rnd(30, 156), rnd(30, 256), rnd(30, 156))

    pass
