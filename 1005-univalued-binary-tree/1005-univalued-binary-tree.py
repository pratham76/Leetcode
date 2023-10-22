# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        def dfs(root,val):
            if root==None:
                return True
            
            if root.val!=val:
                return False
            return dfs(root.left,val) and dfs(root.right,val)
        
        return dfs(root,root.val)
        