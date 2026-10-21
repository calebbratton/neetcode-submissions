class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dp = defaultdict(int)
        res = 0

        for num in nums:
            if dp[num] == 0:
                dp[num] = dp[num - 1] + dp[num + 1] + 1
                dp[num - dp[num-1]] = dp[num]
                dp[num + dp[num+1]] = dp[num]
                res = max(res, dp[num])
        return res
        