"""EX07 - Testing EX06 functions."""
import pytest
from exercises.ex06.dictionary import invert
from exercises.ex06.dictionary import favorite_color
from exercises.ex06.dictionary import count
from exercises.ex06.dictionary import alphabetizer
from exercises.ex06.dictionary import update_attendance

__author__ = "730717463"


# tests for invert function
def test_empty_dict_i() -> None:
    """Return empty dict for empty dict."""
    assert invert({}) == {}


def test_three_keys() -> None:
    """Returns swapped dictionary."""
    assert invert({"key": "sam", "car": "two", "door": "one"}) == {"sam": "key", "two": "car", "one": "door"}


def test_sentence() -> None:
    """Returns a swapped dictionary of length one."""
    with pytest.raises(KeyError):
        invert({'car': 'toyota', 'truck': 'toyota'})


# tests for favorite_color function
def test_empty_dict_fc() -> None:
    """Returns empty string."""
    assert favorite_color({}) == ""


def test_returns_fav() -> None:
    """Returns the favorite color."""
    assert favorite_color({"Austin": "Green", "Jacob": "Blue", "Sam": "Yellow", "Carl": "Blue", "Scott": "Blue", "John": "Yellow"}) == "Blue"


def test_fav_word() -> None:
    """Returns favorite word, even if it is not a color."""
    assert favorite_color({"Austin": "Green", "Jacob": "Car", "Sam": "Yellow", "Carl": "Car", "Scott": "Car", "John": "Yellow"}) == "Car"


# tests count function
def test_empty_list_c() -> None:
    """Tests the empty string."""
    assert count([]) == {}


def test_count_right() -> None:
    """Tests to see if it is correct."""
    assert count(["Awesome", "Awesome", "Cool", "Cool", "Cool", "Sad"]) == {"Awesome": 2, "Cool": 3, "Sad": 1}


def test_letter() -> None:
    """Tests to see if it can count a single letter."""
    assert count(["A", "A", "B", "B", "C", "B", "C", "A", "B", "A"]) == {"A": 4, "B": 4, "C": 2}


# tests alphabetizer function
def test_empty_list_a() -> None:
    """Tests to see if returns a empty dictionary."""
    assert alphabetizer([]) == {}


def test_alpha_uppercase() -> None:
    """Tests to see if function works with uppercase."""
    assert alphabetizer(["Car", "Carrot", "House", "Hose", "Cart", "Toy"]) == {"c": ["Car", "Carrot", "Cart"], "h": ["House", "Hose"], "t": ["Toy"]}


def test_alpha_lowercase() -> None:
    """Tests to see if lowercase works."""
    assert alphabetizer(["car", "carrot", "house", "hose", "cart", "toy"]) == {"c": ["car", "carrot", "cart"], "h": ["house", "hose"], "t": ["toy"]}


# tests update_attendance function
def test_empty_dict_attend() -> None:
    """Tests to see if empty dict returns just the day and student."""
    assert update_attendance({}, "Monday", "Austin") == {"Monday": ["Austin"]}


def test_attend() -> None:
    """Tests to see if attend works correctly with all parameters."""
    assert update_attendance({"Monday": ["Austin", "Sam", "Carl"], "Tuesday": ["Austin"], "Thursday": [], "Friday": ["Austin", "John"]}, "Friday", "Carl") == {"Monday": ["Austin", "Sam", "Carl"], "Tuesday": ["Austin"], "Thursday": [], "Friday": ["Austin", "John", "Carl"]}


def test_same_name_on_day() -> None:
    """Add a week with a student."""
    assert update_attendance({"Monday": ["Austin", "Sam"], "Tuesday": ["Austin"]}, "Tuesday", "Austin") == {'Monday': ['Austin', 'Sam'], 'Tuesday': ['Austin']}