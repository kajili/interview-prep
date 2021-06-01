# LeetCode 462. Minimum Moves to Equal Array Elements II [Medium]

# Given an integer array nums of size n, return the minimum number of moves required to make all array elements equal.

# In one move, you can increment or decrement an element of the array by 1.

# Test cases are designed so that the answer will fit in a 32-bit integer.

import math


class Solution:
    def minMoves2(self, nums) -> int:
        nums_of_moves = 0
        middle_index = math.floor(len(nums) / 2)
        isEvenLength = (len(nums) % 2 == 0)
        nums.sort()

        if isEvenLength:
            second_middle_index = middle_index - 1
            median = math.floor(
                (nums[middle_index] + nums[second_middle_index]) / 2
            )
        else:
            median = nums[middle_index]

        for num in nums:
            diff_from_median = abs(num - median)
            nums_of_moves += diff_from_median

        return nums_of_moves


def main():
    solution = Solution()
    tests = []
    tests.append(solution.minMoves2(nums=[1, 2, 3]))
    tests.append(solution.minMoves2(nums=[1, 10, 2, 9]))
    print(tests)


if __name__ == '__main__':
    main()

# Output:
# [2, 16]

# Example 1:

# Input: nums = [1,2,3]
# Output: 2
# Explanation:
# Only two moves are needed (remember each move increments or decrements one element):
# [1,2,3]  =>  [2,2,3]  =>  [2,2,2]


# Example 2:

# Input: nums = [1,10,2,9]
# Output: 16
