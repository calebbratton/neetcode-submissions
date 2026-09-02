class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = s.replace(" ", "").lower()
        print(t)
        l, r = 0, len(t) - 1
        while l < r:
            if not t[l].isalnum():
                l+=1
            elif not t[r].isalnum():
                r-=1
            elif t[r] != t[l]:
                return False
            else:
                r-=1
                l+=1
        return True