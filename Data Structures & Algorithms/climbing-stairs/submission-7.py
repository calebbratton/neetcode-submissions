class Solution:
    def climbStairs(self, n: int, memo = {1: 1, 2: 2}) -> int:
        if n < 1:
            return 0
        
        if n in memo:
            return memo[n]
        
        memo[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        return memo[n]