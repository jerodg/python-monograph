"""
Python Monograph -> Test Calculate Data Size -> Solution 04 -> Tests

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

from python_monograph.calculate_data_size.solution_04 import DataSize


def test_calculate_data_size_decimal():
    ds = DataSize(1500, 'decimal')
    assert ds.calculate_data_size() == '1.5 KB'


def test_calculate_data_size_binary():
    ds = DataSize(1024, 'binary')
    assert ds.calculate_data_size() == '1 KiB'


def test_calculate_data_size_bits():
    ds = DataSize(1500, 'bits')
    assert ds.calculate_data_size() == '12 Kb'


def test_calculate_data_size_nibbles():
    ds = DataSize(1500, 'nibbles')
    assert ds.calculate_data_size() == '3 Kn'


def test_calculate_data_size_large_size():
    ds = DataSize(10 ** 18, 'decimal')
    assert ds.calculate_data_size() == '1 EB'


def test_calculate_data_size_zero_size():
    ds = DataSize(0, 'decimal')
    assert ds.calculate_data_size() == '0 B'


def test_calculate_data_size_negative_size():
    with pytest.raises(ValueError):
        ds = DataSize(-1, 'decimal')


def test_calculate_data_size_invalid_notation():
    with pytest.raises(ValueError):
        ds = DataSize(1500, 'invalid')


def test_calculate_data_size_random():
    ds = DataSize(123456789, 'decimal')
    assert ds.calculate_data_size() == '123.457 MB'


def test_calculate_data_size_special_case():
    ds = DataSize(1024, 'binary')
    assert ds.calculate_data_size() == '1 KiB'


def test_calculate_data_size_validation():
    with pytest.raises(ValueError):
        ds = DataSize(-1, 'decimal')


def test_calculate_data_size_regression():
    ds = DataSize(1500, 'decimal')
    assert ds.calculate_data_size() == '1.5 KB'


def test_calculate_data_size_equivalence_partitioning():
    ds = DataSize(500, 'decimal')
    assert ds.calculate_data_size() == '500 B'
    ds = DataSize(1500, 'decimal')
    assert ds.calculate_data_size() == '1.5 KB'
    ds = DataSize(1500000, 'decimal')
    assert ds.calculate_data_size() == '1.5 MB'


def test_calculate_data_size_security():
    with pytest.raises(ValueError):
        ds = DataSize(-1, 'decimal')


def test_calculate_data_size_functional():
    ds = DataSize(1500, 'decimal')
    assert ds.calculate_data_size() == '1.5 KB'


def test_calculate_data_size_no_duplicates():
    ds = DataSize(1500, 'decimal')
    assert ds.calculate_data_size() == '1.5 KB'
    ds = DataSize(1501, 'decimal')
    assert ds.calculate_data_size() == '1.501 KB'


def test_calculate_data_size_order_preservation():
    ds = DataSize(1500, 'decimal')
    assert ds.calculate_data_size() == '1.5 KB'
    ds = DataSize(1501, 'decimal')
    assert ds.calculate_data_size() == '1.501 KB'
    ds = DataSize(1502, 'decimal')
    assert ds.calculate_data_size() == '1.502 KB'


@pytest.mark.benchmark
def test_calculate_data_size_performance(benchmark):
    ds = DataSize(10 ** 18, 'decimal')
    benchmark(ds.calculate_data_size)
