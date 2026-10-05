class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return max(nums)
        memo = {}
        def steal(i: int):
            if i >= n:
                return 0
            if i in memo:
                return memo[i]
            memo[i] = max(nums[i] + steal(i + 2), steal(i + 1))
            return memo[i]
        return max(steal(0), steal(1))
         