"""
Python Monograph -> Test Calculate Data Size -> Solution 08 -> Tests

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

from python_monograph.calculate_data_size.solution_08 import calculate_data_size


def test_calculate_data_size_decimal():
    assert calculate_data_size(1500, 'decimal') == '1.5 KB'


def test_calculate_data_size_binary():
    assert calculate_data_size(1024, 'binary') == '1 KiB'


def test_calculate_data_size_bits():
    assert calculate_data_size(1500, 'bits') == '12 Kb'


def test_calculate_data_size_nibbles():
    assert calculate_data_size(1500, 'nibbles') == '3 Kn'


def test_calculate_data_size_large_size():
    assert calculate_data_size(10 ** 18, 'decimal') == '1 EB'


def test_calculate_data_size_zero_size():
    assert calculate_data_size(0, 'decimal') == '0 B'


def test_calculate_data_size_negative_size():
    with pytest.raises(ValueError):
        calculate_data_size(-1, 'decimal')


def test_calculate_data_size_invalid_notation():
    with pytest.raises(ValueError):
        calculate_data_size(1500, 'invalid')


def test_calculate_data_size_random():
    assert calculate_data_size(123456789, 'decimal') == '123.457 MB'


def test_calculate_data_size_special_case():
    assert calculate_data_size(1024, 'binary') == '1 KiB'


def test_calculate_data_size_validation():
    with pytest.raises(ValueError):
        calculate_data_size(-1, 'decimal')


def test_calculate_data_size_regression():
    assert calculate_data_size(1500, 'decimal') == '1.5 KB'


def test_calculate_data_size_equivalence_partitioning():
    assert calculate_data_size(500, 'decimal') == '500 B'
    assert calculate_data_size(1500, 'decimal') == '1.5 KB'
    assert calculate_data_size(1500000, 'decimal') == '1.5 MB'


def test_calculate_data_size_security():
    with pytest.raises(ValueError):
        calculate_data_size(-1, 'decimal')


def test_calculate_data_size_functional():
    assert calculate_data_size(1500, 'decimal') == '1.5 KB'


def test_calculate_data_size_no_duplicates():
    assert calculate_data_size(1500, 'decimal') == '1.5 KB'
    assert calculate_data_size(1501, 'decimal') == '1.501 KB'


def test_calculate_data_size_order_preservation():
    assert calculate_data_size(1500, 'decimal') == '1.5 KB'
    assert calculate_data_size(1501, 'decimal') == '1.501 KB'
    assert calculate_data_size(1502, 'decimal') == '1.502 KB'


@pytest.mark.benchmark
def test_calculate_data_size_performance(benchmark):
    benchmark(calculate_data_size, 10 ** 18, 'decimal')
