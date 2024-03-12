"""
Python Monograph -> Split Strings into Groups of n Consecutive Characters  -> Solution 00

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


def split_string_into_groups(string: str, n: int) -> list:
    """
    Splits a given string into groups of `n` consecutive characters.

    This function uses Python's slicing feature and list comprehension to split the string.
    It iterates over the string with a step size of `n` and slices the string from the current index to the current index plus `n`.
    Each sliced string is then added to a set to remove duplicates. Finally, the set is converted back to a list and returned.

    Note: This function does not preserve the original order of the groups. If the order is important, consider a different approach.

    Args:
        string (str): The input string to be split.
        n (int): The size of the groups in which the string should be split.

    Returns:
        list: A list of unique strings, where each string is a group of `n` consecutive characters from the input string.

    Raises:
        ValueError: If the group size `n` is not a positive integer.

    Examples:
        >>> split_string_into_groups("HelloWorld", 3)
        ['loW', 'orl', 'd', 'Hel']

        >>> split_string_into_groups("Python", 2)
        ['th', 'on', 'Py']
    """
    if n <= 0:
        raise ValueError("Group size should be a positive integer")

    return list(set(string[i:i + n] for i in range(0, len(string), n)))
