# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        if not root:
            return []
        Q = deque([root])
        levels = [[root.val]]
        temp = deque()

        while Q:
            node = Q.popleft()
            if node.left: temp.append(node.left)
            if node.right: temp.append(node.right)
            
            if not Q:
                if temp:
                    levels.append([n.val for n in temp])
                Q = temp
                temp = deque()

        return levels
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
        
         
        