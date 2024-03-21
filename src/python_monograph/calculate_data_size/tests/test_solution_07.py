"""
Python Monograph -> Test Calculate Data Size -> Solution 07 -> Tests

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

from python_monograph.calculate_data_size.solution_07 import BinaryNotationStrategy, BitsNotationStrategy, DataSize, \
    DecimalNotationStrategy, NibblesNotationStrategy


def test_calculate_data_size_decimal():
    calculator = DataSize(DecimalNotationStrategy())
    assert calculator.calculate(1500) == '1.5 KB'


def test_calculate_data_size_binary():
    calculator = DataSize(BinaryNotationStrategy())
    assert calculator.calculate(1024) == '1 KiB'


def test_calculate_data_size_bits():
    calculator = DataSize(BitsNotationStrategy())
    assert calculator.calculate(1500) == '12 Kb'


def test_calculate_data_size_nibbles():
    calculator = DataSize(NibblesNotationStrategy())
    assert calculator.calculate(1500) == '3 Kn'


def test_calculate_data_size_large_size():
    calculator = DataSize(DecimalNotationStrategy())
    assert calculator.calculate(10 ** 18) == '1 EB'


def test_calculate_data_size_zero_size():
    calculator = DataSize(DecimalNotationStrategy())
    assert calculator.calculate(0) == '0 B'


def test_calculate_data_size_negative_size():
    calculator = DataSize(DecimalNotationStrategy())
    with pytest.raises(ValueError):
        calculator.calculate(-1)


def test_calculate_data_size_invalid_notation():
    with pytest.raises(ValueError):
        DataSize('invalid')


def test_calculate_data_size_random():
    calculator = DataSize(DecimalNotationStrategy())
    assert calculator.calculate(123456789) == '123.457 MB'


def test_calculate_data_size_special_case():
    calculator = DataSize(BinaryNotationStrategy())
    assert calculator.calculate(1024) == '1 KiB'


def test_calculate_data_size_validation():
    calculator = DataSize(DecimalNotationStrategy())
    with pytest.raises(ValueError):
        calculator.calculate(-1)


def test_calculate_data_size_regression():
    calculator = DataSize(DecimalNotationStrategy())
    assert calculator.calculate(1500) == '1.5 KB'


def test_calculate_data_size_equivalence_partitioning():
    calculator = DataSize(DecimalNotationStrategy())
    assert calculator.calculate(500) == '500 B'
    assert calculator.calculate(1500) == '1.5 KB'
    assert calculator.calculate(1500000) == '1.5 MB'


def test_calculate_data_size_security():
    calculator = DataSize(DecimalNotationStrategy())
    with pytest.raises(ValueError):
        calculator.calculate(-1)


def test_calculate_data_size_functional():
    calculator = DataSize(DecimalNotationStrategy())
    assert calculator.calculate(1500) == '1.5 KB'


def test_calculate_data_size_no_duplicates():
    calculator = DataSize(DecimalNotationStrategy())
    assert calculator.calculate(1500) == '1.5 KB'
    calculator = DataSize(DecimalNotationStrategy())
    assert calculator.calculate(1501) == '1.501 KB'


def test_calculate_data_size_order_preservation():
    calculator = DataSize(DecimalNotationStrategy())
    assert calculator.calculate(1500) == '1.5 KB'
    calculator = DataSize(DecimalNotationStrategy())
    assert calculator.calculate(1501) == '1.501 KB'
    calculator = DataSize(DecimalNotationStrategy())
    assert calculator.calculate(1502) == '1.502 KB'


@pytest.mark.benchmark
def test_calculate_data_size_performance(benchmark):
    calculator = DataSize(DecimalNotationStrategy())
    benchmark(calculator.calculate, 10 ** 18)
