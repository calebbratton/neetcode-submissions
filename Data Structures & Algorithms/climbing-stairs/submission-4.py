class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        b1, b2 = 1, 1
        for i in range(n-1):
            print(i)
            b1, b2 = b2, b2 + b1
        return b2