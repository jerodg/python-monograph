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
        '1.5 KB'
        >>> calculate_data_size(1500, 'binary')
        '1.465 KiB'
        >>> calculate_data_size(1500, 'bits')
        '12 Kb'
        >>> calculate_data_size(1500, 'nibbles')
        '3 Kn'
        >>> calculate_data_size(1024, 'binary')
        '1 KiB'
    """
    if size < 0:
        raise ValueError('Size cannot be negative.')

    # Define the suffixes for each notation
    suffixes = {'decimal': ['B', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'],
            'binary'     : ['B', 'KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB'],
            'bits'       : ['b', 'Kb', 'Mb', 'Gb', 'Tb', 'Pb', 'Eb', 'Zb', 'Yb'],
            'nibbles'    : ['n', 'Kn', 'Mn', 'Gn', 'Tn', 'Pn', 'En', 'Zn', 'Yn']}

    # Define the base for each notation
    bases = {'decimal': 1000, 'binary': 1024, 'bits': 1000, 'nibbles': 1000}

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
    def calculate_suffix_index(size: int, index: int = 0) -> int:
        """
        Recursive function to calculate the index of the suffix to use.

        This function is used to determine the appropriate suffix (e.g., 'KB', 'MB', 'GB', etc.)
        for a given size in bytes. It does this by recursively dividing the size by the base
        (1024 for binary notation, 1000 for decimal notation) until the size is less than the base
        or until the maximum suffix has been reached.

        Args:
            size (int): The size in bytes.
            index (int, optional): The current index in the suffix list. Defaults to 0.

        Returns:
            int: The index of the suffix to use in the suffix list.

        Examples:
            >>> calculate_suffix_index(1500)
            1
            >>> calculate_suffix_index(1048576)
            2
            >>> calculate_suffix_index(1073741824)
            3
            >>> calculate_suffix_index(1099511627776)
            4
            >>> calculate_suffix_index(1125899906842624)
            5
        """
        if size < base or index == len(suffix_list) - 1:
            # If the size is less than the base or the maximum suffix has been reached,
            # return the current index.
            return index
        else:
            # Otherwise, divide the size by the base and increment the index,
            # then call the function again with the new values.
            return calculate_suffix_index(size / base, index + 1)

    # Calculate the index of the suffix to use using recursion
    index = calculate_suffix_index(size)
    size /= base ** index

    # Return the size with the appropriate suffix
    size = f'{size:.3f}'.rstrip('0').rstrip('.')
    return f'{size} {suffix_list[index]}'
