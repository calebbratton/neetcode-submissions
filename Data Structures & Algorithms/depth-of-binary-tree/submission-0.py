# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode], maxDepth = 0) -> int:
        if not root:
            return maxDepth
        if root:
            maxDepth += 1

        return max(self.maxDepth(root.left, maxDepth), self.maxDepth(root.right, maxDepth))