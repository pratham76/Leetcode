# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # o(n) tine and o(n) space
        temp=head
        slist=[]
        while temp:
            slist.append(temp.val)
            temp=temp.next
        
        if slist==slist[::-1]:
            return True
        return False
