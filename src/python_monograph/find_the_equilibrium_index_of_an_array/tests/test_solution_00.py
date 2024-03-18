"""
Python Monograph -> Find the Equilibrium Index of an Array -> Solution 00 -> Tests

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
import pytest

from python_monograph.find_the_equilibrium_index_of_an_array.solution_00 import equilibrium_index


def test_equilibrium_index_with_positive_case():
    assert equilibrium_index([-7, 1, 5, 2, -4, 3, 0]) == 3


def test_equilibrium_index_with_no_equilibrium_index():
    assert equilibrium_index([1, 2, 3, 4, 5, 6]) == -1


def test_equilibrium_index_with_symmetric_array():
    assert equilibrium_index([1, 2, 3, 4, 3, 2, 1]) == 3


def test_equilibrium_index_with_first_element_as_equilibrium_index():
    assert equilibrium_index([20, 10, -80, 10, 10, 15, 35]) == 0


def test_equilibrium_index_with_negative_numbers():
    assert equilibrium_index([0, -3, 5, -4, -2, 3, 1, 0]) == 0


def test_equilibrium_index_with_single_element():
    assert equilibrium_index([1]) == 0


def test_equilibrium_index_with_empty_array():
    assert equilibrium_index([]) == -1


@pytest.mark.benchmark
def test_equilibrium_index_with_large_input(benchmark):
    benchmark(equilibrium_index, ([1] * 10 ** 6))


def test_equilibrium_index_with_random_order():
    assert equilibrium_index([4, 2, -2, 5, 1, 1, -1, 3]) == 3


def test_equilibrium_index_with_special_case():
    assert equilibrium_index([0, 0, 0, 0, 0]) == 0


def test_equilibrium_index_with_invalid_input_type():
    with pytest.raises(TypeError):
        equilibrium_index("invalid input")


def test_equilibrium_index_with_invalid_input_value():
    with pytest.raises(ValueError):
        equilibrium_index([1, 2, "invalid", 4])


def test_equilibrium_index_with_duplicates():
    assert equilibrium_index([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5]) == 9


def test_equilibrium_index_with_no_duplicates():
    assert equilibrium_index([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 55]) == 9


def test_equilibrium_index_with_order_preservation():
    assert equilibrium_index([1, 2, 3, 4, 5, 6, 21]) == 5
