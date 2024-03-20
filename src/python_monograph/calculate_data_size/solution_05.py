"""
Python Monograph: Calculate Data Size Solution 05

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
    Calculate the data size in different notations using a functional programming approach.

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
    if size < 0:
        raise ValueError('Size cannot be negative.')

    # Define the suffixes for each notation
    suffixes = {
        'decimal': ['B', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'],
        'binary':  ['B', 'KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB'],
        'bits':    ['b', 'Kb', 'Mb', 'Gb', 'Tb', 'Pb', 'Eb', 'Zb', 'Yb'],
        'nibbles': ['n', 'Kn', 'Mn', 'Gn', 'Tn', 'Pn', 'En', 'Zn', 'Yn']
    }

    # Define the base for each notation
    bases = {
        'decimal': 1000,
        'binary':  1024,
        'bits':    1000,
        'nibbles': 1000
    }

    # Check if the notation is valid
    if notation not in suffixes:
        raise ValueError("Invalid notation. Please choose 'decimal', 'binary', 'bits', or 'nibbles'.")

    # Convert bytes to bits or nibbles if necessary
    if notation == 'bits':
        size *= 8  # convert bytes to bits
    elif notation == 'nibbles':
        size *= 2  # convert bytes to nibbles

    base = bases[notation]
    suffix_list = suffixes[notation]

    # Recursive function to calculate the index of the suffix to use
    def calculate_suffix_index(size, index=0):
        if size < base or index == len(suffix_list) - 1:
            return index
        else:
            return calculate_suffix_index(size / base, index + 1)

    # Calculate the index of the suffix to use using recursion
    index = calculate_suffix_index(size)
    size /= base ** index

    # Return the size with the appropriate suffix
    return f'{size:3.2f} {suffix_list[index]}'
