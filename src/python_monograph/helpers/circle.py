"""
Python Monograph -> Helpers -> Circle

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


class Circle:
    """
    A class to represent a circle.
    """

    def __init__(self, x: int, y: int, r: int):
        """
        Initialize a Circle object.

        Args:
            x (int): The x-coordinate of the circle's center.
            y (int): The y-coordinate of the circle's center.
            r (int): The radius of the circle.

        Doctests:
            >>> c = Circle(0, 0, 5)
            >>> c.x
            0
            >>> c.y
            0
            >>> c.r
            5
            >>> c = Circle(-3, 4, 2)
            >>> c.x
            -3
            >>> c.y
            4
            >>> c.r
            2
            >>> c = Circle(1, 1, 1)
            >>> c.x
            1
            >>> c.y
            1
            >>> c.r
            1
            >>> c = Circle(1000, 1000, 1000)
            >>> c.x
            1000
            >>> c.y
            1000
            >>> c.r
            1000
            >>> c = Circle(-1000, -1000, 1000)
            >>> c.x
            -1000
            >>> c.y
            -1000
            >>> c.r
            1000
        """
        self.x = x  # x-coordinate of the circle's center
        self.y = y  # y-coordinate of the circle's center
        self.r = r  # radius of the circle


class CircleNP(Circle):
    """
    A class to represent a circle using numpy.
    """

    def __init__(self, x: int, y: int, r: int):
        """
        Initialize a CircleNP object.

        Args:
            x (int): The x-coordinate of the circle's center.
            y (int): The y-coordinate of the circle's center.
            r (int): The radius of the circle.

        Doctests:
            >>> c = CircleNP(0, 0, 5)
            >>> c.x
            0
            >>> c.y
            0
            >>> c.r
            5
            >>> c = CircleNP(-3, 4, 2)
            >>> c.x
            -3
            >>> c.y
            4
            >>> c.r
            2
            >>> c = CircleNP(1, 1, 1)
            >>> c.x
            1
            >>> c.y
            1
            >>> c.r
            1
            >>> c = CircleNP(1000, 1000, 1000)
            >>> c.x
            1000
            >>> c.y
            1000
            >>> c.r
            1000
            >>> c = CircleNP(-1000, -1000, 1000)
            >>> c.x
            -1000
            >>> c.y
            -1000
            >>> c.r
            1000
        """
        super().__init__(x, y, r)
        self.center = np.array([x, y])


class CircleBB(Circle):
    """
    A class to represent a circle with a bounding box.

    This class inherits from the Circle class and adds a bounding box attribute.
    The bounding box is a tuple that represents the smallest rectangle that can enclose the circle.

    Attributes:
        bounding_box (tuple): The bounding box of the circle. It is a tuple of four integers representing the coordinates of the
        top-left and bottom-right corners of the rectangle.

    Doctests:
        >>> c = CircleBB(0, 0, 5)
        >>> c.x
        0
        >>> c.y
        0
        >>> c.r
        5
        >>> c.bounding_box
        (-5, -5, 5, 5)
        >>> c = CircleBB(-3, 4, 2)
        >>> c.x
        -3
        >>> c.y
        4
        >>> c.r
        2
        >>> c.bounding_box
        (-5, 2, -1, 6)
        >>> c = CircleBB(1, 1, 1)
        >>> c.x
        1
        >>> c.y
        1
        >>> c.r
        1
        >>> c.bounding_box
        (0, 0, 2, 2)
        >>> c = CircleBB(1000, 1000, 1000)
        >>> c.x
        1000
        >>> c.y
        1000
        >>> c.r
        1000
        >>> c.bounding_box
        (0, 0, 2000, 2000)
        >>> c = CircleBB(-1000, -1000, 1000)
        >>> c.x
        -1000
        >>> c.y
        -1000
        >>> c.r
        1000
        >>> c.bounding_box
        (-2000, -2000, 0, 0)
    """

    def __init__(self, x: int, y: int, r: int):
        """
        Initialize a CircleBB object.

        Args:
            x (int): The x-coordinate of the circle's center.
            y (int): The y-coordinate of the circle's center.
            r (int): The radius of the circle.
        """
        super().__init__(x, y, r)
        # Calculate the bounding box of the circle
        self.bounding_box = (self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r)
