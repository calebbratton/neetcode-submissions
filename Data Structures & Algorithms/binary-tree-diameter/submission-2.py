# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #find max depth for each path
        #bubble edge count up to parent
        #choose max of children
        #sum

        self.diameter = 0
        self.maxDepth(root)

        return self.diameter

    def maxDepth(self, node: Optional[TreeNode]):
        if node is None:
            return 0
        
        l, r = self.maxDepth(node.left), self.maxDepth(node.right)
        self.diameter = max(self.diameter, l + r)

        return 1 + max(l, r)