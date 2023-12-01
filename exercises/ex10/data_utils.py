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
        holder: list[str] = []
        i: int = 0
        while i < num_rows:
            holder.append(data[x][i])
            i += 1
        result[x] = holder
    return result

def select(data: dict[str, list[str]], columns: list[str]) -> dict[str, list[str]]:
    """Able to select the columns to look at."""
    result: dict[str, list[str]] = {}

    for i in columns:
        result[i] = data[i]
    return result

def concat(data_one: dict[str, list[str]], data_two: dict[str, list[str]]) -> dict[str, list[str]]:
    """Combine two tables into one single table."""
    result: dict[str, list[str]] = {}
    vals: str = result.keys()
    x: int = 0
    for i in data_one:
        result[i] = data_one[i]
    print(1)
    print(result)
    print(2)
    for i in data_two:
        if i == list(vals)[x]:
            result[i] = (data_one[i])
            print(result)
            #print(result[i])
            x += 1
        else:
            break
    print(3)
    return result

