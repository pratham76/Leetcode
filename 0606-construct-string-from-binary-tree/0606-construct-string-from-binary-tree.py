# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def preorder(root):
            if not root:
                return ""
            
            result = str(root.val)
            
            left_str = preorder(root.left)
            right_str = preorder(root.right)
            
            if left_str or right_str:
                result += "(" + left_str + ")"
            
            if right_str:
                result += "(" + right_str + ")"
            
            return result
        
        return preorder(root)







        self.out=''
        preorder(root)
        return self.out
        