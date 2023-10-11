# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        hashset = set() 
        # traverse the linked list using a while loop
        while head:
            # if the current node is already in the set, it's the start of the cycle
            if head in hashset:   
                return head
            # otherwise, add the current node to the set and move to the next node
            hashset.add(head)
            head = head.next
        # if we reach the end of the linked list without finding a cycle, return None
        return None
        

        