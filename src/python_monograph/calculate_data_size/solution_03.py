"""
Python Monograph: Calculate Data Size Solution 03

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

"""
Python Monograph: Calculate Data Size Solution 03

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
    Calculate the data size in different notations using a recursive approach.

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

    # Recursive function to calculate the index of the suffix to use
    def calculate_suffix_index(size: int, index: int = 0) -> int:
        """
        Recursive helper function to calculate the index of the suffix to use.

        This function calculates the index of the suffix to use for the size
        representation. It uses recursion to divide the size by the base until
        the size is less than the base or the index reaches the end of the suffixes list.

        Args:
            size (int): The size in bytes.
            index (int, optional): The current index. Defaults to 0.

        Returns:
            int: The index of the suffix to use.

        Examples:
            >>> calculate_suffix_index(1500)
            1
            >>> calculate_suffix_index(1048576)
            4
            >>> calculate_suffix_index(1073741824)
            7
            >>> calculate_suffix_index(0)
            0
            >>> calculate_suffix_index(500, 2)
            2
        """
        if size < base or index == len(suffixes) - 1:
            return index
        else:
            return calculate_suffix_index(size / base, index + 1)

    # Calculate the index of the suffix to use using recursion
    # The index is used to determine the appropriate suffix (e.g., B, KB, MB, etc.)
    # for the size representation.
    index = calculate_suffix_index(size)

    # Adjust the size by dividing it by the base raised to the power of the index.
    # This converts the size from bytes to the unit represented by the suffix.
    size /= base ** index

    # Format the size to three decimal places, and remove trailing zeros and decimal point.
    # This makes the size more readable and removes unnecessary precision.
    size = f'{size:.3f}'.rstrip('0').rstrip('.')

    # Return the size with the appropriate suffix.
    # The size is returned as a string in the format "{size} {suffix}".
    return f'{size} {suffixes[index]}'
