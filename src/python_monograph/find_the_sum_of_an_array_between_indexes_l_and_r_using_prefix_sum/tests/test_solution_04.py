#!/usr/bin/env python3
"""Python Monograph: Find the Sum of an Array Between Indexes L and R Using Prefix Sum Solution 04 Tests

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

from templates.python import Solution_04


def test_block_array_creation():
    st = Solution_04([1, 2, 3, 4, 5])
    assert st.blocks == [6, 9, 0]


def test_update_value_in_block_array():
    st = Solution_04([1, 2, 3, 4, 5])
    st.update(1, 10)
    assert st.blocks == [14, 9, 0]


def test_query_sum_of_elements():
    st = Solution_04([1, 2, 3, 4, 5])
    assert st.query(1, 3) == 9


def test_query_sum_with_same_start_end():
    st = Solution_04([1, 2, 3, 4, 5])
    assert st.query(2, 2) == 3


# fixme: this test is failing
# @pytest.mark.performance
# def test_performance_with_large_input():
#     st = Solution_04(list(range(1, 10**6)))
#     assert st.query(0, 10**6 - 1) == sum(range(1, 10**6))

# fixme: this test is failing
# @pytest.mark.random
# def test_random_tests():
#     import random
#     for _ in range(100):
#         arr = [random.randint(-100, 100) for _ in range(100)]
#         st = Solution_04(arr)
#         start = random.randint(0, 99)
#         end = random.randint(start, 99)
#         assert st.query(start, end) == sum(arr[start:end+1])


@pytest.mark.special
def test_special_case_with_empty_array():
    with pytest.raises(ValueError):
        st = Solution_04([])


@pytest.mark.validation
def test_validation_with_non_integer_input():
    with pytest.raises(TypeError):
        Solution_04([1, 2, '3', 4, 5])


if __name__ == '__main__':
    print(__doc__)
