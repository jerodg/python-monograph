#!/usr/bin/env python3
"""Python Monograph: Find All Permutations of a List of Lists Solution 03

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


def solution_03(nums: list[int]) -> list[list[int]]:
    """
    This function generates all permutations of a given list of integers using an iterative approach.

    Args:
        nums (list[int]): The input list of integers.

    Returns:
        list[list[int]]: A list of all permutations of the input list. Each permutation is represented as a list of integers.

    Examples:
        >>> solution_03([1, 2, 3])
        [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    """
    # Initialize the output list with the input list as the first permutation.
    output = [nums]

    # Iterate over the length of the input list.
    for _ in range(1, len(nums)):
        # Initialize a new output list for the next iteration.
        new_output = []

        # Iterate over each permutation in the output list.
        for perm in output:
            # Iterate over each index in the permutation.
            for i in range(len(perm)):
                # Create a new permutation by inserting the last element of the permutation at each index.
                new_perm = perm[:i] + [perm[-1]] + perm[i:-1]

                # Add the new permutation to the new output list.
                new_output.append(new_perm)

        # Update the output list with the new output list.
        output = new_output

    # Return the output list of all permutations.
    return output


if __name__ == '__main__':
    print(__doc__)
