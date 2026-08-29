class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        maxP = 1
        zeroCount = 0
        for num in nums:
            if num == 0:
                zeroCount+=1
            else:
                maxP *= num
        if zeroCount > 0:
            if zeroCount > 1:
                return [0] * len(nums)
            else:
                return [maxP if n == 0 else 0 for n in nums]

        return [maxP // n for n in nums]

