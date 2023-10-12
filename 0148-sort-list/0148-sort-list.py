# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getmid(self, head):
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def merge(self, left, right):
        tail = dummy = ListNode(0)  # Create a dummy node to simplify the code.
        while left and right:
            if left.val < right.val:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next
            tail = tail.next
        if left:
            tail.next = left
        if right:
            tail.next = right
        return dummy.next  # Return the new head of the merged list.

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        left = head
        right = self.getmid(head)
        temp = right.next
        right.next = None  # Disconnect the right sublist from the rest of the list.

        left = self.sortList(left)
        right = self.sortList(temp)  # Use 'temp' as the right list to sort.

        return self.merge(left, right)  # Return the new head of the merged list.
