# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        curr_lvl=[root]
        res=[]
        while curr_lvl:
            next_lvl=[]
            res_lvl=[]
            for node in curr_lvl:
                res_lvl.append(node.val)
                if node.left:
                    next_lvl.append(node.left)
                if node.right:
                    next_lvl.append(node.right)
            curr_lvl=next_lvl
            res.append(res_lvl)
        return res
        