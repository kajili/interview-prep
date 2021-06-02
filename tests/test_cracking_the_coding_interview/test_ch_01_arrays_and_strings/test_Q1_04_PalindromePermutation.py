import pytest

from src.cracking_the_coding_interview.ch_01_arrays_and_strings.Q1_04_PalindromePermutation import palindromePermutation

tests_for_palindromePermutation = [("Tact Coa",  # inputString - tacocat is palindrome
                                    True),  # expected

                                   ("Yak kA", # kayak is palindrome
                                    True),

                                   ("deed",
                                    True),

                                   ("jakshdkhf",
                                    False),

                                   ("not a palindrome",
                                    False)]


@pytest.mark.parametrize("inputString,expected", tests_for_palindromePermutation)
def test_palindromePermutation(inputString, expected):
    function_result = palindromePermutation(inputString)
    assert function_result == expected
