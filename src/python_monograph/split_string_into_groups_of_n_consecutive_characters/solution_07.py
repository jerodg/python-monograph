"""
Python Monograph -> Split Strings into Groups of n Consecutive Characters  -> Solution 07

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
import pandas as pd


def split_string_into_groups(s: str, n: int) -> list[str]:
    """
    Splits a given string into groups of `n` consecutive characters.

    This function uses the pandas library to convert the string into a pandas Series,
    then uses the groupby method to group the characters into groups of `n` characters.
    The groups are then converted back to a list of strings.

    Args:
        s (str): The input string to be split.
        n (int): The size of the groups.

    Returns:
        list[str]: A list of strings, where each string is a group of `n` consecutive characters from the input string.

    Raises:
        ValueError: If `n` is not a positive integer.

    Examples:
        >>> split_string_into_groups("HelloWorld", 3)
        ['Hel', 'loW', 'orl', 'd']
        >>> split_string_into_groups("Python", 2)
        ['Py', 'th', 'on']
        >>> split_string_into_groups("1234567890", 4)
        ['1234', '5678', '90']
        >>> split_string_into_groups("abc", 1)
        ['a', 'b', 'c']
        >>> split_string_into_groups("abc", 5)
        ['abc']
    """
    # Check if `n` is a positive integer
    if n <= 0:
        raise ValueError("The group size must be a positive integer")

    # Convert the string to a pandas Series
    s = pd.Series(list(s))

    # Use pandas groupby to group the characters
    # The index of each character is divided by `n` using integer division,
    # which groups the characters into groups of `n` characters.
    groups = s.groupby(s.index // n).agg(''.join)

    # Convert the result back to a list and return it
    return groups.tolist()
