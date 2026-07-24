class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1
        
        while left < right:
            leftchar = s[left]
            rightchar = s[right]

            if not leftchar.isalnum():
                left+=1
                continue
            if not rightchar.isalnum():
                right-=1
                continue

            if leftchar.lower() != rightchar.lower():
                return False
            
            left+=1
            right-=1
            
        return True
        