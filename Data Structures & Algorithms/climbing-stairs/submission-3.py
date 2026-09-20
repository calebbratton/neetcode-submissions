class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        i = 3
        b1, b2 = 1, 2
        while i <= n:
            b1, b2 = b2, b2 + b1
            i += 1
        return b2