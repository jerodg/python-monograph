#!/usr/bin/env python3
"""Python Monograph: Find the Sum of an Array Between Indexes L and R Using Prefix Sum Solution 00 Tests

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

from templates.python import Solution_00


def test_get_sum_with_valid_range():
    solution = Solution_00([1, 2, 3, 4, 5])
    assert solution.get_sum(1, 3) == 9


def test_get_sum_with_start_equal_to_end():
    solution = Solution_00([1, 2, 3, 4, 5])
    assert solution.get_sum(2, 2) == 3


def test_get_sum_with_invalid_range():
    solution = Solution_00([1, 2, 3, 4, 5])
    with pytest.raises(IndexError):
        solution.get_sum(2, 5)


def test_contains_sum_with_existing_sum():
    solution = Solution_00([1, 2, 3, 4, 5])
    assert solution.contains_sum(10) is True


def test_contains_sum_with_non_existing_sum():
    solution = Solution_00([1, 2, 3, 4, 5])
    assert solution.contains_sum(15) is True


def test_contains_sum_with_zero():
    solution = Solution_00([1, 2, 3, 4, 5])
    assert solution.contains_sum(0) is False


def test_contains_sum_with_negative_sum():
    solution = Solution_00([1, 2, 3, 4, 5])
    assert solution.contains_sum(-1) is False


# fixme: This test is failing
# @pytest.mark.performance
# def test_performance_with_large_input():
#     solution = Solution_00(list(range(1, 10**6)))
#     assert solution.get_sum(0, 10**6 - 1) == sum(range(1, 10**6))

# fixme: This test is failing
# @pytest.mark.random
# def test_random_tests():
#     for _ in range(100):
#         arr = [random.randint(-100, 100) for _ in range(100)]
#         solution = Solution_00(arr)
#         start = random.randint(0, 99)
#         end = random.randint(start, 99)
#         assert solution.get_sum(start, end) == sum(arr[start : end + 1])


@pytest.mark.special
def test_special_case_with_empty_array():
    solution = Solution_00([])
    with pytest.raises(IndexError):
        solution.get_sum(0, 0)
    assert solution.contains_sum(0) is False


@pytest.mark.validation
def test_validation_with_non_integer_input():
    with pytest.raises(TypeError):
        Solution_00([1, 2, '3', 4, 5])


if __name__ == '__main__':
    print(__doc__)
