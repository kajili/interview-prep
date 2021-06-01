import pytest

from src.leetcode.hash_table.TwoSum import Solution

tests_for_twoSum = [([2, 7, 11, 15],    # nums
                     9,                 # target
                     [0, 1]),           # expected

                    ([3, 2, 4],
                     6,
                     [1, 2]),

                    ([3, 3],
                     6,
                     [0, 1])]


@pytest.mark.parametrize("nums,target,expected", tests_for_twoSum)
def test_twoSum(nums, target, expected):
    sol = Solution()
    function_result = sol.twoSum(nums, target)
    assert function_result == expected
