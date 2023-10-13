# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        if self.leaves(root1)==self.leaves(root2):
            return True
        return False
    
    def leaves(self,root):
        res=[]
        def helper(root):
            if not root:
                return 
            if not root.left and not root.right:
                res.append(root.val)
            helper(root.left)
            helper(root.right)
        
        helper(root)
        return res
    
        