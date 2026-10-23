class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        l, r = 0, len(height) - 1
        maxL, maxR = height[0], height[r]
        while l < r:
            if maxR < maxL:
                r -= 1
                maxR = max(maxR, height[r])
                res += maxR - height[r]
            else:
                l += 1
                maxL = max(maxL, height[l])
                res += maxL - height[l]

        return res