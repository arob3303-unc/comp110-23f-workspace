"""Using Lists in Functions."""

__author__ = "730717463"

#  all function
def all(list_nums: list[int], num: int) -> bool:
    """Returns True if the list contains the same value throughout (user's value)."""
    if len(list_nums) == 0:
        return False

    i: int = 0  # index counter
    
    while i < len(list_nums) - 1:
        print(list_nums[i])
        if list_nums[i] != num:  # if index num does not equal user's num, False returned
            return False
        i += 1   # increment to index
    return True   # returns True if while loop comes back False

#  max function
def max(list_nums: list[int]) -> int:
    """Pulls out the largest integer value in the list."""
    if len(list_nums) == 0:  # Raises a ValueError if a empty list is entered
        raise ValueError("max() arg is an empty List")
    
    # Variables
    i: int = 0
    
    while i <= len(list_nums) - 1:  # Goes through the list
        i_max: int = list_nums[0]
        if i_max <= list_nums[i]:  # If the current number is less than the index number it is on
            i_max = 0  # Resets the current number value
            i_max += list_nums[i]  # Adds the index number as the current number
        i += 1  # Increments the index
    
    return i_max  # Returns max number

#  is_equal function
def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Determines if two lists are equal."""
    i: int = 0  # index counter

    if len(list1) == 0 and len(list2) == 0:
        return True
    if len(list1) == 0:
        return False
    if len(list2) == 0:
        return False
    if len(list1) != len(list2):
        return False
    
    while i <= len(list1) - 1:
        if list1[i] != list2[i]:  # if the index(s) do not match, False returned
            return False
        i += 1  # increments index
    return True  # returns True if while loop comes back False