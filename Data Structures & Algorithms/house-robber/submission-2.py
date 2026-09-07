class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        
        for i in range(2, len(nums), 1):
            nums[i] = max(nums[i-1], nums[i-2] + nums[i])
            nums[i-1] = max(nums[i-2], nums[i-1])
        return max(nums[-2], nums[-1])