#!/usr/bin/env python3
"""Python Monograph: Find All Permutations of a List of Lists Solution 01

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


def backtrack(output: list[list[int]], nums: list[int], start: int) -> list[list[int]]:
    """
    This helper function generates all permutations of the list from the given start index.

    It uses a recursive approach to generate the permutations. It iterates over the list from the start index, swaps each element
    with the start element, and then recursively generates all permutations of the remaining list.

    Args:
        output (list[list[int]]): The list to store the permutations.
        nums (list[int]): The input list of integers.
        start (int): The start index for generating permutations.

    Returns:
        list[list[int]]: The list of all permutations of the input list. Each permutation is represented as a list of integers.

    Examples:
        >>> backtrack([], [1, 2, 3], 0)
        [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 2, 1], [3, 1, 2]]
    """
    # Base case: if the start index is the last index of the list, append a copy of the list to the output list.
    if start == len(nums) - 1:
        output.append(nums[:])
    else:
        # Iterate over the list from the start index.
        for i in range(start, len(nums)):
            # Swap the start element with the current element.
            nums[start], nums[i] = nums[i], nums[start]
            # Recursively generate all permutations of the remaining list.
            backtrack(output, nums, start + 1)
            # Swap the start element with the current element again to backtrack.
            nums[start], nums[i] = nums[i], nums[start]

    return output


def solution_01(nums: list[int]) -> list[list[int]]:
    """
    This function generates all permutations of a given list of integers using the backtrack helper function.

    The function uses a backtracking approach to generate the permutations. It iterates over the input list, swaps each element
    with the start element, and then recursively generates all permutations of the remaining list.

    Args:
        nums (list[int]): The input list of integers.

    Returns:
        list[list[int]]: A list of all permutations of the input list. Each permutation is represented as a list of integers.

    Examples:
        >>> solution_01([1, 2, 3])
        [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 2, 1], [3, 1, 2]]

    Note:
        The order of the permutations in the output list is not guaranteed to be in any specific order.
    """
    # Initialize an empty list to store the permutations.
    output: list[list[int]] = []
    # Start generating permutations from the first index of the list.
    output = backtrack(output, nums, 0)

    # Return the list of permutations.
    return output


if __name__ == '__main__':
    print(__doc__)
