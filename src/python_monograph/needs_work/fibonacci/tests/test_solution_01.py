#!/usr/bin/env python3
"""Python Monograph: Test Fibonacci Sequence Solution 01

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
import pytest

from check_if_a_substring_is_in_a_list_strings.solution_01 import solution_01


def test_solution_01_with_zero():
    assert solution_01(0) == 0


def test_solution_01_with_one():
    assert solution_01(1) == 1


def test_solution_01_with_small_number():
    assert solution_01(6) == 8


def test_solution_01_with_large_number():
    assert solution_01(30) == 832040


def test_solution_01_with_negative_number():
    with pytest.raises(ValueError):
        solution_01(-1)


def test_solution_01_with_non_integer():
    with pytest.raises(TypeError):
        solution_01(2.5)


if __name__ == '__main__':
    print(__doc__)
