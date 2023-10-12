# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # o(n) tine and o(n) space
        """
        temp=head
        slist=[]
        while temp:
            slist.append(temp.val)
            temp=temp.next
        
        if slist==slist[::-1]:
            return True
        return False
        """
        #o(1)
        slow,fast=head,head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        
        #reverse sencond half of the list
        prev=None
        while slow:
            temp=slow.next
            slow.next=prev
            prev=slow
            slow=temp
        
        #check for palindrome
        left,right=head,prev
        while right:
            if left.val!=right.val:
                return False
            left=left.next
            right=right.next
        return True
     
