"""
Python Monograph -> Find a Substring Within a List -> Solution 20

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
def compute_hash(s: str, modulus: int, base: int) -> int:
    return sum((ord(s[i]) - ord('a') + 1) * pow(base, len(s) - i - 1) for i in range(len(s))) % modulus

def find_substring(strings: list, pattern: str) -> [int | None]:
    modulus = 10**9 + 7  # Large prime number
    base = 26  # Number of characters in the alphabet
    pattern_hash = compute_hash(pattern, modulus, base)

    for index, string in enumerate(strings):
        string_hash = compute_hash(string[:len(pattern)], modulus, base)
        if string_hash == pattern_hash and string[:len(pattern)] == pattern:
            return index
        for i in range(len(pattern), len(string)):
            string_hash = ((string_hash - (ord(string[i - len(pattern)]) - ord('a') + 1) * pow(base, len(pattern) - 1)) * base + (ord(string[i]) - ord('a') + 1)) % modulus
            if string_hash == pattern_hash and string[i - len(pattern) + 1:i + 1] == pattern:
                return index
    return None
