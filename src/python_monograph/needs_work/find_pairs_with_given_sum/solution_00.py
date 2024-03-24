#!/usr/bin/env python3
"""Python Monograph: Find Pairs With the Given Sum Solution 00

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
from itertools import combinations


def solution_00(arr: List[int], req_sum: int) -> Tuple[int, List[Tuple[int, int]]]:
    """
    This function returns the number of pairs in the input list `arr` that sum up to `req_sum` using the `combinations`
    function from the `itertools` module, and a list of the pairs.

    Args:
        arr (List[int]): A list of integers.
        req_sum (int): The required sum.

    Returns:
        Tuple[int, List[Tuple[int, int]]]: The number of pairs in `arr` that sum up to `req_sum`, and a list of the pairs.

    Doctests:
    >>> solution_00([1, 5, 7, 1], 6)
    (2, [(1, 5), (5, 1)])
    >>> solution_00([1, 1, 1, 1, 1, 1, 1, 1], 2)
    (28, [(1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1),
    (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1)])
    >>> solution_00([1, 7, 6, 2, 5, 4, 3, 1, 9, 8], 7)
    (4, [(1, 6), (6, 1), (2, 5), (5, 2)])

    The function uses the `combinations` function from the `itertools` module to generate all possible pairs of numbers in `arr`.
    It then uses a list comprehension to create a list of pairs that sum up to `req_sum`. The length of this list and the list
    itself are returned.
    """
    # Generate all possible pairs of numbers in `arr` that sum up to `req_sum`
    pairs = [(a, b) for a, b in combinations(arr, 2) if a + b == req_sum]
    # Return the count of pairs and the pairs themselves
    return len(pairs), pairs


if __name__ == '__main__':
    print(__doc__)
