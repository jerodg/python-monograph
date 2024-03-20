#!/usr/bin/env python3
"""Python Monograph: Find the Median of Two Arrays Solution 01

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


def solution_01(nums: List[int], nums1: List[int]) -> float:
    """This function finds the median of two sorted arrays using the binary search method.

    Args:
        nums (list): The first sorted array.
        nums1 (list): The second sorted array.

    Returns:
        float: The median of the two sorted arrays.

    Approach:
        The function first ensures that `nums1` is the smaller array.
        Then it performs a binary search on `nums1` and calculates the median based on the elements at the partition points.

    Example:
        >>> solution_01([1, 3, 5], [2, 4, 6])
        3.5
        >>> solution_01([1, 2], [3, 4])
        2.5
    """
    if not nums and not nums1:
        raise ValueError('Both input arrays are empty.')

    if len(nums) > len(nums1):
        nums, nums1 = nums1, nums

    x, y = len(nums), len(nums1)

    start = 0
    end = x

    while start <= end:
        partitionX = (start + end) // 2
        partitionY = ((x + y + 1) // 2) - partitionX

        maxLeftX = float('-inf') if partitionX == 0 else nums[partitionX - 1]
        minRightX = float('inf') if partitionX == x else nums[partitionX]

        maxLeftY = float('-inf') if partitionY == 0 else nums1[partitionY - 1]
        minRightY = float('inf') if partitionY == y else nums1[partitionY]

        if maxLeftX <= minRightY and maxLeftY <= minRightX:
            if (x + y) % 2 == 0:
                return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2
            else:
                return max(maxLeftX, maxLeftY)

        elif maxLeftX > minRightY:
            end = partitionX - 1

        else:
            start = partitionX + 1


if __name__ == '__main__':
    print(__doc__)
