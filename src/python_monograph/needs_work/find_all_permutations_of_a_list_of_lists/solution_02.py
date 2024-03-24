#!/usr/bin/env python3
"""Python Monograph: Find All Permutations of a List of Lists Solution 02

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
from itertools import permutations


def solution_02(nums: list[int]) -> list[list[int]]:
    """
    This function generates all permutations of a given list of integers using Python's built-in itertools.permutations function.

    Args:
        nums (list[int]): The input list of integers.

    Returns:
        list[list[int]]: A list of all permutations of the input list. Each permutation is represented as a list of integers.

    Examples:
        >>> solution_02([1, 2, 3])
        [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
    """
    return [list(permutation) for permutation in permutations(nums)]


if __name__ == '__main__':
    print(__doc__)
