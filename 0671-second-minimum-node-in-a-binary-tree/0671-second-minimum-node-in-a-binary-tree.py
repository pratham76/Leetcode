# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        min_val=root.val
        sec_min_val=float("inf")

        def dfs(node):
            nonlocal min_val,sec_min_val
            if node.val<min_val:
                min_val=sec_min_val
            elif node.val!=min_val and node.val<sec_min_val:
                sec_min_val=node.val
            
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
        dfs(root)

        return sec_min_val if sec_min_val !=float("inf") else -1