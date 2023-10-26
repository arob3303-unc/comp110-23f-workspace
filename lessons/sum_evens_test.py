"""Testing my sum of evens function"""

from lessons.sum_evens import sum_evens_of_list

def test_empty_list() -> None:
    """Tests sum_evens_of_lists([]) should return 0."""
    assert sum_evens_of_list([]) == 0

def test_sum_one_element() -> None:
    """sum_evens_of_list([2]) = 2."""
    test_list: list[int] = [2]
    assert sum_evens_of_list(test_list) == 2

def test_sum_positives() -> None:
    """sum_evens_of_list of a list of positive."""
    