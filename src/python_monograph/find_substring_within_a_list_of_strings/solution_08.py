"""
Python Monograph -> Find a Substring Within a List -> Solution 08

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


def find_substring(strings: list[str], target: str) -> int | None:
    """
    Search for a target string within a list of strings using a Dynamic Programming approach.

    This function takes a list of strings and a target string as input. It concatenates all the strings in the list into a
    single string, and then uses a Dynamic Programming approach to determine if the target string is a substring of the
    concatenated string. The function returns the index of the first occurrence of the target string in the list of strings,
    and None otherwise.

    Args:
        strings (list[str]): The list of strings to be concatenated and used to search for the target string.
        target (str): The target string to be searched in the concatenated string.

    Returns:
        int: The index of the first occurrence of the target string in the list of strings, None otherwise.

    Doctest:
        >>> find_substring(["hello", "world", "python", "programming"], "hell")
        0
        >>> find_substring(["hello", "world", "python", "programming"], "pyt")
        2
        >>> find_substring(["hello", "world", "python", "programming"], "java") is None
        True
        >>> find_substring(["hello", "world", "python", "programming"], "o")
        0
        >>> find_substring(["hello", "world", "python", "programming"], "")
        Traceback (most recent call last):
        ...
        ValueError: The target string cannot be empty.
        >>> find_substring(["hello", "world", "python", "programming"], "hello")
        0
    """
    if not strings:
        raise ValueError("The list of strings cannot be empty.")

    if not target:
        raise ValueError("The target string cannot be empty.")

    concatenated_string = '#'.join(strings)  # Concatenate the strings, separating them by a unique delimiter
    n = len(concatenated_string)  # Length of the concatenated string
    m = len(target)  # Length of the target string
    # Initialize a 2D boolean array with False
    dp = [[False] * n for _ in range(n)]

    for i in range(n):
        # If the character at index i in the concatenated string is equal to the first character of the target string
        if target and concatenated_string[i] == target[0]:
            dp[i][i] = True  # Set dp[i][i] to True

    for length in range(2, m + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            # If the substring from index i to j in the concatenated string is equal to the target string
            if concatenated_string[i:j + 1] == target:
                dp[i][j] = True  # Set dp[i][j] to True

    # Return the index of the first occurrence of the target string in the list of strings, or None if not found
    for i in range(n - m + 1):
        if dp[i][i + m - 1]:
            return concatenated_string[:i].count('#')

    return None
