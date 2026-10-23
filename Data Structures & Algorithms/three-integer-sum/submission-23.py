class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        seen = set()
        for i, n in enumerate(nums):
            l,r = i+1, len(nums)-1
            while l < r:
                curr = n + nums[l] + nums[r]
                key = str(n) + str(nums[l]) + str(nums[r])
                if curr > 0:
                    r-=1
                elif curr < 0:
                    l += 1
                else:
                    if key not in seen:
                        res.append([n,nums[l], nums[r]])
                        seen.add(key)
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                    l+=1
                    r-=1
        return res
            