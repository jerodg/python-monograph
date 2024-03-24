#!/usr/bin/env python3
"""Python Monograph: Check if Two Circles Intersect, Overlap, or Encompass Solution 00 Tests

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
If not, see <https://www.mongodb.com/licensing/server-side-public-license>."""
import pytest

from templates.python import Circle


def test_circle_creation():
    c = Circle(0, 0, 1)
    assert c.x == 0
    assert c.y == 0
    assert c.r == 1


def test_circle_creation_with_negative_radius():
    with pytest.raises(ValueError):
        Circle(0, 0, -1)


def test_circles_with_same_center():
    c1 = Circle(0, 0, 1)
    c2 = Circle(0, 0, 2)
    assert c1.check_relation(c2) == 'this circle is in other_circle'


def test_circles_touching():
    c1 = Circle(0, 0, 1)
    c2 = Circle(2, 0, 1)
    assert c1.check_relation(c2) == 'this circle and other_circle will touch'


def test_circles_intersecting():
    c1 = Circle(0, 0, 2)
    c2 = Circle(1, 0, 2)
    assert c1.check_relation(c2) == 'this circle and other_circle intersect'


def test_circles_not_overlapping():
    c1 = Circle(0, 0, 1)
    c2 = Circle(3, 0, 1)
    assert c1.check_relation(c2) == 'this circle and other_circle do not overlap, intersect, or touch'


def test_one_circle_inside_other():
    c1 = Circle(0, 0, 2)
    c2 = Circle(0, 0, 1)
    assert c1.check_relation(c2) == 'other_circle is in this circle'


@pytest.mark.parametrize('x1,y1,r1,x2,y2,r2', [(0, 0, 1, 1000000, 1000000, 1), (0, 0, 1, -1000000, -1000000, 1)])
def test_circles_with_large_coordinates(x1, y1, r1, x2, y2, r2):
    c1 = Circle(x1, y1, r1)
    c2 = Circle(x2, y2, r2)
    assert c1.check_relation(c2) == 'this circle and other_circle do not overlap, intersect, or touch'


@pytest.mark.parametrize(
    'x1,y1,r1,x2,y2,r2',
    [(0, 0, 0.000001, 0.000002, 0.000002, 0.000002), (0, 0, 0.000002, 0.000001, 0.000001, 0.000001)]
)
def test_circles_with_small_coordinates(x1, y1, r1, x2, y2, r2):
    c1 = Circle(x1, y1, r1)
    c2 = Circle(x2, y2, r2)
    assert c1.check_relation(c2) == 'this circle and other_circle intersect'


if __name__ == '__main__':
    print(__doc__)
