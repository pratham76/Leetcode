# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        if not root:
            return []  # Return an empty list for an empty tree

        res = []
        curr_lvl = [root]
        while curr_lvl:
            next_lvl = []
            res_lvl=[]
            for node in curr_lvl:
                res_lvl.append(node.val)
                if node.left:
                    next_lvl.append(node.left)
                if node.right:
                    next_lvl.append(node.right)
            curr_lvl = next_lvl
            res.insert(0,res_lvl)
        return res
        