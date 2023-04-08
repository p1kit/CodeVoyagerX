"""
There are n oranges in the kitchen and you decided to eat some of these oranges every day as follows:

Eat one orange.
If the number of remaining oranges n is divisible by 2 then you can eat n / 2 oranges.
If the number of remaining oranges n is divisible by 3 then you can eat 2 * (n / 3) oranges.
You can only choose one of the actions per day.

Given the integer n, return the minimum number of days to eat n oranges.
"""


class Solution:
    def minDays(self, n: int) -> int:
        """
        Intuition: Since we can only choose one of the actions per day, we can use a dp table to store the minimum number of days to eat n oranges.
        and return the minimum number of days to eat n oranges.
        """

        dp = [-1] * (n + 1)
        dp[0] = 0
        dp[1] = 1

        for i in range(2, n + 1):
            dp[i] = 1 + dp[i - 1]
            if i % 2 == 0:
                dp[i] = min(dp[i], 1 + dp[i // 2])
            if i % 3 == 0:
                dp[i] = min(dp[i], 1 + dp[i // 3])

        return dp[n]


if __name__ == "__main__":
    assert Solution().minDays(10) == 4
