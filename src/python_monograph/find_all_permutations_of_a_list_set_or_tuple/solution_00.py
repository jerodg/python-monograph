"""
Python Monograph -> Find All Permutations of a List, Set, or Tuple  -> Solution 00

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
from itertools import permutations
from typing import Any, List


# fixme: This is a WIP
def find_all_permutations(data: [list | set | tuple]) -> list[tuple[Any, ...]]:
    """
    Generate all possible permutations of the elements across all lists, sets, or tuples using a brute-force approach.

    This function uses itertools.product to generate all combinations of elements across all lists, and then uses
    itertools.permutations on each combination to generate all permutations.

    Args:
        data (List[List[Any]]): A list of n lists.

    Returns:
        List[List[Any]]: A list of all possible permutations.

    Raises:
        TypeError: If the input is not a list of lists.

    Examples:
        >>> find_all_permutations([[1, 2], [3, 4]])
        [[1, 2, 3, 4], [1, 2, 4, 3], [1, 3, 2, 4], [1, 3, 4, 2], [1, 4, 2, 3], [1, 4, 3, 2], [2, 1, 3, 4], [2, 1, 4, 3], [2, 3, 1, 4], [2, 3, 4, 1], [2, 4, 1, 3], [2, 4, 3, 1], [3, 1, 2, 4], [3, 1, 4, 2], [3, 2, 1, 4], [3, 2, 4, 1], [3, 4, 1, 2], [3, 4, 2, 1], [4, 1, 2, 3], [4, 1, 3, 2], [4, 2, 1, 3], [4, 2, 3, 1], [4, 3, 1, 2], [4, 3, 2, 1]]
    """
    # Check if the input is a list of lists
    if not all(isinstance(lst, list) for lst in data):
        raise TypeError("Input must be a list of lists")

    # # Generate all combinations of elements across all lists
    # combinations = product(*data)
    #
    # # Generate all permutations for each combination
    # permutations_list = [list(permutation) for combination in combinations for permutation in permutations(combination)]
    #
    # return permutations_list
    print(list(permutations(data)), sep='\n')
    return list(permutations(data))
