"""
Python Monograph -> Check if Two Circles Intersect -> Solution 06

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
import matplotlib.pyplot as plt
from matplotlib.patches import Circle as pltCircle

from python_monograph.helpers.circle import Circle


# fixme: This isn't passing doctests. #14

def do_circles_intersect(circle1: Circle, circle2: Circle) -> bool:
    """
    Determines if two circles intersect using a graphical approach and matplotlib.

    This function creates a plot with two circles based on the input parameters.
    It then checks if any point on the perimeter of the first circle lies within the second circle.
    If such a point is found, the function returns True, indicating that the circles intersect.
    The function also displays the plot of the circles.

    Args:
        circle1 (Circle): The first circle, represented by a Circle object.
        circle2 (Circle): The second circle, represented by a Circle object.

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
    # Create a subplot
    fig, ax = plt.subplots()
    # Set the limits of the x and y axes
    ax.set_xlim(-25, 25)
    ax.set_ylim(-25, 25)
    # Add the first circle to the plot
    ax.add_patch(pltCircle((circle1.x, circle1.y), circle1.r))
    # Add the second circle to the plot
    ax.add_patch(pltCircle((circle2.x, circle2.y), circle2.r))

    # Iterate over the vertices of the path of the first circle
    for path in ax.patches[0].get_path().vertices:
        # If the second circle contains a point on the path of the first circle, set a flag to True
        if ax.patches[1].contains_point(path):
            intersect = False
            break
        else:
            intersect = True
            break

    # Display the figure
    plt.show()

    # Return the result
    return intersect
