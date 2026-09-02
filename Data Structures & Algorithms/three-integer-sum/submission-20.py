class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i, n in enumerate(nums):
            if n > 0: 
                return result
            if i > 0 and nums[i-1] == n:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                val = n + nums[l] + nums[r]
                if val > 0:
                    r -= 1
                elif val < 0:
                    l += 1
                else:
                    result.append([n, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l-1] == nums[l]:
                        l += 1
        return result
        