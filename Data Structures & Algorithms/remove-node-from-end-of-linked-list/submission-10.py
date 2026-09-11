# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        left, right = dummy, head

        # move the second point n time 
        for _ in range(n):
            right = right.next

        # move the two pointer together unit p2 reaches last element
        while right:
            left = left.next
            right = right.next

        # At this point, p1 will be one element before the nth element we need to remove
        left.next = left.next.next

        return dummy.next
        
