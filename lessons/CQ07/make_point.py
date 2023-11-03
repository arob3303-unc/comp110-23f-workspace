"""Test out point class."""
from lessons.CQ07.point import Point

my_point: Point = Point(1, 3)

new_point = my_point.scale(3)

print(my_point)

print(new_point)