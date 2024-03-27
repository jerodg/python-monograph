"""
Python Monograph -> Check if Two Circles Intersect -> Solution 08

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
import math

from python_monograph.helpers.circle import CircleBB


# fixme: The doctest is failing when one circle is completely inside the other. #16
def do_circles_intersect(circle1: CircleBB, circle2: CircleBB) -> bool:
    """
    Determines if two circles intersect.

    This function checks if two circles intersect by first checking if their bounding boxes intersect.
    If the bounding boxes do not intersect, the circles do not intersect.
    If the bounding boxes do intersect, the function calculates the distance between the centers of the circles.
    The circles intersect if the distance is less than or equal to the sum of their radii.

    Args:
        circle1 (CircleBB): The first circle.
        circle2 (CircleBB): The second circle.

    Returns:
        bool: True if the circles intersect, False otherwise.

    Doctests:
        >>> c1 = CircleBB(0, 0, 5)
        >>> c2 = CircleBB(0, 0, 5)
        >>> do_circles_intersect(c1, c2)
        True
        >>> c1 = CircleBB(0, 0, 5)
        >>> c2 = CircleBB(10, 0, 3)
        >>> do_circles_intersect(c1, c2)
        False
        >>> c1 = CircleBB(0, 0, 5)
        >>> c2 = CircleBB(4, 0, 3)
        >>> do_circles_intersect(c1, c2)
        True
        >>> c1 = CircleBB(0, 0, 5)
        >>> c2 = CircleBB(4, 4, 5)
        >>> do_circles_intersect(c1, c2)
        True
        >>> c1 = CircleBB(0, 0, 5)
        >>> c2 = CircleBB(10, 10, 5)
        >>> do_circles_intersect(c1, c2)
        False
    """
    # Get the bounding boxes of the circles
    x1, y1, x2, y2 = circle1.bounding_box
    x3, y3, x4, y4 = circle2.bounding_box

    # Check if the bounding boxes intersect
    if x2 < x3 or x1 > x4 or y2 < y3 or y1 > y4:
        return False

    # Calculate the distance between the centers of the circles
    dx, dy = circle2.x - circle1.x, circle2.y - circle1.y
    d = math.sqrt(dx ** 2 + dy ** 2)

    # Check if the circles intersect
    if d > circle1.r + circle2.r:
        return False
    elif d < abs(circle1.r - circle2.r):
        return False
    elif d == 0 and circle1.r == circle2.r:
        return False
    else:
        return True
