#!/usr/bin/env python3
"""Python Monograph: Merge Sorted Arrays Solution 04

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


def solution_04(nums1: list[int], m: int, nums2: list[int], n: int) -> list[int]:
    """Merges two sorted arrays into one sorted array in-place.

    This function takes two sorted integer arrays nums1 and nums2, and merges them into a single sorted array in-place.
    The first m elements of nums1 and the first n elements of nums2 are considered for merging.
    The function uses a two-pointer technique, where each pointer points to the end of each array and moves backward as we
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
        >>> solution_04([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
        [1, 2, 2, 3, 5, 6]
    """
    # Initialize two pointers, each pointing to the end of each array
    p1, p2 = m - 1, n - 1

    # Process each element in both arrays
    for i in range(m + n - 1, -1, -1):
        # If the pointer of nums1 is still within the range and (the pointer of nums2 is out of range or the current element in
        # nums1 is greater or equal to the current element in nums2)
        if p1 >= 0 and (p2 < 0 or nums1[p1] >= nums2[p2]):
            # Put the current element in nums1 into the current position
            nums1[i] = nums1[p1]
            # Move the pointer of nums1 backward
            p1 -= 1
        else:
            # Otherwise, put the current element in nums2 into the current position
            if p2 >= 0:
                nums1[i] = nums2[p2]
                # Move the pointer of nums2 backward
                p2 -= 1

    return nums1[: m + n]


if __name__ == '__main__':
    print(__doc__)
