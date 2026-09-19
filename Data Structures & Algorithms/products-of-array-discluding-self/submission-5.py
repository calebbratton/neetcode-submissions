class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        zeroIndicies = []
        for i, n in enumerate(nums):
            if n == 0:
                zeroIndicies.append(i)
            else:
                total *= n
        out = [0] * len(nums)
        if len(zeroIndicies) > 1:
            return out
        elif len(zeroIndicies) == 1:
            out[zeroIndicies[0]] = total
            return out
        for i, n in enumerate(nums):
            out[i] = int(total / n)
        return out
            