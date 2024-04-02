#!/usr/bin/env python3
"""Python Monograph: Find Pairs With the Given Sum Solution 04

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


def solution_04(arr: List[int], req_sum: int) -> Tuple[int, List[Tuple[int, int]]]:
    """
    This function returns the number of pairs in the input list `arr` that sum up to `req_sum` and a list of the pairs using a
    brute force approach.

    It uses a brute force approach, checking every possible pair of numbers in the array. If a pair sums up to the target sum,
    it increments the count and adds the pair to the list.

    Args:
        arr (List[int]): A list of integers.
        req_sum (int): The required sum.

    Returns:
        Tuple[int, List[Tuple[int, int]]]: The number of pairs in `arr` that sum up to `req_sum`, and a list of the pairs.

    Doctests:
    >>> solution_04([1, 5, 7, 1], 6)
    (2, [(1, 5), (5, 1)])
    >>> solution_04([1, 1, 1, 1, 1, 1, 1, 1], 2)
    (28, [(1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1),
    (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1)])
    >>> solution_04([1, 7, 6, 2, 5, 4, 3, 1, 9, 8], 7)
    (4, [(1, 6), (6, 1), (2, 5), (5, 2)])
    """
    count = 0  # Initialize count to 0
    pairs = []  # Initialize pairs to an empty list
    for i in range(len(arr)):  # For each element in the array
        for j in range(i + 1, len(arr)):  # For each element in the array after the current element
            if arr[i] + arr[j] == req_sum:  # If the pair sums up to the target sum
                count += 1  # Increment the count
                pairs.append((arr[i], arr[j]))  # Add the pair to the list
    return count, pairs  # Return the count and the list of pairs


if __name__ == '__main__':
    print(__doc__)
