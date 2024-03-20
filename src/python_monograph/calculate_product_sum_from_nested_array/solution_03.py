#!/usr/bin/env python3
"""Python Monograph: Calculate Product Sum of a Nested Array Solution 03

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


def iterate(arr: list[int | list], depth: int = 1):
    """
    Generator function that iterates over the array and its nested arrays in a depth-first manner.

    This function yields each integer in the array along with its depth.

    Args:
        arr (list[int | list]): The array of integers and nested lists.
        depth (int): The current depth level.

    Yields:
        tuple: A tuple containing an integer from the array and its depth.

    Examples:
        >>> list(iterate([1, 2, 3]))
        [(1, 1), (2, 1), (3, 1)]
        >>> list(iterate([-1, 2, [-3, 4]]))
        [(-1, 1), (2, 1), (-3, 2), (4, 2)]
    """
    for ele in arr:
        # If the element is a list, recursively iterate over it with an increased depth.
        if isinstance(ele, list):
            yield from iterate(ele, depth + 1)
        # If the element is an integer, yield it along with its depth.
        else:
            yield ele, depth


def solution_03(arr: list[int | list]) -> int:
    """
    Calculates the product sum of a nested array using a generator function.

    The product sum of an array is defined as the sum of its elements multiplied by
    their respective depths.  If an element is a list, its product sum is calculated
    iteratively by multiplying the sum of its elements with its depth plus one.

    Args:
        arr (list[int | list]): The array of integers and nested lists.

    Returns:
        int: The product sum of the array.

    Examples:
        >>> solution_03([1, 2, 3])
        6
        >>> solution_03([-1, 2, [-3, 4]])
        8
        >>> solution_03([1, 2, 3, [4, 5]])
        23
        >>> solution_03([1, -1])
        0
        >>> solution_03([1, -2])
        -1
        >>> solution_03([-3.5, [1, [0.5]]])
        1.5
    """
    # Initialize a variable `total_sum` to 0. This variable will hold the final product sum.
    total_sum = 0
    # Use the generator function to iterate over the array and its nested arrays.
    for value, depth in iterate(arr):
        # For each integer and its depth, add the integer multiplied by the depth to `total_sum`.
        total_sum += value * depth

    # Return `total_sum`.
    return total_sum


if __name__ == '__main__':
    print(__doc__)
