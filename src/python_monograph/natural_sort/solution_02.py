"""
Python Monograph -> Sorting for Humans (Natural Sort) -> Solution 02

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
from re import compile, split

# Compiles a regular expression pattern into a regular expression object.
# This object can be used for matching using its match(), search() and other methods.
# The pattern we are compiling is '(\d+)', which matches one or more digits.
DRE = compile(r'(\d+)')


def natural_sort(lst: list) -> list:
    """
    Sorts a list of strings in a way that is intuitive to humans (natural sort).
    This function sorts strings containing numbers based on the numerical value of the number, not its lexicographical order.
    This means that '10' comes after '2' when sorting a list of strings.

    Args:
        lst (list): The list of strings to be sorted.

    Returns:
        list: A new list with the strings sorted in natural order.

    Doctest:
        >>> natural_sort(['file1.txt', 'file10.txt', 'file2.txt'])
        ['file1.txt', 'file2.txt', 'file10.txt']
        >>> natural_sort(['file1.txt', 'file10.txt', 'file2.txt'], True)
        ['file10.txt', 'file2.txt', 'file1.txt']
    """
    # The sorted() function returns a new sorted list from the elements of any sequence.
    # The key argument is a function that takes one argument and returns a key to use for sorting purposes.
    # In this case, the key function splits each string into a list of substrings using the regular expression object DRE.
    # Each substring that contains digits is converted to an integer, and other substrings are converted to lowercase.
    return [natural_sort(x) if isinstance(x, list) else x for x in
            sorted(lst, key=lambda _: [int(s) if s.isdigit() else s.lower() for s in split(DRE, _)])]
