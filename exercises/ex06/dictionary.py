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
        raise KeyError("KeyError!")
       
    return new_dict


def favorite_color(color_dict: dict[str, str]) -> str:
    """Returns the color that appears the most."""
    fav_color: str = ""  # Holds the favorite color
    color: list[str] = []
    
    for key in color_dict:
        color.append(color_dict[key])
        for i in color:
            if i == color_dict[key]:
                i

    print(color)
print(favorite_color({"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}))


