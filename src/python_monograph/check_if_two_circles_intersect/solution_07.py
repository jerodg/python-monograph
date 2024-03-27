"""
Python Monograph -> Check if Two Circles Intersect -> Solution 07

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
# fixme: This solution is incorrect. It does not account for the case where one circle is completely inside the other. #15
import math

from python_monograph.helpers.circle import Circle


def do_circles_intersect(circle1: Circle, circle2: Circle) -> bool:
    """
    Determines if two circles intersect using an analytical geometry approach.

    This function calculates the Euclidean distance between the centers of the two circles.
    If the distance is less than or equal to the sum of the radii of the two circles, then the circles intersect.

    Args:
        circle1 (Circle): The first circle, represented as an instance of the Circle class.
        circle2 (Circle): The second circle, represented as an instance of the Circle class.

    Returns:
        bool: True if the circles intersect, False otherwise.

    Doctests:
        >>> circle1 = Circle(0, 0, 5)
        >>> circle2 = Circle(0, 0, 5)
        >>> do_circles_intersect(circle1, circle2)
        True
        >>> circle1 = Circle(0, 0, 5)
        >>> circle2 = Circle(4, 0, 3)
        >>> do_circles_intersect(circle1, circle2)
        True
        >>> circle1 = Circle(0, 0, 5)
        >>> circle2 = Circle(10, 0, 3)
        >>> do_circles_intersect(circle1, circle2)
        False
        >>> circle1 = Circle(0, 0, 5)
        >>> circle2 = Circle(4, 4, 5)
        >>> do_circles_intersect(circle1, circle2)
        True
        >>> circle1 = Circle(0, 0, 5)
        >>> circle2 = Circle(10, 10, 5)
        >>> do_circles_intersect(circle1, circle2)
        False
    """
    # Calculate the difference in x and y coordinates of the two circles
    dx, dy = circle2.x - circle1.x, circle2.y - circle1.y

    # Calculate the Euclidean distance between the centers of the two circles
    d = math.sqrt(dx ** 2 + dy ** 2)

    # Check if the distance is greater than the sum of the radii (circles are too far apart to intersect)
    if d > circle1.r + circle2.r:
        return False
    # Check if the distance is less than the absolute difference of the radii (one circle is completely inside the other)
    elif d < abs(circle1.r - circle2.r):
        return False
    # Check if the distance is zero and the radii are equal (the circles are identical)
    elif d == 0 and circle1.r == circle2.r:
        return False
    # If none of the above conditions are met, the circles intersect
    else:
        return True
