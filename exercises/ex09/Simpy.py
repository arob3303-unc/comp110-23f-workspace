"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730717463"


class Simpy:
    """Simpy Class."""
    # Attributes
    values: list[float]

    # TODO: Your constructor and methods will go here.

    def __init__(self, list_values: list[float]):
        """Returns float values."""
        self.values = list_values
    

    def __str__(self) -> str:
        """Returns a readable str."""
        msg: str = (f"Simply({self.values})")
        return msg
   
    
    def fill(self, num: float, amount: int) -> None:
        """Makes a list with float numbers."""
        # loop to append values
        for i in range(amount):
            self.values.append(num)
        
        return None

    def arange(self, start: float, stop: float, step: float = 1.0):
        """Fill in the values attribute with a range of values."""
        assert step != 0.0
        num = start
        i1: int = 0
        i2: int = 0
        self.values.append(num)
        
        if (step - 1) < step:
            while i1 < stop - step:
                num += step
                self.values.append(num)
                i1 += step
        if (step - 1) > step:
            while i2 < stop - step:
                num += step
                self.values.append(num)
                i2 += step

            

        
twos = Simpy([])
twos.arange(-1.0, -5.0, -1.0)
print(twos)

step = -1
start = -1

print(start + step)