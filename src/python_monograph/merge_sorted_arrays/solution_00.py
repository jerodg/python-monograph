#!/usr/bin/env python3
"""Python Monograph: Merge Sorted Arrays Solution 00

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


def solution_00(nums1: list[int], m: int, nums2: list[int], n: int) -> list[int]:
    """Merges two sorted arrays into one sorted array.

    This function takes two sorted integer arrays nums1 and nums2, and merges them into a single sorted array.
    The first m elements of nums1 and the first n elements of nums2 are considered for merging.
    The function uses a two-pointer technique, where each pointer points to the start of each array and moves forward as we
    process each element.

    Args:
        nums1 (list[int]): The first sorted integer array. It has a size of m+n, where the first m elements are the elements to
        consider for merging, and the rest are zeros.
        m (int): The number of elements in nums1 to consider for merging.
        nums2 (list[int]): The second sorted integer array.
        n (int): The number of elements in nums2 to consider for merging.

    Returns:
        list[int]: The merged sorted array.

    Doctest:
        >>> solution_00([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
        [1, 2, 2, 3, 5, 6]
    """
    # Create a copy of the first m elements of nums1
    nums1_copy = nums1[:m]
    # Clear nums1
    nums1 = []

    # Initialize two pointers, each pointing to the start of each array
    p1 = 0
    p2 = 0

    # Process each element in both arrays
    while p1 < m and p2 < n:
        # Compare the elements pointed by the pointers and put the smaller one into nums1
        if nums1_copy[p1] <= nums2[p2]:
            nums1.append(nums1_copy[p1])
            p1 += 1
        else:
            nums1.append(nums2[p2])
            p2 += 1

    # If there are remaining elements in nums1_copy or nums2, append them into nums1
    if p1 < m:
        nums1[p1 + p2 :] = nums1_copy[p1:]

    if p2 < n:
        nums1[p1 + p2 :] = nums2[p2:]

    return nums1


if __name__ == '__main__':
    print(__doc__)
