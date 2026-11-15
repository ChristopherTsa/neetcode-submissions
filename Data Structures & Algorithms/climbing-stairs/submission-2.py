class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {1: 1, 2: 2}

        def dfs(k: int) -> int:
            if k in memo:
                return memo[k]
            memo[k] = dfs(k - 1) + dfs(k - 2)
            return memo[k]

        return dfs(n)
