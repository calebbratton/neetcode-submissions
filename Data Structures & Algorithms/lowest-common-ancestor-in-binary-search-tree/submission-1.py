# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        lca = root
        stack = [lca]
        while stack:
            node = stack.pop()
            if node is None:
                continue
            if self.isSubtree(node, p) and self.isSubtree(node, q):
                lca = node
                stack.append(node.left)
                stack.append(node.right)
        return lca
            
    def isSubtree(self, root, sub):
        def isSame(node1, node2):
            if node1 is None and node2 is None:
                return True
            if node1 and node2 and node1.val == node2.val:
                return isSame(node1.left, node2.left) and isSame(node1.right, node2.right)
            return False

        if root is None:
            return False
        if isSame(root, sub):
            return True
        return self.isSubtree(root.left, sub) or self.isSubtree(root.right, sub)
        

            

        