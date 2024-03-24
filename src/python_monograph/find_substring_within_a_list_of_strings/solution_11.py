"""
Python Monograph -> Find a Substring Within a List -> Solution 11

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


# fixme: This is a work in progress. It is not yet functional.

def compute_lps(pattern: str) -> list:
    """
    Computes the Longest Proper Prefix which is also suffix (LPS) array for the pattern string.
    This array will be used to skip characters while matching in the KMP algorithm.

    Args:
        pattern (str): The pattern string for which the LPS array is to be computed.

    Returns:
        list: The LPS array for the pattern string.

    Doctest:
        >>> compute_lps("ABAB")
        [0, 0, 1, 2]
        >>> compute_lps("AAAA")
        [0, 1, 2, 3]
        >>> compute_lps("ABCDE")
        [0, 0, 0, 0, 0]
        >>> compute_lps("AAABAAA")
        [0, 1, 2, 0, 1, 2, 3]
        >>> compute_lps("")
        []
    """
    length = 0  # Length of the previous longest prefix suffix
    lps = [0] * len(pattern)  # lps[0] is always 0
    i = 1  # The loop variable

    # Calculate lps[i] for i = 1 to len(pattern)
    while i < len(pattern):
        # case 1: pattern[i] == pattern[length]
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            # case 2: pattern[i] != pattern[length]
            if length != 0:
                # This is tricky. Consider the example.
                # AAACAAAA and i = 7. The idea is similar
                # to search step.
                length = lps[length - 1]
            else:
                # if (length == 0)
                lps[i] = 0
                i += 1

    return lps


def find_substring(strings: list, pattern: str) -> [int | None]:
    """
    Finds the first occurrence of a pattern in a list of strings using the Knuth-Morris-Pratt (KMP) algorithm.

    Args:
        strings (list): The list of strings to search in.
        pattern (str): The pattern to search for.

    Returns:
        int | None: The index of the first string in the list where the pattern is found as a substring.
                     If the pattern is not found in any string, it returns None.

    Doctest:
        >>> find_substring(["hello", "world", "python", "programming"], "pyt")
        2
        >>> find_substring(["hello", "world", "python", "programming"], "java")
        None
        >>> find_substring(["hello", "world", "python", "programming"], "o")
        0
        >>> find_substring(["hello", "world", "python", "programming"], "")
        0
        >>> find_substring([], "hello")
        None
    """
    lps = compute_lps(pattern)  # Compute the Longest Proper Prefix array for the pattern

    for index, string in enumerate(strings):  # Iterate over each string in the list
        i = j = 0  # Initialize pointers for the string and the pattern
        while i < len(string):  # While we have not reached the end of the string
            if string[i] == pattern[j]:  # If the characters match
                i += 1
                j += 1
            if j == len(pattern):  # If we have found a match
                return index  # Return the index of the string in the list
            elif i < len(string) and string[i] != pattern[j]:  # If the characters do not match
                if j != 0:  # If we have some matching characters
                    j = lps[j - 1]  # Use the LPS array to skip characters
                else:  # If we have no matching characters
                    i += 1  # Move to the next character in the string

    return None  # If no match is found in any string, return None
