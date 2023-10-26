"""Summing the elements of a list using different loops."""

__author__ = "730717463"


def w_sum(vals: list[float]) -> float:
    """Use a while loop to sum up the elements in a list."""
    # Variables
    i: int = 0  # index counter
    sum: float = 0.0  # sum holder

    while i < len(vals):
        sum += vals[i]
        i += 1
    return sum  # returns total value of all elements


def f_sum(vals: list[float]) -> float:
    """Use a for loop to sum up the elements in a list (no range)."""
    sum: float = 0.0  # sum holder

    for elem in vals:
        sum += elem
    return sum  # returns total value of all elements


def f_range_sum(vals: list[float]) -> float:
    """Use a for loop to sum up the elements in a list (range)."""
    sum: float = 0.0  # sum holder

    for i in range(0, len(vals)):
        sum += vals[i]
    return sum  # returns total value of all elements

places: dict[str, int] = {"Florida": 24, "Florida": 30}
#print(places["Hello"])