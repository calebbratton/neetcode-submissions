class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 1:
            return 0
        res = 0
        l, r = 0, len(height)
        lMax, rMax = height[0], height[-1]
        while l < r:
            if lMax < rMax:
                l += 1
                lMax = max(lMax, height[l])
                res += lMax - height[l]
            else:
                r -= 1
                rMax = max(rMax, height[r])
                res += rMax - height[r]
        
        return res
