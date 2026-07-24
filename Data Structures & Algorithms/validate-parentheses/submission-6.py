class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            ')':'(',
            ']':'[',
            '}':'{'
        }
        stack = []
        for p in s:
            if p in brackets:
                if stack and stack[-1] == brackets[p]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(p)
        
        return not stack

