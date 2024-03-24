#!/usr/bin/env python3
"""Python Monograph: Find the Median of Two Arrays Solution 03

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


def solution_03(nums: list[int], nums1: list[int]) -> float:
    """
    This function finds the median of two sorted arrays by merging them and then finding the middle value(s) using the brute
    force approach (alternate).

    Args:
        nums (list[int]): The first sorted array.
        nums1 (list[int]): The second sorted array.

    Returns:
        float: The median of the two sorted arrays.

    Raises:
        ValueError: If both input arrays are empty.

    Approach:
        The function first checks if both input arrays are empty and raises a ValueError if they are.
        Then it merges the two sorted arrays into one and sorts it.
        If the total number of elements is odd, it returns the middle element.
        If the total number of elements is even, it calculates the average of the two middle elements as the median.

    Example:
        >>> solution_03([1, 3], [2])
        2.0
        >>> solution_03([1, 2], [3, 4])
        2.5
        >>> solution_03([0, 0], [0, 0])
        0.0
        >>> solution_03([], [])
        Traceback (most recent call last):
            ...
        ValueError: Both input arrays are empty.
        >>> solution_03([], [1])
        1.0
        >>> solution_03([-1000], [1000])
        0.0
        >>> solution_03([-1.1, -2.2], [-3.3, -4.4])
        -2.75
    """

    if not nums and not nums1:
        raise ValueError('Both input arrays are empty.')

    # Merge the arrays into a single sorted array.
    merged = sorted(nums + nums1)
    total = len(merged)

    if total % 2 == 1:  # If the total number of elements is odd
        return float(merged[total // 2])  # then return the middle element

    # If the total number of elements is even, calculate
    # the average of the two middle elements as the median.
    middle1 = merged[total // 2 - 1]
    middle2 = merged[total // 2]
    return (float(middle1) + float(middle2)) / 2.0


if __name__ == '__main__':
    print(__doc__)
