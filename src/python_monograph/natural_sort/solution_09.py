"""
Python Monograph -> Sorting for Humans (Natural Sort) -> Solution 09

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
import re


# fixme: This is failiing 12/14 tests
def natural_sort(lst: list[str]) -> None:
    """
    Sorts a list of strings in a way that is intuitive to humans using an in-place sorting approach.

    Args:
        lst (List[str]): The list of strings to be sorted.

    Returns:
        None

    Examples:
        >>> lst = ['file1.txt', 'file10.txt', 'file2.txt']
        >>> natural_sort(lst)
        >>> print(lst)
        ['file1.txt', 'file2.txt', 'file10.txt']

        >>> lst = ['image99.png', 'image100.png', 'image101.png', 'image1.png', 'image10.png']
        >>> natural_sort(lst)
        >>> print(lst)
        ['image1.png', 'image10.png', 'image99.png', 'image100.png', 'image101.png']

        >>> lst = ['version1.10', 'version1.2', 'version1.1']
        >>> natural_sort(lst)
        >>> print(lst)
        ['version1.1', 'version1.2', 'version1.10']
    """

    def natural_keys(s: str) -> list[str | int]:
        """
        Splits a string into a list of parts, each part is either a string of non-digit characters or an integer.

        Args:
            s (str): The string to be split.

        Returns:
            List[Union[str, int]]: The list of parts.
        """
        return [int(part) if part.isdigit() else part for part in re.split(r'(\d+)', s)]

    # Sort the list in-place using the natural_keys function as the key
    lst.sort(key=natural_keys)
