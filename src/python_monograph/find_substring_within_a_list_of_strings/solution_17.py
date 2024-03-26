"""
Python Monograph -> Find a Substring Within a List -> Solution 17

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


def compute_prefix_function(pattern: str) -> list:
    """
    Computes the prefix function for the given pattern. The prefix function is used in the Knuth-Morris-Pratt (KMP)
    string matching algorithm. It computes, for each position i in the pattern, the length of the longest proper prefix
    of the substring pattern[0..i] which is also a suffix of this substring.

    Args:
        pattern (str): The pattern for which to compute the prefix function.

    Returns:
        list: The prefix function for the given pattern.

    Doctest:
        >>> compute_prefix_function("ABABDABACD")
        [0, 0, 1, 2, 0, 1, 2, 3, 0, 0]
        >>> compute_prefix_function("AAABAAA")
        [0, 1, 2, 0, 1, 2, 3]
        >>> compute_prefix_function("ABCDE")
        [0, 0, 0, 0, 0]
        >>> compute_prefix_function("AABAACAABAA")
        [0, 1, 0, 1, 2, 0, 1, 2, 3, 4, 5]
        >>> compute_prefix_function("AAACAAAAAC")
        [0, 1, 2, 0, 1, 2, 3, 3, 3, 4]
    """
    prefix_function = [0] * len(pattern)  # Initialize the prefix function array with zeros
    j = 0  # Initialize the length of the previous longest prefix suffix

    # Iterate over the characters in the pattern
    for i in range(1, len(pattern)):
        # Handle the case where the current character does not match the next character in the previous longest prefix suffix
        while j > 0 and pattern[i] != pattern[j]:
            j = prefix_function[j - 1]

        # Handle the case where the current character matches the next character in the previous longest prefix suffix
        if pattern[i] == pattern[j]:
            j += 1

        # Update the prefix function for the current position
        prefix_function[i] = j

    return prefix_function


def find_substring(strings: list[str], pattern: str) -> int | None:
    """
    This function finds the first occurrence of a pattern in a list of strings using the Knuth-Morris-Pratt (KMP) algorithm.
    It iterates over each string in the list, and for each character in the string, it checks if it matches the next character in the pattern.
    If the entire pattern is found in a string, it returns the index of that string in the list.
    If the pattern is not found in any string, it returns None.

    Args:
        strings (list[str]): The list of strings to search in.
        pattern (str): The pattern to search for.

    Returns:
        int | None: The index of the first string in the list where the pattern is found as a substring.
                     If the pattern is not found in any string, it returns None.

    Raises:
        ValueError: If the list of strings is empty or the pattern is empty.

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
        ValueError: The pattern cannot be empty.
        >>> find_substring([], "hello")
        Traceback (most recent call last):
        ...
        ValueError: The list of strings cannot be empty.
    """
    if not strings:
        raise ValueError("The list of strings cannot be empty.")

    if not pattern:
        raise ValueError("The pattern cannot be empty.")

    prefix_function = compute_prefix_function(pattern)  # Compute the prefix function for the pattern

    # Iterate over each string in the list
    for index, string in enumerate(strings):
        j = 0  # Initialize the length of the previous longest prefix suffix

        # Iterate over the characters in the string
        for i in range(len(string)):
            # Handle the case where the current character does not match the next character in the previous longest prefix suffix
            while j > 0 and string[i] != pattern[j]:
                j = prefix_function[j - 1]

            # Handle the case where the current character matches the next character in the previous longest prefix suffix
            if string[i] == pattern[j]:
                j += 1

            # If the entire pattern has been found, return the index of the string in the list
            if j == len(pattern):
                return index

    # If the pattern is not found in any string, return None
    return None
