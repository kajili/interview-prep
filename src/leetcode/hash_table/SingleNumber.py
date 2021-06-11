# LeetCode 136. Single Number [Easy]

# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

# You must implement a solution with a linear runtime complexity and use only constant extra space.

# Example 1:

# Input: nums = [2,2,1]
# Output: 1

# Example 2:

# Input: nums = [4,1,2,1,2]
# Output: 4

# Example 3:

# Input: nums = [1]
# Output: 1

class Solution:
    def singleNumber(self, nums) -> int:
        # Create a hash table
        singleNum = {}
        for num in nums:
            if num not in singleNum:
                singleNum[num] = 1
            else:
                singleNum[num] += 1
        # Return key of hash table that has a value of 1
        for num in singleNum:
            value = singleNum[num]
            if value == 1:
                return num
