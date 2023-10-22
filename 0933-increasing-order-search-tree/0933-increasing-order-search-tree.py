# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        initial = TreeNode(0)
        dummy = initial
        
        def dfs(root):
            nonlocal dummy  
            if root == None:
                return
            dfs(root.left)
            root.left = None
            dummy.right = root
            dummy = root
            
            dfs(root.right)
        
        dfs(root)
        return initial.right