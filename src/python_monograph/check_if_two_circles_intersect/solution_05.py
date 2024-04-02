"""
Python Monograph -> Check if Two Circles Intersect -> Solution 05

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
import numpy as np

from python_monograph.helpers.circle import CircleNP


def do_circles_intersect(circle1: CircleNP, circle2: CircleNP) -> bool:
    """
    Determine if two CircleNPs intersect using a matrix approach with numpy.

    Args:
        circle1 (CircleNP): The first circle.
        circle2 (CircleNP): The second circle.

    Returns:
        bool: True if the circles intersect, False otherwise.

    Doctests:
        >>> c1 = CircleNP(0, 0, 5)
        >>> c2 = CircleNP(0, 0, 5)
        >>> do_circles_intersect(c1, c2)
        True
        >>> c1 = CircleNP(0, 0, 5)
        >>> c2 = CircleNP(4, 0, 3)
        >>> do_circles_intersect(c1, c2)
        True
        >>> c1 = CircleNP(0, 0, 5)
        >>> c2 = CircleNP(10, 0, 3)
        >>> do_circles_intersect(c1, c2)
        False
        >>> c1 = CircleNP(0, 0, 5)
        >>> c2 = CircleNP(4, 4, 5)
        >>> do_circles_intersect(c1, c2)
        True
        >>> c1 = CircleNP(0, 0, 5)
        >>> c2 = CircleNP(10, 10, 5)
        >>> do_circles_intersect(c1, c2)
        False
    """
    # Convert the centers of the CircleNPs to numpy arrays
    center1 = np.array([circle1.x, circle1.y])
    center2 = np.array([circle2.x, circle2.y])
    # Calculate the norm (distance) between the two centers
    distance_matrix = np.linalg.norm(center1 - center2)
    # Return True if the distance is less than or equal to the sum of the radii, False otherwise
    return distance_matrix <= (circle1.r + circle2.r)
