class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        
        while l < r:
            m = l + (r - l) // 2
            print("current", nums[m])
            print("right", nums[r])
            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1
        
        return nums[l]