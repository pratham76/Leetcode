"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root==None:
            return 0
        else:
            depth=0
            curr_lvl=[root]
            next_lvl=[]
            while curr_lvl:
                node_out=curr_lvl.pop(0)
                for child in node_out.children:
                    next_lvl.append(child)
                if curr_lvl==[]:
                    curr_lvl,next_lvl=next_lvl,curr_lvl
                    depth+=1
            return depth


        