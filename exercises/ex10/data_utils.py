"""Dictionary related utility functions."""
from csv import DictReader

__author__ = "730717463"


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read csv file and return as a list of dicts with the headers as the keys."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    # do stuff here
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], header: str) -> list[str]:
    """Return a list of all values under a specific header."""
    result: list[str] = []
    # loop thru each element of the list
    for elem in table:

        # for each dictionar, get the value at key "header" nd add that to the result list
        result.append(elem[header])
    return result


def columnar(table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Reformat data so it's a dictionary with column headers as keys."""
    result: dict[str, list[str]] = {}
    # loop through keys of one row of the table to get the headers
    first_row: dict[str, str] = table[0]
    for key in first_row:
        # for each key (header), make a dictionary entry with all the columns
        result[key] = column_values(table, key)
    return result


def head(data: dict[str, list[str]], num_rows: int) -> dict[str, list[str]]:
    """Returns a certain number of rows from the data set."""
    result: dict[str, list[str]] = {}
    # loop through for the columns
    for x in data:
        try:
            holder: list[str] = []  # holds the values
            i: int = 0
        except:
            return data
        while i < num_rows:  # while loop to append the number of data rows
            holder.append(data[x][i])
            i += 1
            
        result[x] = holder
    return result


def select(data: dict[str, list[str]], columns: list[str]) -> dict[str, list[str]]:
    """Able to select the columns to look at."""
    result: dict[str, list[str]] = {}
    # for loop to go through columns 
    for i in columns:
        result[i] = data[i]  # adds on the columns
    return result


def concat(data_one: dict[str, list[str]], data_two: dict[str, list[str]]) -> dict[str, list[str]]:
    """Combine two tables into one single table."""
    result: dict[str, list[str]] = {}
    # for loop to go through data_one 
    for i in data_one:
        result[i] = data_one[i]  # assigns data_one to result dict
    # for loop to go through data_two and see if key needs to be added
    for i in data_two:
        if i in result.keys():  # checks to see if data_two key is a result key
            result[i] += data_two[i]  # if yes, adds on the value to the key
        else:
            result[i] = data_two[i]  # else, adds a new key and value
    return result


def count(info: list[str]) -> dict[str, int]:
    """Count the number of times a value appeared in the input list."""
    result: dict[str, int] = {}

    # loop through each item
    for item in info:
        if item in result:
            result[item] += 1  # adds 1 if item is already there
        else:
            result[item] = 1  # declares a 1 if first time seeing item
    return result
