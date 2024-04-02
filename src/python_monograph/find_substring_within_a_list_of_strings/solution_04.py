"""
Python Monograph -> Find a Substring Within a List -> Solution 04

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


# fixme: This is returning a bool instead of the index of the pattern.

class SuffixArray:
    """
    A class used to represent a Suffix Array.

    A Suffix Array is a sorted array of all suffixes of a given string. It is a simpler and more space-efficient alternative
    to a Suffix Tree, and can be used to solve the problem of finding a substring within a list of strings in linear time.

    Attributes:
        concatenated_string (str): The concatenated string of all input strings, separated by a unique delimiter.
        suffix_array (list[str]): The sorted array of all suffixes of the concatenated string.

    Methods:
        search(pattern: str) -> bool: Searches for a pattern in the Suffix Array and returns True if found, False otherwise.

    Doctest:
        >>> sa = SuffixArray(["hello", "world", "python", "programming"])
        >>> sa.find_substring("hell")
        True
        >>> sa.find_substring("java")
        False
        >>> sa.find_substring("o")
        True
        >>> sa.find_substring("")
        True
        >>> sa.find_substring("hello")
        True
    """

    def __init__(self, strings: list[str]) -> None:
        """
        Initialize a SuffixArray object.

        This method takes a list of strings as input and concatenates them into a single string, separating them by a unique
        delimiter that does not appear in the strings. It then generates all the suffixes of the concatenated string and sorts
        them to create the Suffix Array.

        Args:
            strings (list[str]): The list of strings to be concatenated and used to create the Suffix Array.

        Doctest:
            >>> sa = SuffixArray(["hello", "world", "python", "programming"])
            >>> "hello" in sa.concatenated_string
            True
            >>> "world" in sa.concatenated_string
            True
            >>> "python" in sa.concatenated_string
            True
            >>> "programming" in sa.concatenated_string
            True
            >>> len(sa.suffix_array) == len(sa.concatenated_string)
            True
            >>> sa.suffix_array == sorted(sa.suffix_array)
            True
        """
        self.concatenated_string = '#'.join(strings)  # Concatenate the strings, separating them by a unique delimiter
        # Generate all the suffixes of the concatenated string and sort them to create the Suffix Array
        self.suffix_array = sorted([self.concatenated_string[i:] for i in range(len(self.concatenated_string))])

    def find_substring(self, pattern: str) -> bool:
        """
        Search for a pattern in the Suffix Array.

        This method takes a pattern as input and searches for it in the Suffix Array. It iterates over each suffix in the Suffix
        Array
        and checks if the pattern is a prefix of the current suffix. If it is, it returns True. If the pattern is not a prefix of
        any
        suffix in the Suffix Array, it returns False.

        Args:
            pattern (str): The pattern to be searched in the Suffix Array.

        Returns:
            bool: True if the pattern is found in the Suffix Array, False otherwise.

        Doctest:
            >>> sa = SuffixArray(["hello", "world", "python", "programming"])
            >>> sa.find_substring("hell")
            True
            >>> sa.find_substring("java")
            False
            >>> sa.find_substring("o")
            True
            >>> sa.find_substring("")
            True
            >>> sa.find_substring("hello")
            True
        """
        for suffix in self.suffix_array:  # For each suffix in the Suffix Array
            if suffix.startswith(pattern):  # If the pattern is a prefix of the current suffix
                return True  # Return True

        return False  # Return False if the pattern is not a prefix of any suffix in the Suffix Array
