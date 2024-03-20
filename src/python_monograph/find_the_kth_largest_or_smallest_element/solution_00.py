#!/usr/bin/env python3
"""Python Monograph: Find the kth Largest or Smallest Element Solution 00

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


def solution_00(nums: list, k: int, largest: bool = True) -> int:
    """This function finds the kth largest or smallest element in a given list of numbers using the sort method.

    Parameters:
        nums (list): A list of integers.
        k (int): The position of the element to find. If 'largest' is True, this is the kth largest element. If 'largest' is
        False, this is the kth smallest element.
        largest (bool, optional): A boolean indicating whether to find the kth largest or smallest element. Defaults to True.

    Returns:
        int: The kth largest or smallest element in 'nums'.

    >>> solution_00([3, 2, 1, 5, 6, 4], 2)
    5
    >>> solution_00([3, 2, 1, 5, 6, 4], 2, largest=False)
    2
    >>> solution_00([3, 2, 3, 1, 2, 4, 5, 5, 6], 4)
    4
    """
    if k <= 0:
        raise IndexError('k cannot be zero or negative.')
    # If 'largest' is True, sort the list in descending order.
    if largest:
        nums.sort(reverse=True)
    # If 'largest' is False, sort the list in ascending order.
    else:
        nums.sort()

    # Return the kth element in the sorted list.
    return nums[k - 1]


if __name__ == '__main__':
    print(__doc__)
