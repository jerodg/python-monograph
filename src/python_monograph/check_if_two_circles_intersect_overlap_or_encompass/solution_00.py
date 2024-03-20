#!/usr/bin/env python3
"""Python Monograph: Check if Two Circles Intersect, Overlap, or Encompass Solution 00

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
import math


class Circle(object):
    """A class to represent a circle.

    Attributes:
        x (int | float): The x-coordinate of the circle's center.
        y (int | float): The y-coordinate of the circle's center.
        r (int | float): The radius of the circle.

    Methods:
        check_relation(other_circle: Circle) -> str: Determines the relationship between this circle and another circle.
    """

    def __init__(self, x: [int | float], y: [int | float], r: [int | float]):
        """Initializes a Circle with a center at coordinates (x, y) and a radius r.

        Args:
            x (int | float): The x-coordinate of the circle's center.
            y (int | float): The y-coordinate of the circle's center.
            r (int | float): The radius of the circle.

        Raises:
            ValueError: If the radius is negative.
        """
        if r < 0:
            raise ValueError('Invalid input: radius must be positive')
        self.x = x
        self.y = y
        self.r = r

    def check_relation(self, other_circle) -> str:
        """Determines the relationship between this circle and another circle.

        The relationship can be one of the following:
        - The other circle is inside this circle.
        - This circle is inside the other circle.
        - The circles intersect.
        - The circles touch.
        - The circles do not overlap, intersect, or touch.

        Args:
            other_circle (Circle): The other circle to check the relationship with.

        Returns:
            str: A description of the relationship between the two circles.

        Example:
            >>> c1 = Circle(0, 0, 1)
            >>> c2 = Circle(2, 2, 1)
            >>> c1.check_relation(c2)
            'this circle and other_circle do not overlap, intersect, or touch'
        """
        # Calculate the Euclidean distance between the centers of the two circles
        d = math.sqrt((self.x - other_circle.x) ** 2 + (self.y - other_circle.y) ** 2)

        # Check the relationship based on the distance and the radii of the two circles
        if d <= self.r - other_circle.r:
            return 'other_circle is in this circle'
        elif d <= other_circle.r - self.r:
            return 'this circle is in other_circle'
        elif d < self.r + other_circle.r:
            return 'this circle and other_circle intersect'
        elif d == self.r + other_circle.r:
            return 'this circle and other_circle will touch'
        else:
            return 'this circle and other_circle do not overlap, intersect, or touch'


if __name__ == '__main__':
    print(__doc__)
