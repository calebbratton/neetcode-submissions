class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero = -1
        for i,n in enumerate(nums):
            if n == 0:
                if zero > -1:
                    return [0] * len(nums)
                else:
                    zero = i
            else:
                product *= n
        if zero > -1:
            res = [0] * len(nums)
            res[zero] = product
            return res

        return [product // v for v in nums]