# LeetCode 46. Permutations [Medium]

# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

# Example 1:

# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

# Example 2:

# Input: nums = [0,1]
# Output: [[0,1],[1,0]]

# Example 3:

# Input: nums = [1]
# Output: [[1]]

class Solution:
    def permute(self, nums):
        result = []
        if len(nums) == 0:
            return result
        visited = [False] * len(nums)
        # Can use set since numbers are distinct here
        # visited = set()
        self.backtrack(nums, visited, [], result)

        return result

    def backtrack(self, nums, visited, permutation, result):
        # If we find a permutation, add a copy of the permutation list to the result
        if len(permutation) == len(nums):
            result.append(permutation[:])
        for i, num in enumerate(nums):
            if visited[i]:
                continue
            visited[i] = True
            permutation.append(num)
            self.backtrack(nums, visited, permutation, result)
            permutation.pop()
            visited[i] = False
