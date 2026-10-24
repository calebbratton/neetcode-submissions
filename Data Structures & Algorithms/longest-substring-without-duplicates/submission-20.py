class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        l = 0
        seen = {}
        for i, c in enumerate(s):
            if c in seen:
                l = max(l, seen[c]+1)
            seen[c] = i
            res = max(res, i - l + 1)
        return res