# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return 
        curr_lvl=[root]
        res=[]
        while curr_lvl:
            next_lvl=[]
            max_val=-float("inf")
            for node in curr_lvl:
                max_val=max(max_val,node.val)
                if node.left:
                    next_lvl.append(node.left)
                if node.right:
                    next_lvl.append(node.right)
            curr_lvl=next_lvl
            res.append(max_val)
        return res


        