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

        i: float = start
        plus_num: float = start

        while (i < (start - (stop))) or (i < stop):

            if (step - step) < (step + step):
                self.values.append(plus_num)
                plus_num += step
                i += step

            if (step - step) > (step + step):
                self.values.append(plus_num)
                plus_num += step
                i -= step
        
        if self.values and self.values[-1] >= stop:
            self.values.pop()

    def sum(self) -> float:
        """Sums all values in self.values list."""
        return sum(self.values)

    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Adds a number to each value in the Simpy list."""
        new_list: list[float] = list()
        i: int = 0
        if type(rhs) is float:
            for i in self.values:
                new_list.append(rhs + i)
        else:
            assert len(self.values) == len(rhs.values)
            for x in self.values:
                new_list.append(x + rhs.values[i])
                i += 1

        return new_list

    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Exponentiation the value of lists."""
        new_list: list[float] = list()
        i: int = 0
        if type(rhs) is float:
            for i in self.values:
                new_list.append(i ** rhs)
        else:
            assert len(self.values) == len(rhs.values)
            for x in self.values:
                new_list.append(x ** rhs.values[i])
                i += 1

        return new_list
    
    


a = Simpy([1.0, 1.0, 1.0])
#print(a + 10.0)
b = Simpy([2.0, 3.0, 4.0])
c = a + b
print(c)
