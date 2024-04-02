"""
Python Monograph -> Sorting for Humans (Natural Sort) -> Solution 07

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


def natural_sort(lst: list[str]) -> list[str]:
    """
    Sorts a list of strings in a way that is intuitive to humans using a bucket sort approach.

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

    Notes:
        This solution cannot handle a list of strings that are all the same.
    """

    def natural_keys(s: str) -> list[str | int]:
        """
        Splits a string into a list of parts, each part is either a string of non-digit characters or an integer.

        Args:
            s (str): The string to be split.

        Returns:
            List[Union[str, int]]: The list of parts.
        """
        # Using regular expression to split the string into parts
        return [int(part) if part.isdigit() else part for part in re.split(r'(\d+)', s)]

    # If the list contains one or no elements, return the list as it is
    if len(lst) <= 1:
        return lst

    # Create a list of empty lists (buckets) for each possible number
    # The range is determined by the maximum number found in the strings of the list
    buckets = [[] for _ in range(max([int(part) for s in lst for part in re.split(r'(\d+)', s) if part.isdigit()]) + 1)]

    # For each string, calculate its bucket index and append it to the corresponding bucket
    for s in lst:
        buckets[int(re.search(r'\d+', s).group())].append(s)

    # Sort each bucket and concatenate them to get the sorted list
    # The sorting within each bucket is done based on the natural order of the strings

    return [s for bucket in buckets for s in sorted(bucket, key=natural_keys)]
