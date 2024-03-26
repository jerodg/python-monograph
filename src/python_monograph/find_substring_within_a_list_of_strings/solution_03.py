"""
Python Monograph -> Find a Substring Within a List -> Solution 03

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


class Node:
    """
    A Node class for the Suffix Tree data structure.

    A Node in a Suffix Tree represents a character in a string. Each Node has a dictionary of its children and a boolean flag
    indicating whether it is the end of a string.

    Attributes:
        children (dict): A dictionary where each key-value pair represents a child node. The key is the character, and the value
        is the child Node.
        end_of_string (bool): A flag indicating whether this node is the end of a string.

    Doctest:
        >>> node = Node()
        >>> node.children
        {}
        >>> node.end_of_string
        False
        >>> node.children['a'] = Node()
        >>> node.children['a'].children
        {}
        >>> node.children['a'].end_of_string
        False
        >>> node.children['a'].end_of_string = True
        >>> node.children['a'].end_of_string
        True
    """

    def __init__(self):
        self.children = {}  # Initialize the children dictionary
        self.end_of_string = False  # Initialize the end_of_string flag as False


class SuffixTree:
    """
    A SuffixTree class for the Suffix Tree data structure.

    A Suffix Tree is a tree-like data structure that stores strings in a way that allows for efficient substring searching.
    Each node in the Suffix Tree represents a character, and each path from the root to a node represents a string.

    Attributes:
        root (Node): The root node of the Suffix Tree.

    Doctest:
        >>> tree = SuffixTree()
        >>> tree.insert("hello")
        >>> tree.find_substring("hell")
        True
        >>> tree.find_substring("world")
        False
        >>> tree.insert("world")
        >>> tree.find_substring("world")
        True
        >>> tree.find_substring("python")
        False
        >>> tree.find_substring("")
        True
    """

    def __init__(self):
        self.root = Node()  # Initialize the root node of the Suffix Tree

    def insert(self, word: str) -> None:
        """
        Insert a word and its suffixes into the Suffix Tree.

        This method takes a word as input and inserts it and all its suffixes into the Suffix Tree. It starts from the first
        character of the word and for each character, it calls the _insert method to insert the suffix starting from that character
        into the Suffix Tree.

        Args:
            word (str): The word to be inserted into the Suffix Tree.

        Doctest:
            >>> tree = SuffixTree()
            >>> tree.insert("hello")
            >>> tree.find_substring("hello")
            True
            >>> tree.find_substring("hell")
            True
            >>> tree.find_substring("ello")
            True
            >>> tree.find_substring("world")
            False
            >>> tree.insert("world")
            >>> tree.find_substring("world")
            True
        """
        for i in range(len(word)):  # For each character in the word
            self._insert(word[i:])  # Insert the suffix starting from that character into the Suffix Tree

    def _insert(self, suffix: str) -> None:
        """
        Insert a suffix into the Suffix Tree.

        This method takes a suffix as input and inserts it into the Suffix Tree. It starts from the root node and for each
        character in the suffix, it checks if the character is already a child of the current node. If not, it creates a new
        Node for that character and adds it as a child of the current node. Then it moves to the child node and repeats the
        process for the next character. When all characters of the suffix have been inserted, it sets the end_of_string flag
        of the last node to True.

        Args:
            suffix (str): The suffix to be inserted into the Suffix Tree.

        Doctest:
            >>> tree = SuffixTree()
            >>> tree._insert("hello")
            >>> tree.find_substring("hello")
            True
            >>> tree._insert("hell")
            >>> tree.find_substring("hell")
            True
            >>> tree._insert("ello")
            >>> tree.find_substring("ello")
            True
            >>> tree._insert("world")
            >>> tree.find_substring("world")
            True
            >>> tree._insert("")
            >>> tree.find_substring("")
            True
        """
        node = self.root  # Start from the root node
        for char in suffix:  # For each character in the suffix
            if char not in node.children:  # If the character is not already a child of the current node
                node.children[char] = Node()  # Create a new Node for that character and add it as a child of the current node

            node = node.children[char]  # Move to the child node

        node.end_of_string = True  # Set the end_of_string flag of the last node to True

    # fixme: This needs to be reworked.
    def search(self, pattern: str) -> bool:
        """
        Search for a pattern in the Suffix Tree.

        This method takes a pattern as input and searches for it in the Suffix Tree. It starts from the root node and for each
        character in the pattern, it checks if the character is a child of the current node. If not, it returns False. If the
        character is a child of the current node, it moves to the child node and repeats the process for the next character. If
        all characters of the pattern are found in the tree, it returns True.

        Args:
            pattern (str): The pattern to be searched in the Suffix Tree.

        Returns:
            bool: True if the pattern is found in the tree, False otherwise.

        Doctest:
            >>> tree = SuffixTree()
            >>> tree.insert("hello")
            >>> tree.find_substring("hell")
            True
            >>> tree.find_substring("world")
            False
            >>> tree.insert("world")
            >>> tree.find_substring("world")
            True
            >>> tree.find_substring("python")
            False
            >>> tree.find_substring("")
            True
        """
        node = self.root  # Start from the root node
        for char in pattern:  # For each character in the pattern
            if char not in node.children:  # If the character is not a child of the current node
                return False  # Return False
            node = node.children[char]  # Move to the child node

        return True  # Return True if all characters of the pattern are found in the tree


def find_substring(strings: list, pattern: str) -> [int | None]:
    """
    Find a substring within a list of strings.

    This function takes a list of strings and a pattern as input. It creates a SuffixTree and inserts each string from the list
    into the tree. Then it searches for the pattern in the tree. If the pattern is found, it returns True. If the pattern is not
    found, it returns False.

    Args:
        strings (list): The list of strings to be searched.
        pattern (str): The pattern to be searched for.

    Returns:
        int | None: The index of the first occurrence of the pattern in the list if found, None otherwise.

    Doctest:
        >>> find_substring(["hello", "world", "python", "programming"], "hell")
        True
        >>> find_substring(["hello", "world", "python", "programming"], "java")
        False
        >>> find_substring(["hello", "world", "python", "programming"], "o")
        True
        >>> find_substring(["hello", "world", "python", "programming"], "")
        True
        >>> find_substring([], "hello")
        False
    """
    tree = SuffixTree()  # Create a SuffixTree
    for string in strings:  # For each string in the list
        tree.insert(string)  # Insert the string into the tree

    return tree.search(pattern)  # Search for the pattern in the tree and return the result
