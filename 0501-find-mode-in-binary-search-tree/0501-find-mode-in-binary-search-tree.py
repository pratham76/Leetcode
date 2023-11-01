# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        hash=collections.defaultdict(int)
        def dfs(root):

            if not root:
                return 
            dfs(root.left)
            hash[root.val]+=1
            dfs(root.right)
        res=[]
        dfs(root)
        max_val=max(hash.values())
        for key,val in hash.items():
            if hash[key]==max_val:
                res.append(key)
        return res