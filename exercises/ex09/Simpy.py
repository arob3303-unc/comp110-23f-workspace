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

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Finds if each index is equal to the same index of a list or a float value."""
        new_list: list[bool] = list()
        i: int = 0
        if type(rhs) is float:
            for x in self.values:
                if x == rhs:
                    new_list.append(True)
                else:
                    new_list.append(False)
        else:
            for x in self.values:
                if x == rhs.values[i]:
                    new_list.append(True)
                else:
                    new_list.append(False)
                i += 1
        return new_list
    
    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Finds if each index is equal or greater than to the same index of a different list or a float value."""
        new_list: list[bool] = list()
        i: int = 0
        if type(rhs) is float:
            for x in self.values:
                if x > rhs:
                    new_list.append(True)
                else:
                    new_list.append(False)
        else:
            for x in self.values:
                if x > rhs.values[i]:
                    new_list.append(True)
                else:
                    new_list.append(False)
                i += 1
        return new_list
    
    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Adds subscription notation support to objects of the class."""
        new_list: list[float] = list()
        i: int = 0
        if type(rhs) is int:    
            return self.values[rhs]
        else:
            for x in self.values:
                print(type(rhs))
                if type(rhs) is list:
                    if x > rhs[i] is True:
                        new_list.append(x)
                if type(rhs) is bool:
                    print(rhs)
                    if rhs is False:
                        new_list.append(x)
                i += 1
        return Simpy(new_list)
        
