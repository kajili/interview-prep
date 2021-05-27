# LeetCode 1. Two Sum [Easy]

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

class Solution:
    def twoSum(self, nums, target: int):
        result = {}
        for index, num in enumerate(nums):
            complement = target - num
            if (complement in result):
                return [result[complement], index]
            else:
                result[num] = index


def main():
    solution = Solution()
    tests = []
    tests.append(solution.twoSum(nums=[2, 7, 11, 15], target=9))
    tests.append(solution.twoSum(nums=[3, 2, 4], target=6))
    tests.append(solution.twoSum(nums=[3, 3], target=6))
    for test in tests:
        print(test)


if __name__ == '__main__':
    main()

# Output:
# [0, 1]
# [1, 2]
# [0, 1]

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]
