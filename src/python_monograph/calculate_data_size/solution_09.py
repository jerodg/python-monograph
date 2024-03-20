"""
Python Monograph: Calculate Data Size Solution 09

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
from math import floor, log10, log2


class Command(ABC):
    """
    The Command interface declares a method for executing a command.

    This class is an abstract base class (ABC) that defines a common interface for all commands. It declares an abstract method `execute` that all concrete command classes must implement.

    Methods:
        execute: Execute the command.

    Doctest:
        >>> from abc import ABCMeta
        >>> isinstance(Command, ABCMeta)
        True
        >>> Command.__abstractmethods__
        frozenset({'execute'})
    """

    @abstractmethod
    def execute(self, size: int) -> str:
        """
        Execute the command.

        This is an abstract method that must be implemented by all concrete command classes. It takes a size in bytes and returns a string representing the size in the appropriate notation.

        Args:
            size (int): The size in bytes.

        Returns:
            str: A string representing the size in the appropriate notation.

        Raises:
            NotImplementedError: If this method is called on the Command class itself, rather than on an instance of a subclass.
        """
        raise NotImplementedError("Subclasses must implement this method.")


class DecimalCommand(Command):
    """
    The DecimalCommand class for calculating data size in decimal notation.

    This class is a concrete command class that implements the `execute` method of the Command interface. It calculates the data size in decimal notation.

    Methods:
        execute: Calculate the data size in decimal notation.

    Doctest:
        >>> decimal_command = DecimalCommand()
        >>> decimal_command.execute(1500)
        '1.50 KB'
        >>> decimal_command.execute(1024)
        '1.02 KB'
        >>> decimal_command.execute(1048576)
        '1.05 MB'
        >>> decimal_command.execute(1073741824)
        '1.07 GB'
        >>> decimal_command.execute(0)
        '0.00 B'
    """

    def execute(self, size: int) -> str:
        """
        Calculate the data size in decimal notation.

        This method takes a size in bytes and returns a string representing the size in decimal notation. It uses a list of suffixes and the base-10 logarithm of the size to calculate the index of the appropriate suffix. The size is then divided by 1000 to the power of the index to convert it to the appropriate unit, and the result is formatted as a number with 2 decimal places, followed by the suffix.

        Args:
            size (int): The size in bytes.

        Returns:
            str: A string representing the size in decimal notation.

        Doctest:
            >>> decimal_command = DecimalCommand()
            >>> decimal_command.execute(1500)
            '1.50 KB'
            >>> decimal_command.execute(1024)
            '1.02 KB'
            >>> decimal_command.execute(1048576)
            '1.05 MB'
            >>> decimal_command.execute(1073741824)
            '1.07 GB'
            >>> decimal_command.execute(0)
            '0.00 B'
        """
        # Define the suffixes for decimal notation
        suffixes = ['B', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB']
        # Calculate the index of the appropriate suffix
        index = floor(log10(size) / 3) if size != 0 else 0
        # Calculate the size in the appropriate unit and format the result
        return f'{size / (1000.0 ** index):.2f} {suffixes[index]}'


class BinaryCommand(Command):
    """
    The BinaryCommand class for calculating data size in binary notation.

    This class is a concrete command class that implements the `execute` method of the Command interface. It calculates the data size in binary notation.

    Methods:
        execute: Calculate the data size in binary notation.

    Doctest:
        >>> binary_command = BinaryCommand()
        >>> binary_command.execute(1500)
        '1.46 KiB'
        >>> binary_command.execute(1024)
        '1.00 KiB'
        >>> binary_command.execute(1048576)
        '1.00 MiB'
        >>> binary_command.execute(1073741824)
        '1.00 GiB'
        >>> binary_command.execute(0)
        '0.00 B'
    """

    def execute(self, size: int) -> str:
        """
        Calculate the data size in binary notation.

        This method takes a size in bytes and returns a string representing the size in binary notation. It uses a list of suffixes and the base-2 logarithm of the size to calculate the index of the appropriate suffix. The size is then divided by 1024 to the power of the index to convert it to the appropriate unit, and the result is formatted as a number with 2 decimal places, followed by the suffix.

        Args:
            size (int): The size in bytes.

        Returns:
            str: A string representing the size in binary notation.

        Doctest:
            >>> binary_command = BinaryCommand()
            >>> binary_command.execute(1500)
            '1.46 KiB'
            >>> binary_command.execute(1024)
            '1.00 KiB'
            >>> binary_command.execute(1048576)
            '1.00 MiB'
            >>> binary_command.execute(1073741824)
            '1.00 GiB'
            >>> binary_command.execute(0)
            '0.00 B'
        """
        # Define the suffixes for binary notation
        suffixes = ['B', 'KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']
        # Calculate the index of the appropriate suffix
        index = floor(log2(size) / 10) if size != 0 else 0
        # Calculate the size in the appropriate unit and format the result
        return f'{size / (1024.0 ** index):.2f} {suffixes[index]}'


class BitsCommand(Command):
    """
    The BitsCommand class for calculating data size in bits notation.

    This class is a concrete command class that implements the `execute` method of the Command interface. It calculates the data size in bits notation.

    Methods:
        execute: Calculate the data size in bits notation.

    Doctest:
        >>> bits_command = BitsCommand()
        >>> bits_command.execute(1500)
        '12.00 Kb'
        >>> bits_command.execute(1024)
        '8.19 Kb'
        >>> bits_command.execute(1048576)
        '8.39 Mb'
        >>> bits_command.execute(1073741824)
        '8.59 Gb'
        >>> bits_command.execute(0)
        '0.00 b'
    """

    def execute(self, size: int) -> str:
        """
        Calculate the data size in bits notation.

        This method takes a size in bytes and returns a string representing the size in bits notation. It first converts the size from bytes to bits by multiplying by 8. It then uses a list of suffixes and the base-2 logarithm of the size in bits to calculate the index of the appropriate suffix. The size in bits is then divided by 1000 to the power of the index to convert it to the appropriate unit, and the result is formatted as a number with 2 decimal places, followed by the suffix.

        Args:
            size (int): The size in bytes.

        Returns:
            str: A string representing the size in bits notation.

        Doctest:
            >>> bits_command = BitsCommand()
            >>> bits_command.execute(1500)
            '12.00 Kb'
            >>> bits_command.execute(1024)
            '8.19 Kb'
            >>> bits_command.execute(1048576)
            '8.39 Mb'
            >>> bits_command.execute(1073741824)
            '8.59 Gb'
            >>> bits_command.execute(0)
            '0.00 b'
        """
        # Define the suffixes for bits notation
        suffixes = ['b', 'Kb', 'Mb', 'Gb', 'Tb', 'Pb', 'Eb', 'Zb', 'Yb']
        # Convert the size from bytes to bits
        size_bits = size * 8
        # Calculate the index of the appropriate suffix
        index = floor(log2(size_bits) / 10) if size_bits != 0 else 0
        # Calculate the size in the appropriate unit and format the result
        return f'{size_bits / (1000.0 ** index):.2f} {suffixes[index]}'


class NibblesCommand(Command):
    """
    The NibblesCommand class for calculating data size in nibbles notation.

    This class is a concrete command class that implements the `execute` method of the Command interface. It calculates the data size in nibbles notation.

    Methods:
        execute: Calculate the data size in nibbles notation.

    Doctest:
        >>> nibbles_command = NibblesCommand()
        >>> nibbles_command.execute(1500)
        '3.00 Kn'
        >>> nibbles_command.execute(1024)
        '2.05 Kn'
        >>> nibbles_command.execute(1048576)
        '2.10 Mn'
        >>> nibbles_command.execute(1073741824)
        '2.15 Gn'
        >>> nibbles_command.execute(0)
        '0.00 n'
    """

    def execute(self, size: int) -> str:
        """
        Calculate the data size in nibbles notation.

        This method takes a size in bytes and returns a string representing the size in nibbles notation. It first converts the size from bytes to nibbles by multiplying by 2. It then uses a list of suffixes and the base-2 logarithm of the size in nibbles to calculate the index of the appropriate suffix. The size in nibbles is then divided by 1000 to the power of the index to convert it to the appropriate unit, and the result is formatted as a number with 2 decimal places, followed by the suffix.

        Args:
            size (int): The size in bytes.

        Returns:
            str: A string representing the size in nibbles notation.

        Doctest:
            >>> nibbles_command = NibblesCommand()
            >>> nibbles_command.execute(1500)
            '3.00 Kn'
            >>> nibbles_command.execute(1024)
            '2.05 Kn'
            >>> nibbles_command.execute(1048576)
            '2.10 Mn'
            >>> nibbles_command.execute(1073741824)
            '2.15 Gn'
            >>> nibbles_command.execute(0)
            '0.00 n'
        """
        # Define the suffixes for nibbles notation
        suffixes = ['n', 'Kn', 'Mn', 'Gn', 'Tn', 'Pn', 'En', 'Zn', 'Yn']
        # Convert the size from bytes to nibbles
        size_nibbles = size * 2
        # Calculate the index of the appropriate suffix
        index = floor(log2(size_nibbles) / 10) if size_nibbles != 0 else 0
        # Calculate the size in the appropriate unit and format the result
        return f'{size_nibbles / (1000.0 ** index):.2f} {suffixes[index]}'


def calculate_data_size(size: int, notation: str = 'decimal') -> str:
    """
    Calculate the data size in the specified notation using a command pattern approach.

    This function takes a size in bytes and a notation as input, and returns a string representing the size in the specified notation. It uses a command pattern to select the appropriate calculation method based on the notation. If the size is negative, it raises a ValueError.

    Args:
        size (int): The size in bytes.
        notation (str): The notation to use for the size calculation. It can be 'decimal', 'binary', 'bits', or 'nibbles'. Defaults to 'decimal'.

    Returns:
        str: A string representing the size in the specified notation.

    Raises:
        ValueError: If the size is negative or the notation is invalid.

    Doctest:
        >>> calculate_data_size(1500, 'decimal')
        '1.50 KB'
        >>> calculate_data_size(1500, 'binary')
        '1.46 KiB'
        >>> calculate_data_size(1500, 'bits')
        '12.00 Kb'
        >>> calculate_data_size(1500, 'nibbles')
        '3.00 Kn'
        >>> calculate_data_size(1024, 'binary')
        '1.00 KiB'
    """
    # Raise an error if the size is negative
    if size < 0:
        raise ValueError("Size must be non-negative")

    # Define the commands for each notation
    commands = {
        'decimal': DecimalCommand(),
        'binary':  BinaryCommand(),
        'bits':    BitsCommand(),
        'nibbles': NibblesCommand()
    }

    # Get the command for the specified notation
    command = commands.get(notation)
    # Raise an error if the notation is invalid
    if command is None:
        raise ValueError(f"Invalid notation: {notation}")

    # Execute the command and return the result
    return command.execute(size)
