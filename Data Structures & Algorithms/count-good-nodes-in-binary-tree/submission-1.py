# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root,maxi):

            if not root: return 0

            return (1 if root.val>=maxi else 0) + dfs(root.left, max(maxi,root.val))+ dfs(root.right,max(maxi,root.val))
        return dfs(root,float('-inf'))