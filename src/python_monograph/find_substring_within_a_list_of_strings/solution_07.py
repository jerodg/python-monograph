"""
Python Monograph -> Find a Substring Within a List -> Solution 07

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
import re


def find_substring(strings: list[str], pattern: str) -> int | None:
    """
    This function finds a substring within a list of strings using regular expressions and returns the index of the first string
    in the list where the pattern is found as a substring. If the pattern is not found in any string, it returns None.

    Args:
        strings (List[str]): A list of strings where the pattern is to be searched.
        pattern (str): The target string to be searched as a substring in the list of strings.

    Returns:
        Optional[int]: The index of the first string in the list where the pattern is found as a substring.
                       If the pattern is not found in any string, it returns None.

    Raises:
        ValueError: If the list of strings is empty.

    Examples:
        >>> find_substring(["hello", "world", "python", "programming"], "pyt")
        2
        >>> find_substring(["hello", "world", "python", "programming"], "java") is None
        True
        >>> find_substring(["hello", "world", "python", "programming"], "o")
        0
        >>> find_substring(["hello", "world", "python", "programming"], "")
        0
        >>> find_substring([], "hello")
        Traceback (most recent call last):
        ...
        ValueError: The list of strings cannot be empty.
    """
    # Raise an error if the list of strings is empty
    if not strings:
        raise ValueError("The list of strings cannot be empty.")

    # Iterate over each string in the list
    for i, string in enumerate(strings):
        # Use regular expressions to search for the pattern in the current string
        if re.search(pattern, string):
            # If found, return the index of the string
            return i

    # If the pattern is not found in any string, return None
    return None
