# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.best = 0
        def depth(node):
            if not node: return 0
            l=depth(node.left)
            r=depth(node.right)
            self.best = max(self.best, r+l)
            return 1+max(r,l)
        depth(root)
        return self.best
        
        