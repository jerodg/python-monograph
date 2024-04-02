#!/usr/bin/env python3
"""Python Monograph: Merge Sorted Arrays Solution 01

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


def solution_01(nums1: list[int], m: int, nums2: list[int], n: int) -> list[int]:
    """
    Merges two sorted arrays in-place where the first array has enough space to hold the additional elements from the second array.

    This function uses the Two Pointers / Iteration Method (Start from the end). It involves using two pointers,
    each pointing to the end of each array. Compare the elements pointed by the pointers and put the larger one into
    the last unprocessed position in the result array, then move the pointer of the larger element one step backward.
    Repeat this process until all elements in both arrays have been processed.

    Args:
        nums1 (list[int]): The first sorted array, which has enough space to hold the additional elements from nums2.
        m (int): The number of initialized elements in nums1.
        nums2 (list[int]): The second sorted array.
        n (int): The number of initialized elements in nums2.

    Returns:
        None. The result is stored in nums1.

    Doctest:
        >>> nums1 = [4, 5, 6, 0, 0, 0]
        >>> m = 3
        >>> nums2 = [1, 2, 3]
        >>> n = 3
        >>> solution_01(nums1, m, nums2, n)
        >>> print(nums1)
        [1, 2, 3, 4, 5, 6]
    """
    # Initialize two pointers, each pointing to the end of each array
    p1 = m - 1
    p2 = n - 1
    # Initialize a pointer for the last unprocessed position in nums1
    p = m + n - 1

    # Process each element in both arrays
    while p1 >= 0 and p2 >= 0:
        # Compare the elements pointed by the pointers and put the larger one into the last unprocessed position in nums1
        if nums1[p1] <= nums2[p2]:
            nums1[p] = nums2[p2]
            p2 -= 1
        else:
            nums1[p] = nums1[p1]
            p1 -= 1
        p -= 1

    # If there are remaining elements in nums2, append them into the unprocessed positions in nums1
    if p2 >= 0:
        nums1[: p2 + 1] = nums2[: p2 + 1]

    return nums1[: m + n]


if __name__ == '__main__':
    print(__doc__)
