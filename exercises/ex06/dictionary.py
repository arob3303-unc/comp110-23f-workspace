"""Functions with dictionaries"""

__author__ = "730717463"


def invert(original_dict: dict[str, str]) -> dict[str, str]:
    """keys, values for original dictionary swap and become a new dictionary."""
    # empty dictionary
    new_dict: dict[str, str] = {}

    # for loop to go through original dict
    for key1 in original_dict:
        new_dict[original_dict[key1]] = key1  # assigns value as the key
        
    # raises key error if length of dict is shortened due to same key value!
    if len(original_dict) != len(new_dict):
        raise KeyError("Not allowed to have same key value.")
       
    return new_dict


def favorite_color(color_dict: dict[str, str]) -> str:
    """Returns the color that appears the most."""
    fav_color: str = ""  # Holds the favorite color
    color_counter: int = 0

    for key in color_dict:
        if color_dict[key] in color_dict:

            



        #print(color_dict)
print(favorite_color({"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}))


def count(list_1: list[str]) -> dict[str, int]:
    """Counts the number of times the same value appears."""
    # empty dictionary
    new_dict: dict[str, int] = {}
    for i in list_1:
        if i in new_dict:
            new_dict[i] += 1
        else:
            new_dict[i] = 1
    return new_dict

#print(count(["a", "a", "a", "b", "c", "c"]))


def alphabetizer(list1: list[str]) -> dict[str, list[str]]:
    """The words will be assigned to their starting letter (key)."""

    for i in list1:
        while 