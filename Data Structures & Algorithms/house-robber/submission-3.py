class Solution:
    def rob(self, nums: List[int]) -> int:
        old, curr = 0, 0
        for num in nums:
            new = max(num+old, curr)
            old = curr
            curr = new
        return curr