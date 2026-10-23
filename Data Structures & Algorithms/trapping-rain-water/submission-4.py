class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        l, r = 0, len(height) - 1
        maxL, maxR = height[0], height[r]
        while l < r:
            curr = max(0, min(maxL, maxR) - min(height[l], height[r]))
            if curr > 0:
                res += curr
            if height[r] < height[l]:
                r -= 1
                maxR = max(maxR,height[r])
            else:
                l += 1
                maxL = max(maxL, height[l])

        return res