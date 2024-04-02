#!/usr/bin/env python3
"""Python Monograph: Find All Permutations of a List of Lists Solution 00

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


def solution_00(nums: list[int]) -> list[list[int]]:
    """
    This function generates all permutations of a given list of integers using a recursive approach.
    It iterates over the input list, removes each element, generates all permutations of the remaining list, and then appends the
    removed element to each of these permutations.

    Args:
        nums (list[int]): The input list of integers.

    Returns:
        list[list[int]]: A list of all permutations of the input list. Each permutation is represented as a list of integers.

    Examples:
        >>> solution_00([1, 2, 3])
        [[3, 2, 1], [2, 3, 1], [1, 3, 2], [3, 1, 2], [2, 1, 3], [1, 2, 3]]

    Note:
        The order of the permutations in the output list is not guaranteed to be in any specific order.
    """
    # Initialize an empty list to store the permutations.
    result: list[list[int]] = []

    # Base case: if the input list is empty, return a list containing an empty list.
    if len(nums) == 0:
        return [[]]

    # Iterate over the input list.
    for _ in range(len(nums)):
        # Remove the first element from the list.
        n = nums.pop(0)

        # Recursively generate all permutations of the remaining list.
        permutations = solution_00(nums.copy())

        # Append the removed element to each permutation.
        for perm in permutations:
            perm.append(n)

        # Add the new permutations to the result list.
        result.extend(permutations)

        # Add the removed element back to the end of the list.
        nums.append(n)

    # Return the list of permutations.
    return result


if __name__ == '__main__':
    print(__doc__)
