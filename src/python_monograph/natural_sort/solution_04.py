"""
Python Monograph -> Sorting for Humans (Natural Sort) -> Solution 04

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


# fixme: This is failing 5 tests
def natural_sort(lst: list[str]) -> list[str]:
    """
    Sorts a list of strings in a way that is intuitive to humans.

    Args:
        lst (List[str]): The list of strings to be sorted.

    Returns:
        List[str]: The sorted list of strings.

    Examples:
        >>> natural_sort(['file1.txt', 'file10.txt', 'file2.txt'])
        ['file1.txt', 'file2.txt', 'file10.txt']

        >>> natural_sort(['image99.png', 'image100.png', 'image101.png', 'image1.png', 'image10.png'])
        ['image1.png', 'image10.png', 'image99.png', 'image100.png', 'image101.png']

        >>> natural_sort(['version1.10', 'version1.2', 'version1.1'])
        ['version1.1', 'version1.2', 'version1.10']
    """

    def natural_keys(s: str) -> [str | list[[str | int]]]:
        """
        Splits a string into a list of parts, each part is either a string of non-digit characters or an integer.

        Args:
            s (str): The string to be split.

        Returns:
            Union[str, List[Union[str, int]]]: The tuple containing the string and the list of parts.
        """
        return s, [int(part) if part.isdigit() else part for part in re.split(r'(\d+)', s)]

    # Sort the list twice using the natural_keys function as the key function
    return sorted(sorted(lst), key=natural_keys)
