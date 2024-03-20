"""
Python Monograph: Calculate Data Size Solution 02

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


def calculate_data_size(size: int, notation: str = 'decimal') -> str:
    """
    Calculate the data size in different notations using a lookup table approach.

    This function takes a size in bytes and a notation, and returns a string representing the size in the appropriate notation.

    Args:
        size (int): The size in bytes.
        notation (str, optional): The notation to use for the size calculation. Defaults to 'decimal'.

    Raises:
        ValueError: If the size is negative or if the notation is not 'decimal', 'binary', 'bits', or 'nibbles'.

    Returns:
        str: A string representing the size in the appropriate notation.

    Doctest:
        >>> calculate_data_size(1500, 'decimal')
        '1.50 KB'
        >>> calculate_data_size(1500, 'binary')
        '1.46 KiB'
        >>> calculate_data_size(1500, 'bits')
        '12.00 Kb'
        >>> calculate_data_size(1500, 'nibbles')
        '6.00 Kn'
        >>> calculate_data_size(1024, 'binary')
        '1.00 KiB'
    """
    # Check if size is negative
    if size < 0:
        raise ValueError('Size cannot be negative.')

    # Check the notation and set the appropriate suffixes and base
    if notation == 'decimal':
        suffixes = ['B', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB']
        base = 1000
    elif notation == 'binary':
        suffixes = ['B', 'KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']
        base = 1024
    elif notation == 'bits':
        suffixes = ['b', 'Kb', 'Mb', 'Gb', 'Tb', 'Pb', 'Eb', 'Zb', 'Yb']
        base = 1000
        size *= 8  # convert bytes to bits
    elif notation == 'nibbles':
        suffixes = ['n', 'Kn', 'Mn', 'Gn', 'Tn', 'Pn', 'En', 'Zn', 'Yn']
        base = 1000
        size *= 2  # convert bytes to nibbles
    else:
        raise ValueError("Invalid notation. Please choose 'decimal', 'binary', 'bits', or 'nibbles'.")

    # Create a lookup table for the thresholds for each suffix
    thresholds = [base ** i for i in range(len(suffixes))]

    # Find the appropriate suffix by searching the lookup table
    for i in reversed(range(len(thresholds))):
        if size >= thresholds[i]:
            size /= thresholds[i]
            return f'{size:3.2f} {suffixes[i]}'

    return '0.00 B'