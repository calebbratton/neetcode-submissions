# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = [(p, q)]

        while stack:
            c = stack.pop()
            cp, cq = c[0], c[1]
            if cp is None and cq is None:
                continue
            if cp is None or cq is None or cp.val != cq.val:
                return False
            stack.append((cp.left, cq.left))
            stack.append((cp.right, cq.right))

        return True                