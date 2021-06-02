import pytest

from src.cracking_the_coding_interview.ch_01_arrays_and_strings.Q1_03_URLify import URLify_NewString, \
    URLify_InPlace

tests_for_URLify = [("Mr John Smith      ",  # inputString
                     13,  # trueLength
                     "Mr%20John%20Smith"),  # expected

                    ("Does this work yet?       ",
                     19,
                     "Does%20this%20work%20yet?")]


@pytest.mark.parametrize("inputString,trueLength,expected", tests_for_URLify)
def test_URLify_NewString(inputString, trueLength, expected):
    function_result = URLify_NewString(inputString, trueLength)
    assert function_result == expected


@pytest.mark.parametrize("inputString,trueLength,expected", tests_for_URLify)
def test_URLify_InPlace(inputString, trueLength, expected):
    function_result = URLify_InPlace(inputString, trueLength)
    assert function_result == expected
