#!/usr/bin/env python3
"""Python Monograph: Fibonacci Sequence Solution 00

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


def method_00(n: int) -> int:
    """This function calculates the nth number in the Fibonacci sequence using dynamic programming.

    Parameters:
        n (int): The position in the Fibonacci sequence to calculate. The first position is 0.

    Returns:
        int: The nth number in the Fibonacci sequence.

    Example:
    >>> method_00(6)
    8
    """
    if n < 0:
        raise ValueError('`n` must be a non-negative integer')

    if not isinstance(n, int):
        raise TypeError('`n` must be a non-negative integer')

    fib = [0, 1] + [0] * (n - 1)

    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]

    return fib[n]


if __name__ == '__main__':
    print(__doc__)
