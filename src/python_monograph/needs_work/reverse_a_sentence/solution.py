#!/usr/bin/env python3
"""Python Monograph: Reverse a Sentence Solutions

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
import re
from functools import reduce


def method_0(sentence: str) -> str:
    """Reverse the entire sentence using reversed().

    This function takes a string as input and returns a new string that is the reverse of the input string.
    The function uses the built-in reversed function and join method to reverse the string.
    The original string is not modified.

    Args:
        sentence: The string that should be reversed.

    Returns:
        A new string that is the reverse of the input string.
    """
    return ''.join(reversed(sentence))


def method_1(sentence: str) -> str:
    """Reverse the letters of each word in a sentence, preserving word order, and using regex.sub().

    This function takes a string as input and returns a new string where the letters of each word are reversed, but the order of
    the words in the sentence is preserved.
    The function uses regular expressions to identify words and a lambda function to reverse the letters of each word.
    The original string is not modified.

    Args:
        sentence: The string that should be processed.

    Returns:
        A new string where the letters of each word are reversed, but the order of the words in the sentence is preserved.
    """
    return re.sub(r'(\w+)', lambda x: x.group()[::-1], sentence)


def method_2(sentence: str) -> str:
    """Reverse the entire sentence using slicing.

    This function takes a string as input and returns a new string that is the reverse of the input string.
    The function uses slicing with a step of -1 to reverse the string.
    The original string is not modified.

    Args:
        sentence: The string that should be reversed.

    Returns:
        A new string that is the reverse of the input string.
    """
    return sentence[slice(None, None, -1)]


def method_3(sentence: str) -> str:
    """Reverse the entire sentence using shorthand slice.

    This function takes a string as input and returns a new string that is the reverse of the input string.
    The function uses shorthand slicing with a step of -1 to reverse the string.
    The original string is not modified.

    Args:
        sentence: The string that should be reversed.

    Returns:
        A new string that is the reverse of the input string.
    """
    return sentence[::-1]


def method_4(sentence: str) -> str:
    """Reverse the order of words in a sentence using list comprehension.

    This function takes a string as input and returns a new string where the order of words in the sentence is reversed.
    The function uses list comprehension to create a list of words from the input string, and then reverses the order of words.
    The function also removes duplicate words from the sentence, keeping only the first occurrence of each word.
    The original string is not modified.

    Args:
        sentence: The string that should be processed.

    Returns:
        A new string where the order of words in the sentence is reversed.
    """
    s = sentence.split()
    l = []
    for i in s:
        l.append(i)

    res = [ii for n, ii in enumerate(l) if ii not in l[:n]]
    return ' '.join(res[::-1])


def method_5(sentence: str) -> str:
    """Reverse the order of words in a sentence using split and join.

    This function takes a string as input and returns a new string where the order of words in the sentence is reversed.
    The function uses the split method to create a list of words from the input string, and then reverses the order of words
    using slicing.
    The reversed list of words is then joined back into a string using the join method.
    The original string is not modified.

    Args:
        sentence: The string that should be processed.

    Returns:
        A new string where the order of words in the sentence is reversed.
    """
    words = sentence.split()
    reversed_words = words[::-1]
    reversed_sentence = ' '.join(reversed_words)
    return reversed_sentence


def method_6(sentence: str) -> str:
    """Reverse the order of words in a sentence using list comprehension.

    This function takes a string as input and returns a new string where the order of words in the sentence is reversed.
    The function uses list comprehension to create a list of words from the input string, and then reverses the order of words
    using slicing.
    The reversed list of words is then joined back into a string using the join method.
    The original string is not modified.

    Args:
        sentence: The string that should be processed.

    Returns:
        A new string where the order of words in the sentence is reversed.
    """
    return ' '.join(word for word in sentence.split()[::-1])


def method_7(sentence: str) -> str:
    """Reverse the order of words in a sentence using reduce.

    This function takes a string as input and returns a new string where the order of words in the sentence is reversed.
    The function uses the reduce function from the functools module to reverse the order of words.
    The original string is not modified.

    Args:
        sentence: The string that should be processed.

    Returns:
        A new string where the order of words in the sentence is reversed.
    """
    return reduce(lambda x, y: y + ' ' + x, sentence.split())


if __name__ == '__main__':
    print(__doc__)
