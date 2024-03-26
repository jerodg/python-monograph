"""
Python Monograph -> Find a Substring Within a List -> Solution 18

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


def compute_bad_char_table(pattern: str) -> dict:
    """
    Computes the bad character table for the given pattern. The bad character table is used in the Boyer-Moore
    string matching algorithm. It computes, for each character in the pattern, the last occurrence of that character.

    Args:
        pattern (str): The pattern for which to compute the bad character table.

    Returns:
        dict: The bad character table for the given pattern.

    Doctest:
        >>> compute_bad_char_table("ABABDABACD")
        {'A': 7, 'B': 6, 'D': 9, 'C': 8}
        >>> compute_bad_char_table("AAABAAA")
        {'A': 6, 'B': 3}
        >>> compute_bad_char_table("ABCDE")
        {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4}
        >>> compute_bad_char_table("AABAACAABAA")
        {'A': 10, 'B': 8, 'C': 5}
        >>> compute_bad_char_table("AAACAAAAAC")
        {'A': 8, 'C': 9}
    """
    bad_char_table = {}  # Initialize the bad character table as an empty dictionary

    # Iterate over the characters in the pattern
    for i in range(len(pattern)):
        # For each character, store its last occurrence in the bad character table
        bad_char_table[pattern[i]] = i

    return bad_char_table


def find_substring(strings: list[str], pattern: str) -> int | None:
    """
    This function finds the first occurrence of a pattern in a list of strings using the Boyer-Moore algorithm.
    The Boyer-Moore algorithm is a string searching algorithm that finds the first occurrence of a pattern in a text in linear time.
    It uses a bad character heuristic to skip sections of the text, resulting in a lower constant factor than many other string
    algorithms in practice.

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

    # Compute the bad character table for the pattern
    bad_char_table = compute_bad_char_table(pattern)

    # Iterate over each string in the list
    for index, string in enumerate(strings):
        # Initialize the pointers for the string and the pattern
        s = p = len(pattern) - 1

        # Iterate over the characters in the string from right to left
        while s < len(string):
            # If the current character in the string matches the current character in the pattern
            if string[s] == pattern[p]:
                # If the entire pattern has been found, return the index of the string in the list
                if p == 0:
                    return index
                else:
                    # Move the pointers to the left
                    s -= 1
                    p -= 1
            else:
                # If the current character in the string does not match the current character in the pattern
                # Shift the pattern to the right by the appropriate amount
                s += len(pattern) - min(p, 1 + bad_char_table.get(string[s], -1))
                # Reset the pattern pointer to the rightmost character
                p = len(pattern) - 1

    # If the pattern is not found in any string, return None
    return None
