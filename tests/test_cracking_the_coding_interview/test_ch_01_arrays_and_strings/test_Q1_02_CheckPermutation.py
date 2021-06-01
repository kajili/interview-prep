import pytest

from src.cracking_the_coding_interview.ch_01_arrays_and_strings.Q1_02_CheckPermutation import \
    checkPermutationSingleHashTable, checkPermutationDoubleHashTable

tests_for_checkPermutation = [("anagram", "nagaram", True),
                              ("rat", "car", False)]


@pytest.mark.parametrize("str1,str2,expected", tests_for_checkPermutation)
def test_checkPermutationSingleHashTable(str1, str2, expected):
    function_result = checkPermutationSingleHashTable(str1, str2)
    assert function_result == expected


@pytest.mark.parametrize("str1,str2,expected", tests_for_checkPermutation)
def test_checkPermutationDoubleHashTable(str1, str2, expected):
    function_result = checkPermutationDoubleHashTable(str1, str2)
    assert function_result == expected
