class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False
        brackets = {
            '[': ']',
            '(': ')',
            '{': '}'
        }
        stack = []
        for c in s:
            if c in brackets:
                stack.append(brackets[c])
            elif stack and stack[-1] == c:
                stack.pop()
            else:
                return False
        return False if stack else True