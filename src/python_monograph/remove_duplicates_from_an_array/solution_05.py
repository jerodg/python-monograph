"""
Python Monograph -> Remove Duplicates from an Array -> Solution 05

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
import itertools


def remove_duplicates(arr: list) -> list:
    """
    This function removes duplicates from a given list using the itertools.filterfalse() function approach.

    Args:
        arr (list): The input list from which duplicates need to be removed.

    Returns:
        list: A new list with duplicates removed. The order of elements is preserved.

    Doctest:
        >>> remove_duplicates([1, 2, 2, 3, 4, 4, 5, 5])
        [1, 2, 3, 4, 5]
        >>> remove_duplicates(['a', 'b', 'b', 'c', 'd', 'd', 'e', 'e'])
        ['a', 'b', 'c', 'd', 'e']

    Note:
        This function preserves the original order of elements in the list.
    """
    # Initialize an empty list to store the unique elements
    result = []

    def already_in_result(x):
        """
        This function checks if an element is already in the result list.

        Args:
            x (Any): The element to check.

        Returns:
            bool: True if the element is in the result list, False otherwise.
        """
        # If the element is in the result list, return True
        if x in result:
            return True
        else:
            # Otherwise, append the element to the result list and return False
            result.append(x)
            return False

    # Use the itertools.filterfalse() function to filter out the elements that are already in the result list
    list(itertools.filterfalse(already_in_result, arr))
    # Return the result list
    return result
