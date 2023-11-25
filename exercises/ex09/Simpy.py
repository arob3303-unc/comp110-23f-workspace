"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730717463"


class Simpy:
    """Simpy Class."""
    # Attributes
    values: list[float]

    def __init__(self, list_values: list[float]):
        """The Constructor Method, returns a list of float values."""
        self.values = list_values
    
    def __str__(self) -> str:
        """Returns a readable string."""
        msg: str = (f"Simpy({self.values})")
        return msg
   
    def fill(self, num: float, amount: int) -> None:
        """Makes a list with float numbers."""
        # empty list - resets list to []
        self.values = list()
        # loop to append values
        for x in range(amount):
            self.values.append(num)

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Fill in the values attribute with a range of values."""
        assert step != 0.0  # makes sure 0.0 is not a step value
        # index values
        i: float = start  # for the while loop
        plus_num: float = start  # this is the value added to self.values
        # loop to append values to the self.values list
        while (i < (start - stop)) or (i < stop):
            # if step is positive, goes through this if-statement
            if (step - step) < (step + step):
                self.values.append(plus_num)
                plus_num += step
                i += step
            # if step is negative, goes through this if-statement
            if (step - step) > (step + step):
                self.values.append(plus_num)
                plus_num += step
                i -= step
        # if last index value is equal to stop, it is removed
        if self.values and self.values[-1] >= stop:
            self.values.pop()

    def sum(self) -> float:
        """Sums all values in self.values list."""
        return sum(self.values)  # uses sum() to add up self.values

    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Adds a number to each value in the Simpy list."""
        new_list: list[float] = list()  # empty list
        i: int = 0  # index increment
        if type(rhs) is float:  # if it is a float value, goes through this if-statement
            for i in self.values:
                new_list.append(rhs + i)  # appends the index and float value
        else:  # it is a list if it goes through the else-statement
            assert len(self.values) == len(rhs.values)  # makes sure both lists are equal in length
            for x in self.values:
                new_list.append(x + rhs.values[i])  # adds the lists together, by index value
                i += 1  # increments i by 1

        return Simpy(new_list)  # returns the new Simpy list

    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Exponentiation the value of a list."""
        new_list: list[float] = list()  # empty list
        i: int = 0  # increment index
        if type(rhs) is float:  # if it is a float, goes through this if-statement
            for i in self.values:
                new_list.append(i ** rhs)  # powers the value
        else:  # it is a list if it goes through the else-statement
            assert len(self.values) == len(rhs.values)  # makes sure lists are equal in length
            for x in self.values:
                new_list.append(x ** rhs.values[i])  # powers the same index values
                i += 1

        return Simpy(new_list)

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Finds if each index is equal to the same index of a list or a float value."""
        new_list: list[bool] = list()  # empty bool list
        i: int = 0  # increment index
        if type(rhs) is float:  # if it is a float value, goes through this if-statement
            for x in self.values:  # for loop for self.values
                if x == rhs:
                    new_list.append(True)  # if value is equal to same value, True is appended
                else:
                    new_list.append(False)  # false if not
        else:  # if it is a list, goes through this else-statement
            for x in self.values:
                if x == rhs.values[i]:  # if index is equal to other index in list, appends true, else it appends false
                    new_list.append(True)
                else:
                    new_list.append(False)
                i += 1
        return new_list  # returns the new list of true, false values
    
    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Finds if each index is equal or greater than to the same index of a different list or a float value."""
        new_list: list[bool] = list()  # empty bool list
        i: int = 0 
        if type(rhs) is float:  # if it is a float value, goes through this if-statement
            for x in self.values:
                if x > rhs:  # if value in self.values is greater than rhs; True appended
                    new_list.append(True)
                else:  # False if not
                    new_list.append(False)
        else:  # if rhs is a Simpy list
            for x in self.values:  # for loop for self.values
                if x > rhs.values[i]:  # if x in list is greater than rhs list value, True appended
                    new_list.append(True)
                else:
                    new_list.append(False)
                i += 1  # increments by 1 for rhs list
        return new_list
    
    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Adds subscription notation support to objects of the class."""
        new_list: list[float] = list()  # empty list
        i: int = 0
        if type(rhs) is int:  # if rhs is a int, goes through this if-statement 
            return self.values[rhs]  # returns the self.value index by rhs value
        else:  # if it is a list[bool]
            for x in self.values:
                if rhs[i] is True:  # if rhs list value is True, appends the x value in self.values
                    new_list.append(x)
                i += 1  # increment for rhs list index
        return Simpy(new_list)  # returns a Simpy Class list
