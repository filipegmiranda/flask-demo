from unittest import TestCase

from palindromy.palindromes_analyser import palindromes_in_json_keys, is_palindrome, \
    count_palindromes


class TestPalindromyModule(TestCase):
    def test_palindromes_in_json_keys(self):
        palindromes = palindromes_in_json_keys(self._simple_input_data())
        self.assertEqual(len(palindromes), 1)
        self.assertEqual(palindromes[0], "racecar")

    def test_count_palindromes(self):
        count = count_palindromes(self._simple_input_data())
        self.assertEqual(count, 1)

    def test_is_palindrome(self):
        palindrome_example = "solos"
        another_palindrome = "Step on no pets"
        not_palindrome = "meat"
        self.assertTrue(is_palindrome(palindrome_example))
        self.assertTrue(is_palindrome(another_palindrome))
        self.assertFalse(is_palindrome(not_palindrome))

    def _simple_input_data(self):
        return [
            """{"foo": "bar"}""",
            """{"key": "racecar"}""",
            """{"key": "not a palindrome", "word": "sentence"}"""
        ]
