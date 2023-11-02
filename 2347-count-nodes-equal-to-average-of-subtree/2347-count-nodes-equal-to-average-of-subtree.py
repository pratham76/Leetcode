# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            nonlocal count
            if not root:
                return [0,0]
            left,right=dfs(root.left),dfs(root.right)
            totalsum=left[0]+right[0]+root.val
            totalnode=left[1]+right[1]+1
            if floor(totalsum/totalnode)==root.val:
                count+=1
            return [totalsum,totalnode]
        count=0
        if not root:
            return count
        dfs(root)
        return count
        