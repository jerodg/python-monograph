"""
Python Monograph -> Find a Substring Within a List -> Solution 13

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
    This function finds the index of the string that contains the target substring within a list of strings.
    It uses the `find()` method with a list comprehension to achieve this.

    Args:
        strings (list[str]): The list of strings to be searched.
        target (str): The target string to be searched for.

    Returns:
        int | None: The index of the string that contains the target substring if found, None otherwise.

    Raises:
        ValueError: If the list of strings is empty or the target string is empty.

    Doctest:
        >>> find_substring(["hello", "world", "python", "programming"], "hell")
        0
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
        >>> find_substring(["hello", "world", "python", "programming"], "pro")
        3
        >>> find_substring(["hello", "world", "python", "programming"], "worl")
        1
    """
    # Check if the list of strings is empty
    if not strings:
        raise ValueError("The list of strings cannot be empty.")

    # Check if the target string is empty
    if not target:
        raise ValueError("The target string cannot be empty.")

    # Use list comprehension and the find() method to check if the target string is a substring of any string in the list
    # If the target string is found, return the index of the first string that contains it
    # If the target string is not found in any string, return None
    return next((i for i, string in enumerate(strings) if string.find(target) != -1), None)