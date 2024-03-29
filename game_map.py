import numpy as np # type: ignore
from tcod.console import Console
import tile_types

class GameMap:
    def __init__(self, width: int, heigth: int):
        self.width, self.heigth = width, heigth
        self.tiles = np.full((width, heigth), fill_value=tile_types.wall, order="F")

    def in_bounds(self, x: int, y:int) -> bool:
        """Return True if x and y are inside of the bounds of this map."""
        return 0 <= self.width and 0 <= y < self.heigth
    
    def render(self, console: Console) -> None:
        console.tiles_rgb[0:self.width, 0:self.heigth] = self.tiles["dark"]