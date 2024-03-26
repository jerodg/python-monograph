"""
Python Monograph: Calculate Data Size Solution 06

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


def validate_inputs(func):
    """
    This is a decorator function that validates the inputs of another function.

    This decorator checks if the size is negative or if the notation is not 'decimal', 'binary', 'bits', or 'nibbles',
    and raises a ValueError if so.

    Args:
        func (function): The function to decorate.

    Returns:
        function: The decorated function.

    Raises:
        ValueError: If size is negative or notation is not 'decimal', 'binary', 'bits', or 'nibbles'.

    Examples:
        >>> @validate_inputs
        ... def test_func(size, notation):
        ...     return size, notation
        ...
        >>> test_func(1000, 'decimal')
        (1000, 'decimal')
        >>> test_func(-1000, 'decimal')
        Traceback (most recent call last):
        ...
        ValueError: Size cannot be negative.
        >>> test_func(1000, 'invalid')
        Traceback (most recent call last):
        ...
        ValueError: Invalid notation. Please choose 'decimal', 'binary', 'bits', or 'nibbles'.
    """

    def wrapper(size: int, notation: str = 'decimal') -> str:
        # Check if size is negative
        if size < 0:
            raise ValueError('Size cannot be negative.')
        # Check if notation is valid
        if notation not in ['decimal', 'binary', 'bits', 'nibbles']:
            raise ValueError("Invalid notation. Please choose 'decimal', 'binary', 'bits', or 'nibbles'.")
        # If all checks pass, call the decorated function
        return func(size, notation)

    return wrapper


@validate_inputs
def calculate_data_size(size: int, notation: str = 'decimal') -> str:
    """
    Calculate the data size in different notations using a decorator pattern approach.

    This function takes a size in bytes and a notation, and returns a string representing the size in the appropriate notation.

    Args:
        size (int): The size in bytes.
        notation (str, optional): The notation to use for the size calculation. Defaults to 'decimal'.

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
    # Define the suffixes for each notation
    suffixes = {'decimal': ['B', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'],
            'binary'     : ['B', 'KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB'],
            'bits'       : ['b', 'Kb', 'Mb', 'Gb', 'Tb', 'Pb', 'Eb', 'Zb', 'Yb'],
            'nibbles'    : ['n', 'Kn', 'Mn', 'Gn', 'Tn', 'Pn', 'En', 'Zn', 'Yn']}

    # Define the base for each notation
    bases = {'decimal': 1000, 'binary': 1024, 'bits': 1000, 'nibbles': 1000}

    # Convert bytes to bits or nibbles if necessary
    if notation == 'bits':
        size *= 8  # convert bytes to bits
    elif notation == 'nibbles':
        size *= 2  # convert bytes to nibbles

    base = bases[notation]
    suffix_list = suffixes[notation]

    # Recursive function to calculate the index of the suffix to use

    def calculate_suffix_index(size: float, index: int = 0) -> int:
        """
        Recursive function to calculate the index of the suffix to use.

        This function takes a size and an index, and returns the index of the suffix to use in the appropriate notation.
        The function uses recursion to divide the size by the base until it's less than the base, incrementing the index at each 
        step.

        Args:
            size (float): The size in the appropriate unit (bytes, bits, or nibbles).
            index (int, optional): The current index of the suffix. Defaults to 0.

        Returns:
            int: The index of the suffix to use.

        Doctest:
            >>> calculate_suffix_index(1500)
            1
            >>> calculate_suffix_index(1500000)
            2
            >>> calculate_suffix_index(1500000000)
            3
            >>> calculate_suffix_index(1500, 1)
            1
            >>> calculate_suffix_index(1500000, 2)
            2
        """
        # If the size is less than the base or the index is the last index in the suffix list, return the index
        if size < base or index == len(suffix_list) - 1:
            return index
        else:
            # Otherwise, divide the size by the base and increment the index, and call the function again with the new size and
            # index
            return calculate_suffix_index(size / base, index + 1)

    # Calculate the index of the suffix to use using recursion
    index = calculate_suffix_index(size)
    size /= base ** index

    # Return the size with the appropriate suffix
    size = f'{size:.3f}'.rstrip('0').rstrip('.')
    return f'{size} {suffix_list[index]}'
