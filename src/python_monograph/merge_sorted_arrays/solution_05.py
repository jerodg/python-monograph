#!/usr/bin/env python3
"""Python Monograph: Merge Sorted Arrays Solution 05

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


def solution_05(nums1: list[int], m: int, nums2: list[int], n: int) -> list[int]:
    """
    Merges two sorted integer arrays into one sorted array.

    This function takes two sorted integer arrays, nums1 and nums2, and merges them into a single sorted array.
    The function modifies nums1 in-place to include the elements of nums2 and then sorts the combined array.

    Args:
        nums1 (list[int]): The first sorted integer array. It has a size of m+n, where m is the number of initialized elements.
        m (int): The number of initialized elements in nums1.
        nums2 (list[int]): The second sorted integer array.
        n (int): The number of elements in nums2.

    Returns:
        list[int]: The merged and sorted array.

    Doctest:
        >>> solution_05([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
        [1, 2, 2, 3, 5, 6]
    """
    # Slice nums1 up to the mth index. This removes any placeholder zeros at the end of nums1.
    nums1[:] = nums1[:m]

    # Extend nums1 with the elements of nums2.
    nums1.extend(nums2)

    # Sort the combined array in-place.
    nums1.sort()

    return nums1


if __name__ == '__main__':
    print(__doc__)
