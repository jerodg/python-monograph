"""
Python Monograph -> Find All Permutations of a List of n LIsts  -> Solution 01

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
If not, see <https://www.mongodb.com/licensing/server-side-public-license>.
"""


def find_all_permutations(lists: list[list[any]], index: int = 0) -> list[list[any]]:
    """
    Generate all possible permutations of the elements across all lists using backtracking.

    This function uses a recursive backtracking approach to generate all permutations. It starts with the first list and
    recursively generates permutations for the rest of the lists. It then inserts each element from the first list into
    all possible positions in each permutation of the rest of the lists.

    Args:
        lists (List[List[Any]]): A list of n lists.
        index (int): The current index in the list of lists. Defaults to 0.

    Returns:
        List[List[Any]]: A list of all possible permutations.

    Raises:
        TypeError: If the input is not a list of lists.

    Examples:
        >>> find_all_permutations([[1, 2], [3, 4]])
        [[1, 2, 3, 4], [1, 3, 2, 4], [1, 3, 4, 2], [1, 4, 2, 3], [1, 4, 3, 2], [2, 1, 3, 4], [2, 3, 1, 4], [2, 3, 4, 1], [2, 4,
        1, 3], [2, 4, 3, 1], [3, 4, 1, 2], [3, 4, 2, 1], [4, 3, 1, 2], [4, 3, 2, 1]]
    """
    # Check if the input is a list of lists
    if not all(isinstance(lst, list) for lst in lists):
        raise TypeError("Input must be a list of lists")

    # Base case: if there are no lists, return an empty list
    if not lists:
        return []

    # Base case: if there is only one list, return a list of lists with each element in its own list
    if len(lists) == 1:
        return [[element] for element in lists[0]]

    # Recursive case: generate permutations for the rest of the lists
    if index == len(lists) - 1:
        return [[element] for element in lists[index]]

    # Initialize an empty list to store the final permutations
    permutations = []

    # For each element in the current list, insert it into all possible positions in each permutation of the rest of the lists
    for element in lists[index]:
        for permutation in find_all_permutations(lists, index + 1):
            for i in range(len(permutation) + 1):
                new_permutation = permutation[:i] + [element] + permutation[i:]
                permutations.append(new_permutation)

    return permutations
