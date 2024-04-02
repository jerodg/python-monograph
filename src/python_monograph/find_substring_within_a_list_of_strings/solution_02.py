"""
Python Monograph -> Find a Substring Within a List -> Solution 02

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


# fixme: doctests are failing; this is returning a bool instead of the index of the first string in the list where the pattern is
#  found as a substring

class TrieNode:
    """
    A node in the Trie.

    Each TrieNode object represents a node in the Trie data structure. It has two attributes:
    - children: A dictionary that maps each character in the alphabet to the next TrieNode in the Trie that the character leads to.
    - end_of_string: A boolean value that is True if this node marks the end of a string in the Trie, and False otherwise.

    Attributes:
        children (dict): A dictionary mapping characters to TrieNode objects.
        end_of_string (bool): A flag indicating whether this node is the end of a string in the Trie.

    Doctest:
        >>> node = TrieNode()
        >>> node.children
        {}
        >>> node.end_of_string
        False
        >>> node.children['a'] = TrieNode()
        >>> node.children['a'].children
        {}
        >>> node.children['a'].end_of_string
        False
    """

    def __init__(self):
        self.children = {}  # Initialize the children dictionary
        self.end_of_string = False  # Initialize the end_of_string flag as False


class Trie:
    """
    A Trie data structure.

    A Trie is a tree-like data structure that stores strings in a way that allows for efficient substring searching.
    Each node in the Trie represents a character, and each path from the root to a node represents a string.

    Attributes:
        root (TrieNode): The root node of the Trie.

    Doctest:
        >>> trie = Trie()
        >>> trie.root.children
        {}
        >>> trie.root.end_of_string
        False
        >>> trie.insert("hello")
        >>> trie.root.children['h'].children['e'].children['l'].children['l'].children['o'].end_of_string
        True
        >>> trie.find_substring("hello")
        True
        >>> trie.find_substring("world")
        False
    """

    def __init__(self):
        self.root = TrieNode()  # Initialize the root node of the Trie

    def insert(self, word: str) -> None:
        """
        Insert a word into the Trie.

        This method takes a word as input and inserts it into the Trie. It starts from the root of the Trie and for each
        character in the word, it checks if the character is already a child of the current node. If not, it creates a new
        TrieNode and adds it as a child of the current node. It then moves to the child node and continues with the next
        character. Once all characters are processed, it marks the last node as the end of a string.

        Args:
            word (str): The word to be inserted into the Trie.

        Doctest:
            >>> trie = Trie()
            >>> trie.insert("hello")
            >>> trie.root.children['h'].children['e'].children['l'].children['l'].children['o'].end_of_string
            True
            >>> trie.insert("world")
            >>> trie.root.children['w'].children['o'].children['r'].children['l'].children['d'].end_of_string
            True
            >>> trie.insert("python")
            >>> trie.root.children['p'].children['y'].children['t'].children['h'].children['o'].children['n'].end_of_string
            True
            >>> trie.insert("programming")
            >>> trie.root.children['p'].children['r'].children['o'].children['g'].children['r'].children['a'].children[
            'm'].children['m'].children['i'].children['n'].children['g'].end_of_string
            True
            >>> trie.insert("")
            >>> trie.root.end_of_string
            True
        """
        node = self.root  # Start from the root of the Trie
        for char in word:  # For each character in the word
            if char not in node.children:  # If the character is not already a child of the current node
                node.children[char] = TrieNode()  # Create a new TrieNode and add it as a child of the current node

            node = node.children[char]  # Move to the child node

        node.end_of_string = True  # Mark the last node as the end of a string

    def search(self, word: str) -> bool:
        """
        Search for a word in the Trie.

        This method takes a word as input and searches for it in the Trie. It starts from the root of the Trie and for each
        character in the word, it checks if the character is a child of the current node. If not, it returns False as the
        word is not present in the Trie. If the character is a child of the current node, it moves to the child node and
        continues with the next character. If all characters are found in the Trie, it returns True.

        Args:
            word (str): The word to be searched in the Trie.

        Returns:
            bool: True if the word is found in the Trie, False otherwise.

        Doctest:
            >>> trie = Trie()
            >>> trie.insert("hello")
            >>> trie.find_substring("hello")
            True
            >>> trie.find_substring("world")
            False
            >>> trie.insert("world")
            >>> trie.find_substring("world")
            True
            >>> trie.find_substring("python")
            False
            >>> trie.find_substring("")
            False
        """
        node = self.root  # Start from the root of the Trie
        for char in word:  # For each character in the word
            if char not in node.children:  # If the character is not a child of the current node
                return False  # Return False as the word is not present in the Trie
            node = node.children[char]  # Move to the child node

        return node.end_of_string  # Return True if all characters are found in the Trie, False otherwise


def find_substring(strings: list, target: str) -> [int | None]:
    """
    Finds the first occurrence of a pattern in a list of strings using a Trie data structure.

    This function creates a Trie and inserts all the strings from the list into the Trie. Then it searches for the pattern
    in the Trie. If the pattern is found, it returns the index of the first string in the list where the pattern is found
    as a substring. If the pattern is not found in any string, it returns None.

    Args:
        strings (list): The list of strings to search in.
        target (str): The pattern to search for.

    Returns:
        int | None: The index of the first string in the list where the pattern is found as a substring.
                     If the pattern is not found in any string, it returns None.

    Doctest:
        >>> find_substring(["hello", "world", "python", "programming"], "pyt")
        2
        >>> find_substring(["hello", "world", "python", "programming"], "java") is None
        True
        >>> find_substring(["hello", "world", "python", "programming"], "o")
        0
        >>> find_substring(["hello", "world", "python", "programming"], "")
        Traceback (most recent call last):
        ...
        ValueError: The target string cannot be empty.
        >>> find_substring([], "hello")
        Traceback (most recent call last):
        ...
        ValueError: The list of strings cannot be empty.
    """
    # Check if the list of strings is empty
    if not strings:
        raise ValueError("The list of strings cannot be empty.")

    # Check if the target string is empty
    if not target:
        raise ValueError("The target string cannot be empty.")

    trie = Trie()  # Create a Trie
    for string in strings:  # For each string in the list
        trie.insert(string)  # Insert the string into the Trie

    # Search for the pattern in the Trie and return the result
    return trie.search(target)
