"""
Python Monograph -> Find a Substring Within a List -> Solution 19

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


def compute_hash(s: str, modulus: int, base: int) -> int:
    """
    Computes the hash value of a string using a specific modulus and base.

    This function is used in the Rabin-Karp string matching algorithm. It computes the hash value of a string by
    summing up the ASCII value of each character in the string, multiplied by the base raised to the power of the
    position of the character in the string, and then taking the modulus of the result.

    Args:
        s (str): The string for which to compute the hash value.
        modulus (int): The modulus to use in the computation.
        base (int): The base to use in the computation.

    Returns:
        int: The hash value of the string.

    Doctest:
        >>> compute_hash("hello", 10**9 + 7, 26)
        3752127
        >>> compute_hash("world", 10**9 + 7, 26)
        10786572
        >>> compute_hash("python", 10**9 + 7, 26)
        201883748
        >>> compute_hash("programming", 10**9 + 7, 26)
        787339245
        >>> compute_hash("", 10**9 + 7, 26)
        0
    """
    return sum((ord(s[i]) - ord('a') + 1) * pow(base, len(s) - i - 1) for i in range(len(s))) % modulus


def find_substring(strings: list[str], pattern: str) -> int | None:
    """
    This function finds the first occurrence of a pattern in a list of strings using the Rabin-Karp algorithm.
    The Rabin-Karp algorithm is a string searching algorithm that finds the first occurrence of a pattern in a text in linear time.
    It uses a hash function to convert the pattern and substrings of the text into integers, and then compares these integers for
    a match.

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
        ValueError: The target string cannot be empty.
        >>> find_substring([], "hello")
        Traceback (most recent call last):
        ...
        ValueError: The list of strings cannot be empty.
    """
    if not strings:
        raise ValueError("The list of strings cannot be empty.")

    if not pattern:
        raise ValueError("The target string cannot be empty.")

    modulus = 10 ** 9 + 7  # Large prime number
    base = 26  # Number of characters in the alphabet
    pattern_hash = compute_hash(pattern, modulus, base)  # Compute the hash value of the pattern

    # Iterate over each string in the list
    for index, string in enumerate(strings):
        string_hash = compute_hash(string[:len(pattern)], modulus,
                                   base)  # Compute the hash value of the first substring of the string
        # If the hash values of the pattern and the substring are equal and the substring is equal to the pattern
        if string_hash == pattern_hash and string[:len(pattern)] == pattern:
            return index  # Return the index of the string in the list
        # Iterate over the rest of the string
        for i in range(len(pattern), len(string)):
            # Update the hash value of the substring
            string_hash = ((string_hash - (ord(string[i - len(pattern)]) - ord('a') + 1) * pow(base, len(pattern) - 1)) * base + (
                    ord(string[i]) - ord('a') + 1)) % modulus
            # If the hash values of the pattern and the substring are equal and the substring is equal to the pattern
            if string_hash == pattern_hash and string[i - len(pattern) + 1:i + 1] == pattern:
                return index  # Return the index of the string in the list

    return None  # If the pattern is not found in any string, return None
