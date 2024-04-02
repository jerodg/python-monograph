#!/usr/bin/env python3
"""Python Monograph: Find Pairs With the Given Sum Solution 01

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


def solution_01(arr: List[int], req_sum: int) -> Tuple[int, List[Tuple[int, int]]]:
    """
    This function returns the number of pairs in the input list `arr` that sum up to `req_sum` using a hash map, and a list of
    the pairs.

    The function uses a hash map to store the frequency of each number in the array. Then, for each number in the array,
    it subtracts the target sum from it and checks if the result is in the hash map. If it is, it adds the frequency of
    that number to the count.

    Args:
        arr (List[int]): A list of integers.
        req_sum (int): The required sum.

    Returns:
        Tuple[int, List[Tuple[int, int]]]: The number of pairs in `arr` that sum up to `req_sum`, and a list of the pairs.

    Doctests:
    >>> solution_01([1, 5, 7, 1], 6)
    (2, [(1, 5), (5, 1)])
    >>> solution_01([1, 1, 1, 1, 1, 1, 1, 1], 2)
    (28, [(1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1),
    (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1)])
    >>> solution_01([1, 7, 6, 2, 5, 4, 3, 1, 9, 8], 7)
    (4, [(1, 6), (6, 1), (2, 5), (5, 2)])
    """
    freq = {}  # Initialize an empty hash map
    pairs = []  # Initialize an empty list for pairs

    for num in arr:  # For each number in the array
        if req_sum - num in freq:  # If the target sum minus the current number is in the hash map
            pairs.extend([(num, req_sum - num)] * freq[req_sum - num])  # Add the pair to the list for each occurrence

        if num in freq:  # If the current number is in the hash map
            freq[num] += 1  # Increment its frequency

        else:  # If the current number is not in the hash map
            freq[num] = 1  # Set its frequency to 1

    return len(pairs), pairs  # Return the count and the list of pairs


if __name__ == '__main__':
    print(__doc__)
