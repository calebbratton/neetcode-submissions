class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        foundS, foundT = {}, {}

        for i in range(len(s)):
            foundS[s[i]] = 1+foundS.get(s[i], 0)
            foundT[t[i]] = 1+foundT.get(t[i], 0)

        return foundS == foundT


                