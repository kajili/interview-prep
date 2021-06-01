import pytest

from src.cracking_the_coding_interview.ch_01_arrays_and_strings.Q1_01_IsUnique import isUnique

tests_for_isUnique = [("abcd",  # test_string
                       True),  # expected

                      ("s4fad",
                       True),

                      ("23ds2",
                       False),

                      ("hb 627jh=j ()",
                       False)]


@pytest.mark.parametrize("test_string,expected", tests_for_isUnique)
def test_isUnique(test_string, expected):
    function_result = isUnique(test_string)
    assert function_result == expected
