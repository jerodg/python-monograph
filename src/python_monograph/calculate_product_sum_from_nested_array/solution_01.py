#!/usr/bin/env python3
"""Python Monograph: Calculate Product Sum of a Nested Array Solution 01

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


def solution_01(arr: list[int | list]) -> int:
    """
    Calculates the product sum of a nested array using an iterative method with a stack.

    The product sum of an array is defined as the sum of its elements multiplied by
    their respective depths.  If an element is a list, its product sum is calculated
    iteratively by multiplying the sum of its elements with its depth plus one.

    Args:
        arr (list[int | list]): The array of integers and nested lists.

    Returns:
        int: The product sum of the array.

    Examples:
        >>> solution_01([1, 2, 3])
        6
        >>> solution_01([-1, 2, [-3, 4]])
        8
        >>> solution_01([1, 2, 3, [4, 5]])
        23
        >>> solution_01([1, -1])
        0
        >>> solution_01([1, -2])
        -1
        >>> solution_01([-3.5, [1, [0.5]]])
        1.5
    """
    # Initialize a stack and push the input array and its depth (which is 1) into the stack.
    stack = [(arr, 1)]
    # Initialize a variable `total_sum` to 0. This variable will hold the final product sum.
    total_sum = 0

    # While the stack is not empty, pop an element from the stack.
    # This element is a tuple containing an array and its depth.
    while stack:
        current_arr, depth = stack.pop()
        # Iterate over the array. For each element in the array, check if it is a list or an integer.
        for ele in current_arr:
            # If the element is a list, push it into the stack along with its depth (which is the current depth + 1).
            if isinstance(ele, list):
                stack.append((ele, depth + 1))
            # If the element is an integer, add it to `total_sum` multiplied by the depth.
            else:
                total_sum += ele * depth

    # Return `total_sum`.
    return total_sum


if __name__ == '__main__':
    print(__doc__)
