#!/usr/bin/env python3
"""Python Monograph: Merge Sorted Arrays Solution 03

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


def solution_03(nums1: list[int], m: int, nums2: list[int], n: int) -> list[int]:
    """
    Merges two sorted arrays into one sorted array using the built-in sort function in Python.

    This function creates a new list and appends the first m elements from nums1 and the first n elements from nums2.
    It then sorts this new list and replaces the first m+n elements in nums1 with the sorted elements.

    Args:
        nums1 (List[int]): The first sorted array, which has enough space to hold the additional elements from nums2.
        m (int): The number of initialized elements in nums1.
        nums2 (List[int]): The second sorted array.
        n (int): The number of initialized elements in nums2.

    Returns:
        None. The result is stored in nums1.

    Doctest:
        >>> nums1 = [1, 2, 3, 0, 0, 0]
        >>> m = 3
        >>> nums2 = [2, 5, 6]
        >>> n = 3
        >>> solution_03(None, nums1, m, nums2, n)
        >>> print(nums1)
        [1, 2, 2, 3, 5, 6]
    """
    # Create a new list
    nums3 = []
    # Append the first m elements from nums1
    for i in range(m):
        nums3.append(nums1[i])

    # Append the first n elements from nums2
    for i in range(n):
        nums3.append(nums2[i])

    # Sort the new list and replace the first m+n elements in nums1 with the sorted elements
    for i, num in enumerate(sorted(nums3)):
        nums1[i] = num

    # Remove trailing zeros if nums2 is empty
    if n == 0:
        nums1 = nums1[:m]

    return nums1


if __name__ == '__main__':
    print(__doc__)
