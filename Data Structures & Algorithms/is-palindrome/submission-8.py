class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            if not self.isAlnum(s[l]):
                l+=1
            elif not self.isAlnum(s[r]):
                r-=1
            elif s[r].lower() != s[l].lower():
                return False
            else:
                r-=1
                l+=1
        return True
    
    def isAlnum(self, char: str) -> bool:
        c = ord(char)
        A, a, Z, z, zero, nine = ord('A'), ord('a'), ord('Z'), ord('z'), ord('0'), ord('9')
        isalnum =  A <= c <= Z or a <= c <= z or zero <= c <= nine
        return isalnum