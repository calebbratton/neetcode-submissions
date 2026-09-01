class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        productNoZero = 1
        zeroIndices = []
        for i, num in enumerate(nums):
            if num == 0:
                zeroIndices.append(i)
                if len(zeroIndices) > 1:
                    return [0] * len(nums)
            else:
                productNoZero *= num
        
        if len(zeroIndices):
            res = [0] * len(nums)
            res[zeroIndices[0]] = productNoZero
            return res
        
        return [productNoZero//n for n in nums]