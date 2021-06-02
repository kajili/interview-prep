import pytest

from src.cracking_the_coding_interview.ch_01_arrays_and_strings.Q1_01_IsUnique import isUnique_SetLengthComparison, \
    isUnique_SetComparingEachLetter, isUnique_HashTableComparingEachLetter, isUnique_ConstantSpace

tests_for_isUnique = [("abcd",  # test_string
                       True),  # expected

                      ("s4fad",
                       True),

                      ("23ds2",
                       False),

                      ("hb 627jh=j ()",
                       False),

                      ("hb 627j= ()",
                       False)]


@pytest.mark.parametrize("test_string,expected", tests_for_isUnique)
def test_isUnique_SetLengthComparison(test_string, expected):
    function_result = isUnique_SetLengthComparison(test_string)
    assert function_result == expected


@pytest.mark.parametrize("test_string,expected", tests_for_isUnique)
def test_isUnique_SetComparingEachLetter(test_string, expected):
    function_result = isUnique_SetComparingEachLetter(test_string)
    assert function_result == expected


@pytest.mark.parametrize("test_string,expected", tests_for_isUnique)
def test_isUnique_HashTableComparingEachLetter(test_string, expected):
    function_result = isUnique_HashTableComparingEachLetter(test_string)
    assert function_result == expected


@pytest.mark.parametrize("test_string,expected", tests_for_isUnique)
def test_isUnique_ConstantSpace(test_string, expected):
    function_result = isUnique_ConstantSpace(test_string)
    assert function_result == expected
