#!/usr/bin/env python3
"""Python Monograph: Find All Permutations of a List of Lists Solution 04

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


def solution_04(nums: list[int]) -> list[list[int]]:
    """
    This function generates all permutations of a given list of integers using a stack-based approach.

    Args:
        nums (list[int]): The input list of integers.

    Returns:
        list[list[int]]: A list of all permutations of the input list. Each permutation is represented as a list of integers.

    Examples:
        >>> solution([1, 2, 3])
        [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    """
    # Initialize the stack with the input list and an empty permutation.
    stack = [(nums, [])]

    # Initialize the output list.
    output = []

    # While the stack is not empty.
    while stack:
        # Pop a list and a permutation from the stack.
        nums, perm = stack.pop()

        # If the list is empty, add the permutation to the output list.
        if not nums:
            output.append(perm)
        else:
            # For each number in the list.
            for i in range(len(nums)):
                # Push a new list (with the current number removed) and a new permutation (with the current number added) to the
                # stack.
                stack.append((nums[:i] + nums[i + 1 :], perm + [nums[i]]))

    # Return the output list of all permutations.
    return output


if __name__ == '__main__':
    print(__doc__)
