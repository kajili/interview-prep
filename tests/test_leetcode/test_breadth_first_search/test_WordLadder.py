import pytest

from src.leetcode.breadth_first_search.WordLadder import Solution

tests_for_ladderLength = [("hit",
                           "cog",
                           ["hot", "dot", "dog", "lot", "log", "cog"],
                           5),

                          ("hit",
                           "cog",
                           ["hot", "dot", "dog", "lot", "log"],
                           0),
                          ]


@pytest.mark.parametrize("beginWord,endWord,wordList,expected", tests_for_ladderLength)
def test_ladderLength(beginWord, endWord, wordList, expected):
    sol = Solution()
    function_result = sol.ladderLength(beginWord, endWord, wordList)
    assert function_result == expected
