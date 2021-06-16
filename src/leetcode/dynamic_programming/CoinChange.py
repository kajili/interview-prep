# LeetCode 322. Coin Change

# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

# Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

# You may assume that you have an infinite number of each kind of coin.

# Example 1:

# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1

# Example 2:

# Input: coins = [2], amount = 3
# Output: -1

# Example 3:

# Input: coins = [1], amount = 0
# Output: 0

# Example 4:

# Input: coins = [1], amount = 1
# Output: 1

# Example 5:

# Input: coins = [1], amount = 2
# Output: 2

class Solution:
    def coinChange(self, coins, amount: int) -> int:
        # Initial Thoughts:
        # Because we want to find the fewest number of coins to make up an amount, we most likely
        # can build a solution that is recursive in nature, i.e. we can build the solutions for the
        # fewest number of coins for lower amounts than the given amount. In fact we can start from
        # 0 and realize we can only have one answer for the amount 0, which is 0 coins. So that will be
        # the base case. Most likely because of the nature of this solution there will be recalculations
        # so we can use Dynamic Programming to store values along the way to reduce run time.

        # Algorithm:
        # So we can go through every amount starting at 1, knowing the value of the num of coins for amount
        # 0. Then we can also go through each type of available coin in our coins list.
        # Next we can check if our current amount minus our current coin is greater than 0. Otherwise the coin would take us
        # past our amount.
        # If so, then we can check if the number of coins it takes to reach our current amount using that coin is less
        # then the previously calculated number of coins for that given amount in our DP array.
        #
        # This can be done by checking what the minimum value between the current amount in our DP array
        # (which represents the previously calculated minimum number of coins for that amount),
        # or the DP array if we included the current coin (which means we add 1, representing choosing that coin,
        # to the previously calculated number of coins it took to get to the current amount - current coin.
        # This is stored in the DP[current amount - current coin]). We store this minimum in the current amount index
        # of our DP array.

        # Initialize the dp array
        dp = [float('inf')] * (amount + 1)
        # Base case
        dp[0] = 0

        for currAmount in range(1, amount + 1):
            for coin in coins:
                if currAmount - coin >= 0:
                    dp[currAmount] = min(dp[currAmount], 1 + dp[currAmount - coin])

        return dp[amount] if dp[amount] != float('inf') else -1
