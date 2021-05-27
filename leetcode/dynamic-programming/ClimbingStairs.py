# LeetCode 70. Climbing Stairs (Easy)

# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

class Solution:
    def climbStairs(self, n: int) -> int:
        # Initialize array with extra space for step 0
        dp = [0] * (n + 1)

        # Base cases - there is 1 way to reach step 0 and 1
        dp[0] = 1
        dp[1] = 1

        # Iterate through the steps starting from step 2 and build from the previous recurrance relations
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        # Return the combination of steps at n
        return dp[n]


def main():
    solution = Solution()

    tests = []
    tests.append(solution.climbStairs(2))
    tests.append(solution.climbStairs(3))
    tests.append(solution.climbStairs(5))

    print(tests)


if __name__ == '__main__':
    main()

# Example 1:

# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# Example 2:

# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
