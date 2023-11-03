"""Point Class with x, y as attributes."""
from __future__ import annotations

__author__ = "730717463"


class Point:
    """Point Class - Graph Coordinates."""
    x: float
    y: float

    def __init__(self, x_init: float, y_init: float) -> float:
        """Assigns attributes as __init__."""
        self.x = x_init
        self.y = y_init

    def scale_by(self, factor: int) -> None:
        """Updates Point with updated attribute values by a factor."""
        self.x *= factor
        self.y *= factor

    def scale(self, factor: int) -> Point:
        """Creates a new point."""
        new_point: Point = Point(self.x * factor, self.y * factor)
        return new_point