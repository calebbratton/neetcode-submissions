class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        def climb(i: int):
            if i >= len(cost):
                return 0
            if i in memo:
                return memo[i]
            memo[i] = cost[i] + min(climb(i + 1), climb(i + 2))
            return memo[i]
        climb(0)
        return min(memo[0], memo[1])