#!/usr/bin/env python3
"""Python Monograph: Fibonacci Sequence Solution 02

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
import numpy as np


def method_02(n) -> int:
    """This function calculates the nth number in the Fibonacci sequence using matrix exponentiation.

    This function uses the fact that the Fibonacci sequence can be expressed as a matrix that is raised to the power of `n`.

    Parameters:
        n (int): The position in the Fibonacci sequence to calculate. The first position is 0.

    Returns:
        int: The nth number in the Fibonacci sequence.

    Example:
    >>> method_02(6)
    8
    """
    if n < 0:
        raise ValueError('`n` must be a non-negative integer')

    if not isinstance(n, int):
        raise TypeError('`n` must be a non-negative integer')

    # Define the Fibonacci matrix
    F = np.matrix([[1, 1], [1, 0]], dtype='int64')

    # Return the nth Fibonacci number calculated using matrix exponentiation
    return (F ** n)[0, 1]


if __name__ == '__main__':
    print(__doc__)
