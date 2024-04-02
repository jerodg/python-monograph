"""
Python Monograph -> Check if Two Circles Intersect -> Solution 09

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
import random

from python_monograph.helpers.circle import Circle


def do_circles_intersect(circle1: Circle, circle2: Circle, num_samples: int = 10000) -> bool:
    """
    Determines if two circles intersect using a Monte Carlo approach.

    Args:
        circle1 (Circle): The first circle, represented as a tuple of (x, y, r).
        circle2 (Circle): The second circle, represented as a tuple of (x, y, r).
        num_samples (int, optional): The number of random points to sample. Defaults to 10000.

    Returns:
        bool: True if the circles intersect, False otherwise.

    Doctests:
        >>> do_circles_intersect(Circle(0, 0, 5), Circle(0, 0, 5))
        True
        >>> do_circles_intersect(Circle(0, 0, 5), Circle(4, 0, 3))
        True
        >>> do_circles_intersect(Circle(0, 0, 5), Circle(10, 0, 3))
        False
        >>> do_circles_intersect(Circle(0, 0, 5), Circle(4, 4, 5))
        True
        >>> do_circles_intersect(Circle(0, 0, 5), Circle(10, 10, 5))
        False
    """
    count = 0
    for _ in range(num_samples):
        # Generate a random point within the bounding box of the two circles
        x = random.uniform(min(circle1.x - circle1.r, circle2.x - circle2.r), max(circle1.x + circle1.r, circle2.x + circle2.r))
        y = random.uniform(min(circle1.y - circle1.r, circle2.y - circle2.r), max(circle1.y + circle1.r, circle2.y + circle2.r))

        # Check if the point is within both circles
        if math.sqrt((x - circle1.x) ** 2 + (y - circle1.y) ** 2) <= circle1.r and math.sqrt(
                (x - circle2.x) ** 2 + (y - circle2.y) ** 2) <= circle2.r:
            count += 1

    # Return True if the proportion of points within both circles is greater than 0
    return count / num_samples > 0
