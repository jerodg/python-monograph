"""
Python Monograph -> Check if Two Circles Intersect -> Solution 01

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


def do_circles_intersect(circle1: Circle, circle2: Circle) -> bool:
    """
    Determine if two circles intersect using a Squared Distance approach.

    Args:
        circle1 (Circle): The first circle.
        circle2 (Circle): The second circle.

    Returns:
        bool: True if the circles intersect, False otherwise.

    Doctests:
        >>> c1 = Circle(0, 0, 5)
        >>> c2 = Circle(0, 0, 5)
        >>> do_circles_intersect(c1, c2)
        True
        >>> c1 = Circle(0, 0, 5)
        >>> c2 = Circle(4, 0, 3)
        >>> do_circles_intersect(c1, c2)
        True
        >>> c1 = Circle(0, 0, 5)
        >>> c2 = Circle(10, 0, 3)
        >>> do_circles_intersect(c1, c2)
        False
        >>> c1 = Circle(0, 0, 5)
        >>> c2 = Circle(4, 4, 5)
        >>> do_circles_intersect(c1, c2)
        True
        >>> c1 = Circle(0, 0, 5)
        >>> c2 = Circle(10, 10, 5)
        >>> do_circles_intersect(c1, c2)
        False
    """
    # Calculate the squared distance between the centers of the two circles
    distance_squared = (circle2.x - circle1.x) ** 2 + (circle2.y - circle1.y) ** 2
    # Return True if the squared distance is less than or equal to the square of the sum of the radii, False otherwise
    return distance_squared <= (circle1.r + circle2.r) ** 2