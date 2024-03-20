"""
Python Monograph: Calculate Data Size Solution 08

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
from abc import ABC, abstractmethod
from math import floor, log2


class NotationStrategy(ABC):
    """
    Abstract base class for notation strategies.

    This class defines the interface for notation strategies. It declares an abstract method `calculate` that all concrete notation strategies must implement.

    Methods:
        calculate: Calculate the data size in a specific notation.

    Doctest:
        >>> class TestNotationStrategy(NotationStrategy):
        ...     def calculate(self, size: int) -> str:
        ...         return str(size)
        >>> test_strategy = TestNotationStrategy()
        >>> test_strategy.calculate(1500)
        '1500'
        >>> test_strategy.calculate(1024)
        '1024'
        >>> test_strategy.calculate(0)
        '0'
        >>> test_strategy.calculate(1)
        '1'
        >>> test_strategy.calculate(999)
        '999'
    """

    @abstractmethod
    def calculate(self, size: int) -> str:
        """
        Abstract method to calculate the data size in a specific notation.

        This method takes a size in bytes and returns a string representing the size in a specific notation. The specific notation is determined by the concrete class that implements this method.

        Args:
            size (int): The size in bytes.

        Returns:
            str: A string representing the size in a specific notation.

        Raises:
            NotImplementedError: This method must be implemented by a subclass.
        """
        raise NotImplementedError("This method must be implemented by a subclass.")


class DecimalNotationStrategy(NotationStrategy):
    """
    Concrete strategy for decimal notation.

    This class implements the NotationStrategy interface for decimal notation.
    It provides an implementation of the `calculate` method that calculates the data size in decimal notation.

    Methods:
        calculate: Calculate the data size in decimal notation.

    Doctest:
        >>> decimal_strategy = DecimalNotationStrategy()
        >>> decimal_strategy.calculate(1500)
        '1.50 KB'
        >>> decimal_strategy.calculate(1024)
        '1.02 KB'
        >>> decimal_strategy.calculate(0)
        '0.00 B'
        >>> decimal_strategy.calculate(1)
        '1.00 B'
        >>> decimal_strategy.calculate(999)
        '999.00 B'
    """

    def calculate(self, size: int) -> str:
        """
        Calculate the data size in decimal notation.

        This method takes a size in bytes and returns a string representing the size in decimal notation.
        The size is converted to the appropriate unit (B, KB, MB, GB, etc.) based on its magnitude,
        and the result is formatted as a number with 2 decimal places followed by the appropriate suffix.

        Args:
            size (int): The size in bytes.

        Returns:
            str: A string representing the size in decimal notation.
        """
        # List of suffixes for decimal notation
        suffixes = ['B', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB']

        # Calculate the index of the suffix to use
        index = floor(log2(size) / 10) if size != 0 else 0

        # Convert the size to the appropriate unit and format the result
        return f'{size / (1000.0 ** index):.2f} {suffixes[index]}'


class BinaryNotationStrategy(NotationStrategy):
    """
    Concrete strategy for binary notation.

    This class implements the NotationStrategy interface for binary notation.
    It provides an implementation of the `calculate` method that calculates the data size in binary notation.

    Methods:
        calculate: Calculate the data size in binary notation.

    Doctest:
        >>> binary_strategy = BinaryNotationStrategy()
        >>> binary_strategy.calculate(1500)
        '1.46 KiB'
        >>> binary_strategy.calculate(1024)
        '1.00 KiB'
        >>> binary_strategy.calculate(0)
        '0.00 B'
        >>> binary_strategy.calculate(1)
        '1.00 B'
        >>> binary_strategy.calculate(999)
        '999.00 B'
    """

    def calculate(self, size: int) -> str:
        """
        Calculate the data size in binary notation.

        This method takes a size in bytes and returns a string representing the size in binary notation.
        The size is converted to the appropriate unit (B, KiB, MiB, GiB, etc.) based on its magnitude,
        and the result is formatted as a number with 2 decimal places followed by the appropriate suffix.

        Args:
            size (int): The size in bytes.

        Returns:
            str: A string representing the size in binary notation.
        """
        # List of suffixes for binary notation
        suffixes = ['B', 'KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']

        # Calculate the index of the suffix to use
        index = floor(log2(size) / 10) if size != 0 else 0

        # Convert the size to the appropriate unit and format the result
        return f'{size / (1024.0 ** index):.2f} {suffixes[index]}'


class BitsNotationStrategy(NotationStrategy):
    """
    Concrete strategy for bits notation.

    This class implements the NotationStrategy interface for bits notation.
    It provides an implementation of the `calculate` method that calculates the data size in bits notation.

    Methods:
        calculate: Calculate the data size in bits notation.

    Doctest:
        >>> bits_strategy = BitsNotationStrategy()
        >>> bits_strategy.calculate(1500)
        '12.00 Kb'
        >>> bits_strategy.calculate(1024)
        '8.19 Kb'
        >>> bits_strategy.calculate(0)
        '0.00 b'
        >>> bits_strategy.calculate(1)
        '8.00 b'
        >>> bits_strategy.calculate(999)
        '7.99 Kb'
    """

    def calculate(self, size: int) -> str:
        """
        Calculate the data size in bits notation.

        This method takes a size in bytes and returns a string representing the size in bits notation.
        The size is converted to bits, then to the appropriate unit (b, Kb, Mb, Gb, etc.) based on its magnitude,
        and the result is formatted as a number with 2 decimal places followed by the appropriate suffix.

        Args:
            size (int): The size in bytes.

        Returns:
            str: A string representing the size in bits notation.
        """
        # List of suffixes for bits notation
        suffixes = ['b', 'Kb', 'Mb', 'Gb', 'Tb', 'Pb', 'Eb', 'Zb', 'Yb']

        # Convert size to bits
        size_bits = size * 8

        # Calculate the index of the suffix to use
        index = floor(log2(size_bits) / 10) if size_bits != 0 else 0

        # Convert the size to the appropriate unit and format the result
        return f'{size_bits / (1000.0 ** index):.2f} {suffixes[index]}'


class NibblesNotationStrategy(NotationStrategy):
    """
    Concrete strategy for nibbles notation.

    This class implements the NotationStrategy interface for nibbles notation.
    It provides an implementation of the `calculate` method that calculates the data size in nibbles notation.

    Methods:
        calculate: Calculate the data size in nibbles notation.

    Doctest:
        >>> nibbles_strategy = NibblesNotationStrategy()
        >>> nibbles_strategy.calculate(1500)
        '3.00 Kn'
        >>> nibbles_strategy.calculate(1024)
        '2.05 Kn'
        >>> nibbles_strategy.calculate(0)
        '0.00 n'
        >>> nibbles_strategy.calculate(1)
        '2.00 n'
        >>> nibbles_strategy.calculate(999)
        '1.99 Kn'
    """

    def calculate(self, size: int) -> str:
        """
        Calculate the data size in nibbles notation.

        This method takes a size in bytes and returns a string representing the size in nibbles notation.
        The size is converted to nibbles, then to the appropriate unit (n, Kn, Mn, Gn, etc.) based on its magnitude,
        and the result is formatted as a number with 2 decimal places followed by the appropriate suffix.

        Args:
            size (int): The size in bytes.

        Returns:
            str: A string representing the size in nibbles notation.
        """
        # List of suffixes for nibbles notation
        suffixes = ['n', 'Kn', 'Mn', 'Gn', 'Tn', 'Pn', 'En', 'Zn', 'Yn']

        # Convert size to nibbles
        size_nibbles = size * 2

        # Calculate the index of the suffix to use
        index = floor(log2(size_nibbles) / 10) if size_nibbles != 0 else 0

        # Convert the size to the appropriate unit and format the result
        return f'{size_nibbles / (1000.0 ** index):.2f} {suffixes[index]}'


def get_strategy(notation: str) -> NotationStrategy:
    """
    Factory function to get the appropriate notation strategy.

    This function takes a notation as input and returns an instance of the appropriate NotationStrategy subclass based on the notation. If the notation is not recognized, it raises a ValueError.

    Args:
        notation (str): The notation to use for the size calculation. It can be 'decimal', 'binary', 'bits', or 'nibbles'.

    Returns:
        NotationStrategy: An instance of the appropriate NotationStrategy subclass.

    Raises:
        ValueError: If the notation is not recognized.

    Doctest:
        >>> strategy = get_strategy('decimal')
        >>> isinstance(strategy, DecimalNotationStrategy)
        True
        >>> strategy = get_strategy('binary')
        >>> isinstance(strategy, BinaryNotationStrategy)
        True
        >>> strategy = get_strategy('bits')
        >>> isinstance(strategy, BitsNotationStrategy)
        True
        >>> strategy = get_strategy('nibbles')
        >>> isinstance(strategy, NibblesNotationStrategy)
        True
        >>> get_strategy('invalid')
        Traceback (most recent call last):
        ...
        ValueError: Invalid notation: invalid
    """
    # Check the notation and return the appropriate strategy
    if notation == 'decimal':
        return DecimalNotationStrategy()
    elif notation == 'binary':
        return BinaryNotationStrategy()
    elif notation == 'bits':
        return BitsNotationStrategy()
    elif notation == 'nibbles':
        return NibblesNotationStrategy()
    else:
        # Raise an error if the notation is not recognized
        raise ValueError(f"Invalid notation: {notation}")


def calculate_data_size(size: int, notation: str = 'decimal') -> str:
    """
    Calculate the data size in the specified notation using a factory pattern approach.

    This function takes a size in bytes and a notation as input, and returns a string representing the size in the specified notation. It uses a strategy pattern to select the appropriate calculation method based on the notation. If the size is negative, it raises a ValueError.

    Args:
        size (int): The size in bytes.
        notation (str): The notation to use for the size calculation. It can be 'decimal', 'binary', 'bits', or 'nibbles'. Defaults to 'decimal'.

    Returns:
        str: A string representing the size in the specified notation.

    Raises:
        ValueError: If the size is negative.

    Doctest:
        >>> calculate_data_size(1500, 'decimal')
        '1.50 KB'
        >>> calculate_data_size(1500, 'binary')
        '1.46 KiB'
        >>> calculate_data_size(1500, 'bits')
        '12.00 Kb'
        >>> calculate_data_size(1500, 'nibbles')
        '3.00 Kn'
        >>> calculate_data_size(-1, 'decimal')
        Traceback (most recent call last):
        ...
        ValueError: Size must be non-negative
    """
    # Check if the size is negative
    if size < 0:
        # Raise an error if the size is negative
        raise ValueError("Size must be non-negative")

    # Get the appropriate notation strategy
    strategy = get_strategy(notation)

    # Calculate and return the size in the specified notation
    return strategy.calculate(size)
