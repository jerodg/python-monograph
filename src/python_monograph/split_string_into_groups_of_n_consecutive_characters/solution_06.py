"""
Python Monograph -> Split Strings into Groups of n Consecutive Characters  -> Solution 06

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
import numpy as np


def split_string_into_groups(s: str, n: int) -> list[str]:
    """
    Splits a string into groups of `n` consecutive characters using numpy.reshape().

    Args:
        s (str): The input string to be split.
        n (int): The size of the groups.

    Returns:
        List[str]: A list of strings where each string is a group of `n` consecutive characters.

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
    # Check if `n` is a positive integer.
    if n <= 0:
        raise ValueError("The group size must be a positive integer")

    # Convert the string to a list of characters
    chars = list(s)

    # Add extra empty strings only if the length of `s` is not a multiple of `n`
    if len(s) % n != 0:
        chars += [''] * (n - len(s) % n)

    # Reshape the array into a 2D array with the number of groups as the number of rows and n as the number of columns
    arr = np.array(chars).reshape(-1, n)

    # Convert each row of the 2D array back to a string and add it to the result list
    result = [''.join(row).rstrip() for row in arr]

    return result
