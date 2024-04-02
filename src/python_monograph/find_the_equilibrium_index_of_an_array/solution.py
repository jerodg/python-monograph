#!/usr/bin/env python3
"""Python Monograph: Find the Equilibrium Index of an Array

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


def method_0(arr: list) -> int:
    """This function finds the equilibrium index of an array. The equilibrium index of an array is an index such that
    the sum of elements at lower indexes is equal to the sum of elements at higher indexes. The function uses a
    brute force approach to find the equilibrium index by iterating over the array and for each index, it calculates
    the sum of elements on the left and right. If the sums are equal, it returns the index. If no equilibrium index
    is found, it returns -1.

    Parameters:
        arr (list): The input array for which to find the equilibrium index.

    Returns:
        int: The equilibrium index if found, otherwise -1.
    """
    leftsum = 0
    rightsum = 0
    n = len(arr)

    # Iterate over the array
    for i in range(n):
        leftsum = 0
        rightsum = 0

        # Calculate the sum of elements on the left
        for j in range(i):
            leftsum += arr[j]

        # Calculate the sum of elements on the right
        for j in range(i + 1, n):
            rightsum += arr[j]

        # If the sums are equal, return the index
        if leftsum == rightsum:
            return i

    # If no equilibrium index is found, return -1
    return -1


def method_1(arr: list) -> int:
    """This function finds the equilibrium index of an array. The equilibrium index of an array is an index such that
    the sum of elements at lower indexes is equal to the sum of elements at higher indexes. The function uses an
    optimized approach to find the equilibrium index by iterating over the array and for each index, it calculates
    the sum of elements on the left and right in a single pass. If the sums are equal, it returns the index. If no
    equilibrium index is found, it returns -1.

    Parameters:
        arr (list): The input array for which to find the equilibrium index.

    Returns:
        int: The equilibrium index if found, otherwise -1.
    """
    total_sum = sum(arr)
    left_sum = 0

    for i, num in enumerate(arr):
        total_sum -= num

        if left_sum == total_sum:
            return i

        left_sum += num

    return -1


if __name__ == '__main__':
    print(__doc__)
