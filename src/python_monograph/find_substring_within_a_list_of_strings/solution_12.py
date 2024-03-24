"""
Python Monograph -> Find a Substring Within a List -> Solution 12

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
def compute_bad_char_table(pattern: str) -> dict:
    bad_char_table = {}
    for i in range(len(pattern)):
        bad_char_table[pattern[i]] = i
    return bad_char_table

def find_substring(strings: list, pattern: str) -> [int | None]:
    bad_char_table = compute_bad_char_table(pattern)

    for index, string in enumerate(strings):
        s = p = len(pattern) - 1
        while s < len(string):
            if string[s] == pattern[p]:
                if p == 0:
                    return index
                else:
                    s -= 1
                    p -= 1
            else:
                s += len(pattern) - min(p, 1 + bad_char_table.get(string[s], -1))
                p = len(pattern) - 1
    return None
