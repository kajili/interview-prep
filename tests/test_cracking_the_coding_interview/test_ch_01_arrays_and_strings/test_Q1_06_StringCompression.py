import pytest

from src.cracking_the_coding_interview.ch_01_arrays_and_strings.Q1_06_StringCompression import stringCompression

tests_for_stringCompression = [("aabcccccaaa",  # inputString
                                "a2b1c5a3"),  # expected

                               ("abcd",
                                "abcd"),

                               ("bbbddeeeeffffgggghhhhhiizkxxx",
                                "b3d2e4f4g4h5i2z1k1x3")]


@pytest.mark.parametrize("inputString,expected", tests_for_stringCompression)
def test_stringCompression(inputString, expected):
    function_result = stringCompression(inputString)
    assert function_result == expected
