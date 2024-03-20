"""
Python Monograph: Calculate Data Size Solution 07

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
    Abstract class that defines the interface for all concrete strategies.

    This class is used as a base for all strategies that calculate the data size in different notations.
    It defines a single method, `calculate`, that takes a size in bytes and returns a string representing the size in the appropriate notation.
    The specific implementation of the `calculate` method is provided by the concrete strategy classes.

    Methods:
        calculate (abstractmethod): Calculate the data size in the appropriate notation.

    Doctest:
        >>> class TestStrategy(NotationStrategy):
        ...     def calculate(self, size: int) -> str:
        ...         return f'{size} B'
        >>> test_strategy = TestStrategy()
        >>> test_strategy.calculate(1500)
        '1500 B'
        >>> test_strategy.calculate(1024)
        '1024 B'
        >>> test_strategy.calculate(0)
        '0 B'
        >>> test_strategy.calculate(1)
        '1 B'
        >>> test_strategy.calculate(999)
        '999 B'
    """

    @abstractmethod
    def calculate(self, size: int) -> str:
        """
        Abstract method to calculate the data size in the appropriate notation.

        This method takes a size in bytes and returns a string representing the size in the appropriate notation.
        The specific implementation of this method is provided by the concrete strategy classes.

        Args:
            size (int): The size in bytes.

        Returns:
            str: A string representing the size in the appropriate notation.

        Raises:
            NotImplementedError: This method is abstract and must be overridden by a concrete strategy class.
        """
        raise NotImplementedError("This method is abstract and must be overridden by a concrete strategy class.")


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
        The size is converted to bits by multiplying by 8, then converted to the appropriate unit (b, Kb, Mb, Gb, etc.) based on its magnitude,
        and the result is formatted as a number with 2 decimal places followed by the appropriate suffix.

        Args:
            size (int): The size in bytes.

        Returns:
            str: A string representing the size in bits notation.
        """
        # List of suffixes for bits notation
        suffixes = ['b', 'Kb', 'Mb', 'Gb', 'Tb', 'Pb', 'Eb', 'Zb', 'Yb']

        # Convert size to bits and calculate the index of the suffix to use
        size_bits = size * 8
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
        The size is converted to nibbles by multiplying by 2, then converted to the appropriate unit (n, Kn, Mn, Gn, etc.) based on its magnitude,
        and the result is formatted as a number with 2 decimal places followed by the appropriate suffix.

        Args:
            size (int): The size in bytes.

        Returns:
            str: A string representing the size in nibbles notation.
        """
        # List of suffixes for nibbles notation
        suffixes = ['n', 'Kn', 'Mn', 'Gn', 'Tn', 'Pn', 'En', 'Zn', 'Yn']

        # Convert size to nibbles and calculate the index of the suffix to use
        size_nibbles = size * 2
        index = floor(log2(size_nibbles) / 10) if size_nibbles != 0 else 0

        # Convert the size to the appropriate unit and format the result
        return f'{size_nibbles / (1000.0 ** index):.2f} {suffixes[index]}'


class DataSizeCalculator:
    """
    Context class that uses a strategy to calculate the data size.

    This class uses a strategy to calculate the data size in different notations.
    It provides an implementation of the `calculate` method that delegates the calculation to the strategy.

    Attributes:
        strategy (NotationStrategy): The strategy to use for the calculation.

    Methods:
        calculate: Calculate the data size using the strategy.

    Doctest:
        >>> decimal_strategy = DecimalNotationStrategy()
        >>> binary_strategy = BinaryNotationStrategy()
        >>> bits_strategy = BitsNotationStrategy()
        >>> nibbles_strategy = NibblesNotationStrategy()
        >>> calculator = DataSizeCalculator(decimal_strategy)
        >>> calculator.calculate(1500)
        '1.50 KB'
        >>> calculator.strategy = binary_strategy
        >>> calculator.calculate(1500)
        '1.46 KiB'
        >>> calculator.strategy = bits_strategy
        >>> calculator.calculate(1500)
        '12.00 Kb'
        >>> calculator.strategy = nibbles_strategy
        >>> calculator.calculate(1500)
        '3.00 Kn'
    """

    def __init__(self, strategy: NotationStrategy) -> None:
        """
        Initialize the DataSizeCalculator with a strategy.

        Args:
            strategy (NotationStrategy): The strategy to use for the calculation.
        """
        # Store the strategy
        self.strategy = strategy

    def calculate(self, size: int) -> str:
        """
        Calculate the data size using the strategy.

        This method delegates the calculation to the strategy.

        Args:
            size (int): The size in bytes.

        Returns:
            str: A string representing the size in the appropriate notation.
        """
        # Delegate the calculation to the strategy
        return self.strategy.calculate(size)
