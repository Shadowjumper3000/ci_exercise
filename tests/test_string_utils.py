"""Unit tests for the string_utils module."""

from src.string_utils import (
    reverse_string,
    is_palindrome,
    count_vowels,
    capitalize_words,
)


class TestReverseString:
    """Tests for the reverse_string function."""

    def test_reverse_simple_string(self):
        assert reverse_string("hello") == "olleh"

    def test_reverse_empty_string(self):
        assert reverse_string("") == ""

    def test_reverse_single_char(self):
        assert reverse_string("a") == "a"

    def test_reverse_palindrome(self):
        assert reverse_string("radar") == "radar"


class TestIsPalindrome:
    """Tests for the is_palindrome function."""

    def test_simple_palindrome(self):
        assert is_palindrome("radar") is True

    def test_not_palindrome(self):
        assert is_palindrome("hello") is False

    def test_palindrome_with_spaces(self):
        assert is_palindrome("a man a plan a canal panama") is True

    def test_palindrome_case_insensitive(self):
        assert is_palindrome("Radar") is True

    def test_empty_string_is_palindrome(self):
        assert is_palindrome("") is True


class TestCountVowels:
    """Tests for the count_vowels function."""

    def test_count_vowels_simple(self):
        assert count_vowels("hello") == 2

    def test_count_vowels_no_vowels(self):
        assert count_vowels("xyz") == 0

    def test_count_vowels_all_vowels(self):
        assert count_vowels("aeiou") == 5

    def test_count_vowels_uppercase(self):
        assert count_vowels("HELLO") == 2

    def test_count_vowels_empty_string(self):
        assert count_vowels("") == 0


class TestCapitalizeWords:
    """Tests for the capitalize_words function."""

    def test_capitalize_simple_sentence(self):
        assert capitalize_words("hello world") == "Hello World"

    def test_capitalize_single_word(self):
        assert capitalize_words("hello") == "Hello"

    def test_capitalize_already_capitalized(self):
        assert capitalize_words("Hello World") == "Hello World"

    def test_capitalize_empty_string(self):
        assert capitalize_words("") == ""
