"""Point Class with x, y as attributes."""
from __future__ import annotations

__author__ = "730717463"


class Point:
    """Point Class - Graph Coordinates."""
    x: float
    y: float

    def __init__(self, x_init: float = 0.0, y_init: float = 0.0) -> None:
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

    def __str__(self) -> str:
        """The str method for printing x and y."""
        msg: str = (f"x: {self.x}; y: {self.y}")
        return msg
    
    def __mul__(self, factor: int | float) -> Point:
        """The multiplcation overload operator."""
        new_point: Point = Point(self.x * factor, self.y * factor)
        return new_point
        
    def __add__(self, factor: int | float) -> Point:
        """The add overload operator."""
        new_point: Point = Point(self.x + factor, self.y + factor)
        return new_point
