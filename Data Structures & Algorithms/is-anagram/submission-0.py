class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        found = [i for i in s]

        for j in t:
            if j in found:
                found.remove(j)

        return len(found) == 0


                