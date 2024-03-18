"""
Python Monograph -> Find the Equilibrium Index of an Array -> Solution 00

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
If not, see <https://www.mongodb.com/licensing/server-side-public-license>.
"""


def equilibrium_index(arr: list) -> int:
    """
    This function finds and returns the equilibrium index of an array. The equilibrium index of an array is an index
    such that the sum of elements at lower indexes is equal to the sum of elements at higher indexes. If no such index
    exists, the function returns -1.

    Args:
        arr (list): A list of integers representing the array.

    Returns:
        int: The equilibrium index of the array if it exists, otherwise -1.

    Raises:
        TypeError: If the input is not a list.
        ValueError: If the list contains non-integer elements.

    Doctest:
        >>> equilibrium_index([-7, 1, 5, 2, -4, 3, 0])
        3
        >>> equilibrium_index([1, 2, 3, 4, 5, 6])
        -1
        >>> equilibrium_index([1, 2, 3, 4, 3, 2, 1])
        3
        >>> equilibrium_index([20, 10, -80, 10, 10, 15, 35])
        0
        >>> equilibrium_index([0, -3, 5, -4, -2, 3, 1, 0])
        3
    """
    # Check if input is a list
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")

    # Check if list contains only integers
    if not all(isinstance(i, int) for i in arr):
        raise ValueError("List must contain only integers")

    # Iterate through the array
    for i in range(len(arr)):
        # Calculate the sum of elements on the left and right
        left_sum = sum(arr[:i])
        right_sum = sum(arr[i + 1:])

        # If the sums are equal, return the current index
        if left_sum == right_sum:
            return i

    # If no equilibrium index is found, return -1
    return -1
