import pytest

from src.cracking_the_coding_interview.ch_01_arrays_and_strings.Q1_05_OneAway import oneAway

tests_for_oneAway = [("pale",  # str1
                      "ple",  # str2
                      True),  # expected

                     ("pales",
                      "pale",
                      True),

                     ("pale",
                      "bale",
                      True),

                     ("pale",
                      "bake",
                      False)]


@pytest.mark.parametrize("str1,str2,expected", tests_for_oneAway)
def test_oneAway(str1, str2, expected):
    function_result = oneAway(str1, str2)
    assert function_result == expected
