"""
Python Monograph -> Find a Substring Within a List -> Solution 09

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
import concurrent.futures


def worker(chunk: str, target: str) -> int | None:
    """
    Check if the target string is a substring of the chunk.

    This function takes a chunk of the concatenated string and the target string as input. It checks if the target string
    is a substring of the chunk and returns the index of the first occurrence of the target string in the chunk if it is,
    and None otherwise.

    Args:
        chunk (str): The chunk of the concatenated string to be checked.
        target (str): The target string to be searched in the chunk.

    Returns:
        int | None: The index of the first occurrence of the target string in the chunk if it is a substring, None otherwise.

    Raises:
        ValueError: If the target string is empty.

    Doctest:
        >>> worker("hello#world", "hell")
        0
        >>> worker("hello#world", "java") is None
        True
        >>> worker("hello#world", "o")
        4
        >>> worker("hello#world", "")
        Traceback (most recent call last):
        ...
        ValueError: The target string cannot be empty.
        >>> worker("hello#world", "hello")
        0
    """
    # Check if the target string is empty
    if not target:
        raise ValueError("The target string cannot be empty.")

    # Check if the target string is a substring of the chunk
    if target in chunk:
        # Return the index of the first occurrence of the target string in the chunk
        return chunk.index(target)

    # If the target string is not a substring of the chunk, return None
    return None


# fixme: Sometimes this returns the index for the first occurrence of the target string in the concatenated string
#           and other times it returns the index for the last occurrence of the target string in the concatenated string.
def find_substring(strings: list[str], target: str) -> int | None:
    """
    Search for a target string within a list of strings using a Parallel Computing approach.

    This function takes a list of strings and a target string as input. It uses a ThreadPoolExecutor to process each string
    in the list in parallel, and calls the worker function on each string. If the worker function returns a non-None result
    for any string, the function immediately returns the index of that string in the list. If the worker function returns
    None for all strings, the function returns None.

    Args:
        strings (list[str]): The list of strings to be processed.
        target (str): The target string to be searched in the strings.

    Returns:
        int | None: The index of the first string in the list that contains the target string as a substring, or None if
        no such string is found.

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
    """
    # Check if the list of strings is empty
    if not strings:
        raise ValueError("The list of strings cannot be empty.")

    # Check if the target string is empty
    if not target:
        raise ValueError("The target string cannot be empty.")

    # Create a ThreadPoolExecutor
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Submit the worker function for each string in the list to the executor
        futures = [executor.submit(worker, strings[i], target) for i in range(len(strings))]

        # Iterate over the futures as they complete
        for future in concurrent.futures.as_completed(futures):
            # If the future's result is not None, return the index of the string in the list
            if future.result() is not None:
                return futures.index(future)

    # If no string in the list contains the target string as a substring, return None
    return None
