#!/usr/bin/env python3
"""Python Monograph: Calculate Data Size Automatically Solution 00

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
If not, see <https://www.mongodb.com/licensing/server-side-public-license>."""


def method_00(size: int, notation: str = 'decimal') -> str:
    """Convert a given size in bytes to a human-readable format using either decimal or binary notation.

    This function takes a size in bytes and a notation (either 'decimal' or 'binary') and returns a string
    representing the size in a human-readable format. The 'decimal' notation uses a base of 1000 and the 'binary'
    notation uses a base of 1024.

    Args:
        size (int): The size in bytes to convert.
        notation (str): The notation to use for the conversion. Must be either 'decimal' or 'binary'. Defaults to 'decimal'.

    Returns:
        str: A string representing the size in a human-readable format.

    Raises:
        ValueError: If the size is negative or the notation is not 'decimal' or 'binary'.
    """
    # Check if the size is negative. If it is, raise a ValueError.
    if size < 0:
        raise ValueError('Size cannot be negative.')

    # Check the notation. If it's 'decimal', use the decimal suffixes and a base of 1000.
    # If it's 'binary', use the binary suffixes and a base of 1024.
    # If it's neither, raise a ValueError.
    if notation == 'decimal':
        suffixes = ['B', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB']
        base = 1000
    elif notation == 'binary':
        suffixes = ['B', 'KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']
        base = 1024
    else:
        raise ValueError("Invalid notation. Please choose 'decimal' or 'binary'.")

    # Initialize the index to 0. This will be used to select the appropriate suffix.
    index = 0

    # While the size is greater than or equal to the base and the index is less than the number of suffixes - 1,
    # divide the size by the base and increment the index.
    while abs(size) >= base and index < len(suffixes) - 1:
        size /= base
        index += 1

    # Return the size formatted as a string with 2 decimal places, followed by the appropriate suffix.
    return f'{size:3.2f} {suffixes[index]}'


if __name__ == '__main__':
    print(__doc__)
