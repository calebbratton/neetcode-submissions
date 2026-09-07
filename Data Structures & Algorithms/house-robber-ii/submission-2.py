class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.theft(nums[1:]),
        self.theft(nums[:-1]))
        
    def theft(self, nums: list[int]) -> int:
        old, curr = 0, 0
        for n in nums:
            new = max(n + old, curr)
            old = curr
            curr = new
        return curr