"""
Python Monograph -> Check if Two Circles Intersect -> Solution 00 -> Tests

Copyright ©2024 Jerod Gawne <https://github.com/jerodg/>

This program is free software: you can redistribute it and/or modify
it under the terms of the Server Side Public License (SSPL) as
published by MongoDB, Inc., either version 1 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
SSPL for more details.

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
You should have received a copy of the SSPL along with this program.
If not, see <https://www.mongodb.com/licensing/server-side-public-license>.
"""
from python_monograph.helpers.circle import Circle
from python_monograph.check_if_two_circles_intersect.solution_00 import do_circles_intersect


def test_circles_with_same_center_intersect():
    c1 = Circle(0, 0, 5)
    c2 = Circle(0, 0, 5)
    assert do_circles_intersect(c1, c2) is True


def test_circles_with_overlapping_areas_intersect():
    c1 = Circle(0, 0, 5)
    c2 = Circle(4, 0, 3)
    assert do_circles_intersect(c1, c2) is True


def test_circles_with_no_overlap_do_not_intersect():
    c1 = Circle(0, 0, 5)
    c2 = Circle(10, 0, 3)
    assert do_circles_intersect(c1, c2) is False


def test_circles_touching_at_one_point_intersect():
    c1 = Circle(0, 0, 5)
    c2 = Circle(10, 0, 5)
    assert do_circles_intersect(c1, c2) is True


def test_circles_with_one_inside_the_other_intersect():
    c1 = Circle(0, 0, 5)
    c2 = Circle(0, 0, 3)
    assert do_circles_intersect(c1, c2) is True


def test_circles_with_negative_coordinates_intersect():
    c1 = Circle(-2, -2, 5)
    c2 = Circle(-3, -3, 3)
    assert do_circles_intersect(c1, c2) is True


def test_circles_with_large_coordinates_intersect():
    c1 = Circle(1000, 1000, 500)
    c2 = Circle(1000, 1000, 500)
    assert do_circles_intersect(c1, c2) is True


def test_circles_with_large_radius_intersect():
    c1 = Circle(0, 0, 1000)
    c2 = Circle(500, 500, 1000)
    assert do_circles_intersect(c1, c2) is True


def test_circles_with_small_radius_do_not_intersect():
    c1 = Circle(0, 0, 1)
    c2 = Circle(3, 3, 1)
    assert do_circles_intersect(c1, c2) is False
