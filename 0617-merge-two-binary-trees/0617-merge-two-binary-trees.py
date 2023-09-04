# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
            def gh(root1,root2):
                if root1 is None and root2 is None:
                    return 
                if root1 is None:
                    return root2
                if root2 is None:
                    return root1
                s=TreeNode(root1.val+root2.val)
                s.left=gh(root1.left,root2.left)
                s.right=gh(root1.right,root2.right)
                return s
            return gh(root1,root2)