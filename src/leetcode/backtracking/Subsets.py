# LeetCode 78. Subsets [Medium]

# Given an integer array nums of unique elements, return all possible subsets (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.

# Example 1:

# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

# Example 2:

# Input: nums = [0]
# Output: [[],[0]]

class Solution:
    def subsets(self, nums):
        # Initial Thoughts:
        # Use backtracking. We can think of this problem as a tree with two decisions at
        # each node.
        #
        # Either we can include an element or we can not. So if we are looking at [1,2,3],
        # we can start by either including 1 or not including one, generating two subsets of
        # [1] and []. Then branching off of those two subsets, we can decide on both of them
        # whether or not to include 2. So we end up with 4 subsets, [1], [1,2] (both from [1]),
        # [2], and [] (both from []). If we continue this process using 3 as the next decision,
        # we will end up with 8 total subsets which would be the result we want:
        # ([[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]])
        #
        # To accomplish this we will use backtracking to recurse, with the decision point
        # being whether or not we want to include the next element of the original list.
        # We will also be checking if our subset is valid and include it in our answer list
        # when that is the case. Otherwise we will continue recursing through the original list
        # and check if subsets created by following the above method are valid. After recursing
        # we must also undo our selection so we can try the next one.

        # Algorithm:
        # Create a result list for the list of subsets, and a subset list for each individual
        # subset. Pass in the index of the value we want to check for our subset creation
        # to a dfs backtracking function.
        #
        # Within that function, we will add a copy of the current subset to the result list
        # if our current index is out of bounds of the number list (meaning we checked all
        # values for that subset).
        #
        # Then make the decision whether or not we will include the number at that index.
        # When we decide to include the number, we will add it to the current subset list,
        # then recurse again on the next index. For the opposite decision, we will pop that same
        # number off of the list (backtracking) and then recurse again on the next index. This
        # way we are checking both pathways through recursion.
        #
        # Finally we will just call that dfs backtracking function within the original function,
        # and start it at index 0. Then we can just return our result list.

        result = []
        subset = []

        def dfs_backtracking(index):
            if index > len(nums) - 1:
                result.append(subset[:])
            else:
                subset.append(nums[index])
                dfs_backtracking(index + 1)

                subset.pop()
                dfs_backtracking(index + 1)

        dfs_backtracking(0)

        return result
