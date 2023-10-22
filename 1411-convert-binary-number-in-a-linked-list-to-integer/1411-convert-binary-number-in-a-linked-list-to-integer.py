# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        res=""
        while head:
            res+=str(head.val)
            head=head.next
        
        integer=0
        pow=0
        for i in range(len(res)-1,-1,-1):
            integer+=(2**pow)*int(res[i])
            pow+=1
        return integer
