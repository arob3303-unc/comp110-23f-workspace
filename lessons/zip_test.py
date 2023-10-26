"""Test my Zip Function."""

__author__ = "730717463"

from lessons.zip import zip


def test_empty_list() -> None:
    """Edge case for empty list."""
    assert zip([], []) == {}


def test_different_length_list() -> None:
    """Use case for different length of lists."""
    assert zip(["House", "Car", "Bike"], [1, 2, 0, 1]) == {}


def test_length_of_three() -> None:
    """Use case for length of three for lists."""
    assert zip(["House", "Car", "Bike"], [1, 2, 5]) == {"House": 1, "Car": 2, "Bike": 5}
