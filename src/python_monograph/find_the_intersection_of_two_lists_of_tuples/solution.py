#!/usr/bin/env python3
"""Python Monograph: Find the Intersection of Two Lists of Tuples Solution

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


def method_0(ls0: list, ls1: list) -> set:
    """Find the intersection of two lists using list comprehension and set().

    This function takes two lists of tuples as input and returns a set of tuples that are present in both lists.
    The tuples are sorted before comparison to ensure that the order of elements does not affect the result.

    Args:
        ls0: The first list of tuples.
        ls1: The second list of tuples.

    Returns:
        A set of tuples that are present in both input lists.
    """
    return set([tuple(sorted(x)) for x in ls0]) & set([tuple(sorted(y)) for y in ls1])


def method_1(ls0: list, ls1: list) -> set:
    """Find the intersection of two lists using map() and frozenset().

    This function takes two lists of tuples as input and returns a set of tuples that are present in both lists.
    The tuples are converted to frozensets before comparison to ensure that the order of elements does not affect the result.

    Args:
        ls0: The first list of tuples.
        ls1: The second list of tuples.

    Returns:
        A set of tuples that are present in both input lists.
    """
    return set(map(frozenset, ls0)) & set(map(frozenset, ls1))


def method_2(ls0: list, ls1: list) -> list:
    """Find the intersection of two lists using list comprehension.

    This function takes two lists as input and returns a list of elements that are present in both lists.
    The order of elements in the input lists does not affect the result.

    Args:
        ls0: The first list.
        ls1: The second list.

    Returns:
        A list of elements that are present in both input lists.
    """
    return [x for x in ls0 for y in ls1 if x == y]


def method_3(ls0: list, ls1: list) -> list:
    """Find the intersection of two lists using set() and intersection().

    This function takes two lists as input and returns a list of elements that are present in both lists.
    The order of elements in the input lists does not affect the result.

    Args:
        ls0: The first list.
        ls1: The second list.

    Returns:
        A list of elements that are present in both input lists.
    """
    return list(set(ls0).intersection(set(ls1)))


def method_4(ls0: list, ls1: list) -> list:
    """Find the intersection of two lists using list comprehension.

    This function takes two lists as input and returns a list of elements that are present in both lists.
    The order of elements in the input lists does not affect the result.

    Args:
        ls0: The first list.
        ls1: The second list.

    Returns:
        A list of elements that are present in both input lists.
    """
    return [x for x in ls0 if x in ls1]


def method_5(ls0: list, ls1: list) -> list:
    """Find the intersection of two lists using filter() and lambda.

    This function takes two lists as input and returns a list of elements that are present in both lists.
    The order of elements in the input lists does not affect the result.

    Args:
        ls0: The first list.
        ls1: The second list.

    Returns:
        A list of elements that are present in both input lists.
    """
    return list(filter(lambda x: x in ls1, ls0))


def method_6(ls0: list, ls1: list) -> list:
    """Find the intersection of two lists using set comprehension and intersection().

    This function takes two lists as input and returns a list of elements that are present in both lists.
    The order of elements in the input lists does not affect the result.

    Args:
        ls0: The first list.
        ls1: The second list.

    Returns:
        A list of elements that are present in both input lists.
    """
    return list({x for x in ls0}.intersection(ls1))


if __name__ == '__main__':
    print(__doc__)
