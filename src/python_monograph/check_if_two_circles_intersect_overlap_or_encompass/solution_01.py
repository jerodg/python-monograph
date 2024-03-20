#!/usr/bin/env python3
"""Python Monograph: Check if Two Circles Intersect, Overlap, or Encompass Solution 01
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


class Circle:
    """A class to represent a circle using complex numbers.

    Attributes:
        center (complex): The center of the circle represented as a complex number.
        radius (float): The radius of the circle.

    Methods:
        relation(other: Circle) -> str: Determines the relationship between this circle and another circle.
    """

    def __init__(self, center: tuple, radius: float):
        """Initializes a Circle with a center at coordinates (x, y) and a radius r.

        Args:
            center (tuple): The center of the circle represented as a tuple of two numbers (x, y).
            radius (float): The radius of the circle.

        Raises:
            ValueError: If the radius is negative.
        """
        if radius < 0:
            raise ValueError('Invalid input: radius must be positive')

        self.center = complex(*center)
        self.radius = radius

    def relation(self, other: 'Circle') -> str:
        """Determines the relationship between this circle and another circle.

        The relationship can be one of the following:
        - The other circle is separate from this circle.
        - The other circle touches this circle.
        - The other circle is encompassed by this circle.
        - The other circle intersects this circle.

        Args:
            other (Circle): The other circle to check the relationship with.

        Returns:
            str: A description of the relationship between the two circles.

        Example:
            >>> c1 = Circle((0, 0), 1)
            >>> c2 = Circle((2, 0), 1)
            >>> c1.relation(c2)
            'Touch'
        """
        # Calculate the Euclidean distance between the centers of the two circles
        distance = abs(self.center - other.center)

        # Check the relationship based on the distance and the radii of the two circles
        if distance > self.radius + other.radius:
            return 'Separate'
        elif distance == self.radius + other.radius:
            return 'Touch'
        elif distance + min(self.radius, other.radius) < max(self.radius, other.radius):
            return 'Encompass'
        else:
            return 'Intersect'


if __name__ == '__main__':
    print(__doc__)
