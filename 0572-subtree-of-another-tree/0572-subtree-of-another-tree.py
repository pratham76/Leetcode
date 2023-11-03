# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        def isidentical(root1,root2):
            if not root1 and not root2:
                return True
            if not root1 or not root2:
                return False
            return (root1.val==root2.val) and isidentical(root1.left,root2.left) and isidentical(root1.right,root2.right)
        
        if not root:
            return False
        if isidentical(root, subRoot):
            return True
        
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
        
        
            
        