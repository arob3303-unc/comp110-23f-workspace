"""Combining two lists into a dictionary!"""

__author__ = "730717463"


def zip(list1: list[str], list2: list[int]) -> dict[str, int]:
    """Produces a dictionary with two lists."""
    # empty dictionary
    comb_dict: dict[str, int] = {}
    
    # returns empty list if both lists are not same length
    if len(list1) != len(list2):
        return comb_dict

    # index start
    idx: int = 0

    # for loop to go thru list1
    for x in list1:
        y: int = list2[idx]  # adds list 2 value to y
        comb_dict[x] = y  # makes the dictionary
        idx += 1
    
    # Returns the completed dictionary
    return comb_dict
