#!/usr/bin/env python3
"""Python Monograph: Find Multiples of 3 and 5 Solutions

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


def method_0(n: int = 1000) -> int:
    """Method 0: Using a for loop to calculate and print the sum of all multiples of 3 or 5 below 1000.

    Returns:
        int
    """
    sum = 0
    for i in range(1, n):
        if i % 3 == 0 or i % 5 == 0:
            sum += i

    return sum


def method_1(n: int = 1000) -> int:
    """Method 1: Using a list comprehension to calculate and print the sum of all multiples of 3 or 5 below 1000.

    Returns:
        int
    """
    return sum(i for i in range(1, n) if i % 3 == 0 or i % 5 == 0)


# fixme: this method is returning the wrong value
def method_2(n: int = 1000) -> int:
    """Method 2: Using a mathematical approach recursively to calculate and print the sum of all multiples of 3 or 5 below 1000.

    Returns:
        int
    """

    def sum_divisible_by(i: int = 1000) -> int:
        p = n // i
        return i * (p * (p + 1)) // 2

    return sum_divisible_by(3) + sum_divisible_by(5) - sum_divisible_by(15)


def method_3(n: int = 1000) -> int:
    """Method 3: Using a mathematical approach to calculate and print the sum of all multiples of 3 or 5 below 1000.

    Returns:
        int
    """
    total = 0
    terms = (n - 1) // 3
    total += (terms * (6 + (terms - 1) * 3)) // 2  # total of an A.P.
    terms = (n - 1) // 5
    total += (terms * (10 + (terms - 1) * 5)) // 2
    terms = (n - 1) // 15
    total -= (terms * (30 + (terms - 1) * 15)) // 2
    return total


def method_4(n: int = 1000) -> int:
    """Method 4: Using a set with union operator to calculate and print the sum of all multiples of 3 or 5 below 1000.

    Returns:
        int
    """
    return sum(set(range(3, n, 3)) | set(range(5, n, 5)))


def method_5(n: int = 1000) -> int:
    """Method 5: Using a set with .union() to calculate and print the sum of all multiples of 3 or 5 below 1000.

    Returns:
        int
    """
    return sum(set(range(3, n, 3)).union(set(range(5, n, 5))))


def method_6(n: int = 1000) -> int:
    """Method 6: Using a while loop to calculate and print the sum of all multiples of 3 or 5 below 1000.

    Returns:
        int
    """
    total = 0
    num = 0
    while 1:
        num += 3
        if num >= n:
            break
        total += num
        num += 2
        if num >= n:
            break
        total += num
        num += 1
        if num >= n:
            break
        total += num
        num += 3
        if num >= n:
            break
        total += num
        num += 1
        if num >= n:
            break
        total += num
        num += 2
        if num >= n:
            break
        total += num
        num += 3
        if num >= n:
            break
        total += num

    return total


def method_7(n: int = 1000) -> int:
    """Method 7: Using a mathematical approach with multiple loops to calculate and print the sum of all multiples of 3 or 5 below
    1000.

    Returns:
        int
    """
    total = 0
    for i in range(3, n, 3):
        total += i

    for i in range(5, n, 5):
        if i % 3 != 0:
            total += i

    return total


def method_8(n: int = 1000) -> int:
    """Method 8: Using a mathematical approach with multiple loops to calculate and print the sum of all multiples of 3 or 5
    below 1000.

    Returns:
        int
    """
    total = 0
    for i in range(3, n, 3):
        total += i

    for i in range(5, n, 5):
        total += i

    return total


def method_9(n: int = 1000) -> int:
    """Method 9: Using a mathematical approach with multiple loops to calculate and print the sum of all multiples of 3 or 5
    below 1000.

    Returns:
        int
    """
    xmulti = []
    zmulti = []
    z = 3
    x = 5
    temp = 1
    while True:
        result = z * temp
        if result < n:
            zmulti.append(result)
            temp += 1
        else:
            temp = 1
            break

    while True:
        result = x * temp
        if result < n:
            xmulti.append(result)
            temp += 1
        else:
            break

    collection = list(set(xmulti + zmulti))

    return sum(collection)


def method_10(n: int = 1000) -> int:
    """Method 10: Using a mathematical approach with a while loop to calculate and print the sum of all multiples of 3 or 5 below
    1000.

    Returns:
        int
    """
    a = 3
    result = 0
    while a < n:
        if a % 3 == 0 or a % 5 == 0:
            result += a
        elif a % 15 == 0:
            result -= a
        a += 1

    return result


if __name__ == '__main__':
    print(__doc__)
