#!/usr/bin/env python3
"""Python Monograph: Find the Median of Two Arrays Solution 02

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


def solution_02(nums: List[int], nums1: List[int]) -> float:
    """This function finds the median of two sorted arrays using the two pointers method.

    Args:
        nums (List[int]): The first sorted array.
        nums1 (List[int]): The second sorted array.

    Returns:
        float: The median of the two sorted arrays.

    Approach:
        The function uses two pointers to merge the two sorted arrays into one.
        Then it calculates the median based on the length of the merged array.

    Example:
        >>> solution_02([1, 3, 5], [2, 4, 6])
        3.5
        >>> solution_02([1, 2], [3, 4])
        2.5
    """
    merged = []
    i = j = 0

    while i < len(nums) and j < len(nums1):
        if nums[i] < nums1[j]:
            merged.append(nums[i])
            i += 1
        else:
            merged.append(nums1[j])
            j += 1

    while i < len(nums):
        merged.append(nums[i])
        i += 1

    while j < len(nums1):
        merged.append(nums1[j])
        j += 1

    if len(merged) % 2 == 0:
        return (merged[len(merged) // 2] + merged[len(merged) // 2 - 1]) / 2
    else:
        return merged[len(merged) // 2]


if __name__ == '__main__':
    print(__doc__)
