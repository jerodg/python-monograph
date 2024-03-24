#!/usr/bin/env python3
"""Python Monograph: Find Triplets with Zero Sum Solution 00

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


def solution_00(nums: list[int]) -> list[list[int]]:
    """This function takes a list of integers as input and returns a list of lists where each sublist contains three integers
    whose sum is zero. The function uses the combinations function from the itertools module to generate all possible
    combinations of three integers from the input list. It then filters out the combinations whose sum is not zero.
    The function finally returns the filtered combinations as a list of lists.

    Args:
        nums (list[int]): A list of integers.

    Returns:
        list[list[int]]: A list of lists where each sublist contains three integers whose sum is zero.

    Examples:
        >>> solution_00([-1, 0, 1, 2, -1, -4])
            [[-1, -1, 2], [-1, 0, 1]]
        >>> solution_00([])
            []
        >>> solution_00([0, 0, 0])
            [[0, 0, 0]]
        >>> solution_00([1, 2, 3, 0, -1, -2, -3])
            [[-3, 0, 3], [-3, 1, 2], [-2, -1, 3], [-2, 0, 2], [-1, 0, 1]]
    """
    return [list(x) for x in sorted({abc for abc in combinations(sorted(nums), 3) if not sum(abc)})]


if __name__ == '__main__':
    print(__doc__)
