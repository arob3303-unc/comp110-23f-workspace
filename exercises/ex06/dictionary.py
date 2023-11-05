"""Functions with dictionaries."""

__author__ = "730717463"


def invert(original_dict: dict[str, str]) -> dict[str, str]:
    """The keys, values for original dictionary swap and become a new dictionary."""
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
    # favorite color
    fav_color: str = ""
    # empty dictionary
    new_dict: dict[str, int] = {}
    # empty list
    new_list: list[str] = []

    # creates a list of the colors
    for key in color_dict:
        new_list.append(color_dict[key])

    # for loop to go through the list and assign it to the dict along with num count
    for i in new_list:
        # goes through list and assigns +1 as value for key if key is already in dict
        if i in new_dict:
            new_dict[i] += 1
        # if key is not in dict, it assigns the number 1 to the value
        else:
            new_dict[i] = 1
    
    # holds max num to find favorite color
    max_num: int = 0

    # for loop to find favorite color
    for key in new_dict:
        # if the max_num is less than the current value, it assigns it as the favorite color
        if new_dict[key] > max_num:
            fav_color = key
            max_num = new_dict[key]
    return fav_color


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


def alphabetizer(list1: list[str]) -> dict[str, list[str]]:
    """The words will be assigned to their starting key letter."""
    # empty dictionary
    new_dict: dict[str, list[str]] = {}

    # goes through list to create keys for new dictionary
    for i in list1:
        new_dict[i[0].lower()] = []
    
    # for loop to go through keys and assign list values
    for key in new_dict:
        for i in list1:
            if key == i[0].lower():  # if key equals the starting letter, assigns the value to key
                new_dict[key].append(i)  # appends it since it is a list
    return new_dict


def update_attendance(attendance_log: dict[str, list[str]], day: str, student: str) -> dict[str, list[str]]:
    """Updates the attendance log (dictionary)."""
    # updated attendance log
    updated_log: dict[str, list[str]] = attendance_log
    i: int = 0

    # makes sure same name is entered twice on a day
    for key in updated_log:
        name_list: list[str] = list()
        for x in updated_log[key]:
            name_list.append(x)
            i += 1
        print(name_list)
        if student in name_list and key == day:
            return updated_log
    
    # empty string to hold the days (keys)
    day_list: list[str] = []
    # for loop to make list of days (keys)
    for key in attendance_log:
        day_list.append(key)
    # if the day is not in the dictionary, adds the day and student and returns updated dictionary
    if day not in day_list:
        updated_log[day] = [student]  # assigns day and student as a new key, value
        return updated_log  # returns it to prevent KeyError later on in function
    # for loop to go through dictionary (only if it is a day that is already in dictionary)
    for key in updated_log:
        if key == day:  # if the day equals the day being recorded, student is added to the day
            updated_log[day].append(student)
    return updated_log  # returns the updated dictionary (log)
