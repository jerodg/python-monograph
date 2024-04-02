"""
Python Monograph: Calculate Data Size Solution 04

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


class DataSize:
    """
    A class used to represent a Data Size.

    This class takes a size in bytes and a notation, and provides a method to calculate and return a string representing the size
    in the appropriate notation.

    Attributes:
        size (int): The size in bytes.
        notation (str): The notation to use for the size calculation.
        suffixes (dict): A dictionary mapping notations to their corresponding suffixes.
        bases (dict): A dictionary mapping notations to their corresponding bases.

    Methods:
        calculate_data_size(): Calculates the size in the appropriate notation and returns it as a string.

    Doctest:
        >>> ds = DataSize(1500, 'decimal')
        >>> ds.calculate_product_sum()
        '1.5 KB'
        >>> ds = DataSize(1500, 'binary')
        >>> ds.calculate_product_sum()
        '1.465 KiB'
        >>> ds = DataSize(1500, 'bits')
        >>> ds.calculate_product_sum()
        '12 Kb'
        >>> ds = DataSize(1500, 'nibbles')
        >>> ds.calculate_product_sum()
        '3 Kn'
        >>> ds = DataSize(1024, 'binary')
        >>> ds.calculate_product_sum()
        '1 KiB'
    """

    def __init__(self, size: int, notation: str = 'decimal'):
        """
        Constructs all the necessary attributes for the DataSize object.

        Args:
            size (int): The size in bytes.
            notation (str, optional): The notation to use for the size calculation. Defaults to 'decimal'.

        Raises:
            ValueError: If the size is negative or if the notation is not 'decimal', 'binary', 'bits', or 'nibbles'.
        """
        if size < 0:
            raise ValueError('Size cannot be negative.')
        self.size = size
        self.notation = notation
        self.suffixes = {'decimal': ['B', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'],
                'binary'          : ['B', 'KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB'],
                'bits'            : ['b', 'Kb', 'Mb', 'Gb', 'Tb', 'Pb', 'Eb', 'Zb', 'Yb'],
                'nibbles'         : ['n', 'Kn', 'Mn', 'Gn', 'Tn', 'Pn', 'En', 'Zn', 'Yn']}
        self.bases = {'decimal': 1000, 'binary': 1024, 'bits': 1000, 'nibbles': 1000}
        if notation not in self.suffixes:
            raise ValueError("Invalid notation. Please choose 'decimal', 'binary', 'bits', or 'nibbles'.")

    def calculate_data_size(self) -> str:
        """
        Calculates the size in the appropriate notation and returns it as a string using an object-oriented approach.

        This method first determines the base for the calculation based on the notation.
        If the notation is 'bits', it converts the size from bytes to bits by multiplying by 8.
        If the notation is 'nibbles', it converts the size from bytes to nibbles by multiplying by 2.
        It then divides the size by the base until the size is less than the base or it has gone through all the suffixes for the
        notation.
        Finally, it formats the size as a string with 3 decimal places, removes trailing zeros and the decimal point if it's at
        the end, and returns the size with the appropriate suffix.

        Returns:
            str: A string representing the size in the appropriate notation.

        Examples:
            >>> calculator = DataSize(1500, 'decimal')
            >>> calculator.calculate_product_sum()
            '1.5 KB'

            >>> calculator = DataSize(1500, 'binary')
            >>> calculator.calculate_product_sum()
            '1.465 KiB'

            >>> calculator = DataSize(1500, 'bits')
            >>> calculator.calculate_product_sum()
            '12 Kb'

            >>> calculator = DataSize(1500, 'nibbles')
            >>> calculator.calculate_product_sum()
            '3 Kn'

            >>> calculator = DataSize(1024, 'binary')
            >>> calculator.calculate_product_sum()
            '1 KiB'
        """
        base = self.bases[self.notation]  # Determine the base for the calculation

        # Convert the size from bytes to bits or nibbles if necessary
        if self.notation == 'bits':
            self.size *= 8  # convert bytes to bits
        elif self.notation == 'nibbles':
            self.size *= 2  # convert bytes to nibbles

        index = 0
        # Divide the size by the base until the size is less than the base or we've gone through all the suffixes
        while self.size >= base and index < len(self.suffixes[self.notation]) - 1:
            self.size /= base
            index += 1

        # Format the size as a string with 3 decimal places, remove trailing zeros and the decimal point if it's at the end
        size = f'{self.size:.3f}'.rstrip('0').rstrip('.')
        # Return the size with the appropriate suffix
        return f'{size} {self.suffixes[self.notation][index]}'
