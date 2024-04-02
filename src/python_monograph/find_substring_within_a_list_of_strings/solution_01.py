"""
Python Monograph -> Find a Substring Within a List -> Solution 01

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
    Finds the first occurrence of a pattern in a list of strings using a naive string matching algorithm.

    This function iterates over each string in the list, and for each string, it iterates over the characters in the string.
    For each character, it checks if the pattern matches the current substring of the string. If the pattern is found,
    it returns the index of the string in the list. If the pattern is not found in any string, it returns None.

    Args:
        strings (list[str]): The list of strings to search in.
        target (str): The pattern to search for.

    Returns:
        Union[int, None]: The index of the first string in the list where the pattern is found as a substring.
                          If the pattern is not found in any string, it returns None.

    Raises:
        ValueError: If the list of strings is empty or the target string is empty.

    Doctest:
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
        >>> find_substring([], "hello")
        Traceback (most recent call last):
        ...
        ValueError: The list of strings cannot be empty.
    """
    # Check if the list of strings is empty
    if not strings:
        raise ValueError("The list of strings cannot be empty.")

    # Check if the target string is empty
    if not target:
        raise ValueError("The target string cannot be empty.")

    # Iterate over each string in the list
    for index, string in enumerate(strings):
        # Iterate over the characters in the string
        for i in range(len(string) - len(target) + 1):
            # Check if the pattern matches the current substring of the string
            if string[i:i + len(target)] == target:
                # If the pattern is found, return the index of the string in the list
                return index

    # If the pattern is not found in any string, return None
    return None
