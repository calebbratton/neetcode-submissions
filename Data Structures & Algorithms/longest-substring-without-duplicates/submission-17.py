class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        i = 0
        seen = {}

        for j, v in enumerate(s):
            if s[j] in seen:
                i = max(i, seen[s[j]] + 1)
            longest = max(longest, j - i + 1)
            seen[s[j]] = j
        
        return longest
