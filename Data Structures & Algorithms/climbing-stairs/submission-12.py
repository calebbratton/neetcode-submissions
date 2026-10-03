class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [-1] * n
        
        def ways(i):
            if i > n:
                return 0
            if i == n:
                return 1
            if memo[i] != -1:
                return memo[i]
            memo[i] = ways(i + 1) + ways(i + 2)
            return memo[i]

        return ways(0)