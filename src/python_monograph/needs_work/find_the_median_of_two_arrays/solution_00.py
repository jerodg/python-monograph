#!/usr/bin/env python3
"""Python Monograph: Find the Median of Two Arrays Solution 00

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


def solution_00(nums: List[int], nums1: List[int]) -> float:
    """This function finds the median of two sorted arrays using the brute force approach.

    Args:
        nums (list): The first sorted array.
        nums1 (list): The second sorted array.

    Returns:
        float: The median of the two sorted arrays.

    Approach:
        The function merges the two sorted arrays into a new list and sorts it.
        Then it checks if the length of the merged list is odd or even.
        If it's odd, it returns the middle element.
        If it's even, it returns the average of the two middle elements.

    Example:
        >>> solution_00([1, 3, 5], [2, 4, 6])
        3.5
        >>> solution_00([1, 2], [3, 4])
        2.5
    """
    if not nums and not nums1:
        raise ValueError('Both input arrays are empty.')

    # Merge and sort the two arrays
    merged = sorted(nums + nums1)

    # Calculate the length of the merged array
    n = len(merged)

    # If the length is odd, return the middle element
    if n % 2 == 1:
        return merged[n // 2]
    # If the length is even, return the average of the two middle elements
    else:
        return (merged[n // 2 - 1] + merged[n // 2]) / 2


if __name__ == '__main__':
    print(__doc__)
