"""
Homework 07: Library of Word Functions, all written recursively
===========================
Course:   CS 5001
Semester: Fall 2024
Student:  Cassie Honda

Various functions to practice recursion.
"""


def is_palindrome(word: str) -> bool:
    """
    Recursively looks at a string to determine if it is a palindrome.

    Does not remove punctuation or spaces, and assumes the word is
    already in lower case.

    Examples:
        >>> is_palindrome('racecar')
        True
        >>> is_palindrome('hello')
        False

    Args:
        word (str): the word to check

    Returns:
        bool: True if the word is a palindrome, False otherwise
    """
    word = word.lower()
    if len(word) <= 1:
        return True
    elif word[0] == word[-1]:
        return is_palindrome(word[1:-1])
    else:
        return False


def count_vowels(word: str) -> int:
    """
    Recursively counts the number of vowels in a string. Case
    does not matter.

    Examples:
        >>> count_vowels('hello')
        2
        >>> count_vowels('aeiou')
        5
        >>> count_vowels('AEIOU')
        5

    Args:
        word (str): the word to check

    Returns:
        int: the number of vowels in the word
    """
    word = word.lower()
    vowels = ['a', 'e', 'i', 'o', 'u']

    if len(word) == 0:
        return 0
    else:
        if word[-1] in vowels:
            return 1 + count_vowels(word[:-1])
        else:
            return count_vowels(word[:-1])


def clean_word(word: str) -> str:
    """
    Recursively removes punctuation from a word, and reduces it to lower case.

    Examples:
        >>> clean_word('Hello!')
        'hello'
        >>> clean_word('World...')
        'world'

    See:
        https://docs.python.org/3/library/stdtypes.html#str.isalnum


    Args:
        word (str): the word to remove punctuation from

    Returns:
        str: the word without punctuation
    """
    if word == "":
        return ""
    else:
        if word[0].isalnum():
            word = word[0] + clean_word(word[1:])
            return word.lower()
        else:
            return clean_word(word[1:]).lower()



if __name__ == "__main__":  # if doctest is not installed, comment out these lines
    import doctest

    doctest.testmod(verbose=True)
