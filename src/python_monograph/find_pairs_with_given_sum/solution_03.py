#!/usr/bin/env python3
"""Python Monograph: Find Pairs With the Given Sum Solution 03

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


def binary_search(arr: List[int], low: int, high: int, x: int) -> int:
    """
    This function performs a binary search on a sorted list and returns the index of the element if found, else -1 using recursion.

    Args:
        arr (List[int]): A sorted list of integers.
        low (int): The lower index of the list to search.
        high (int): The higher index of the list to search.
        x (int): The element to search for.

    Returns:
        int: The index of the element if found, else -1.

    Doctests:
    >>> binary_search([1, 2, 3, 4, 5], 0, 4, 3)
    2
    >>> binary_search([1, 2, 3, 4, 5], 0, 4, 6)
    -1
    """
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        return -1


def solution_03(arr: List[int], req_sum: int) -> Tuple[int, List[Tuple[int, int]]]:
    """
    This function returns the number of pairs in the input list `arr` that sum up to `req_sum` and a list of the pairs.

    Args:
        arr (List[int]): A list of integers.
        req_sum (int): The required sum.

    Returns:
        Tuple[int, List[Tuple[int, int]]]: The number of pairs in `arr` that sum up to `req_sum`, and a list of the pairs.

    Doctests:
    >>> solution_03([1, 5, 7, 1], 6)
    (2, [(1, 5), (5, 1)])
    >>> solution_03([1, 1, 1, 1, 1, 1, 1, 1], 2)
    (28, [(1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1),
    (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1)])
    >>> solution_03([1, 7, 6, 2, 5, 4, 3, 1, 9, 8], 7)
    (4, [(1, 6), (6, 1), (2, 5), (5, 2)])
    """
    arr.sort()  # Sort the array
    count = 0  # Initialize count to 0
    pairs = []  # Initialize pairs to an empty list
    for i in range(len(arr)):  # For each element in the array
        # Perform a binary search for the required sum minus the current element
        j = binary_search(arr, i + 1, len(arr) - 1, req_sum - arr[i])
        if j != -1:  # If the element is found
            count += 1  # Increment the count
            pairs.append((arr[i], arr[j]))  # Add the pair to the list
    return count, pairs  # Return the count and the list of pairs


if __name__ == '__main__':
    print(__doc__)
