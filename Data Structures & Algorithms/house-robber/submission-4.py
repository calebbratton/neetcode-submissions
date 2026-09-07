class Solution:
    def rob(self, nums: List[int]) -> int:
        prev, curr = 0, 0
        for num in nums:
            new = max(num+prev, curr)
            prev = curr
            curr = new
        return curr