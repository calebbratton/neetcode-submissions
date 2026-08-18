# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        self.res = True
        def dfs(root):
            if root is None:
                return 0
            
            l, r = dfs(root.left), dfs(root.right)
            if abs(l - r) > 1:
                self.res = False
            return 1 + max(l, r)
        dfs(root)

        return self.res