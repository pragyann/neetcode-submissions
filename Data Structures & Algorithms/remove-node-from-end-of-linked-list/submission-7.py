# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class Solution:
#     def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
#         length = 0

#         p = head

#         while p:
#             p = p.next
#             length += 1
        
#         index = length - n

#         dummy = ListNode()
#         dummy.next = head

#         node_before_deletion = dummy

#         for _ in range(index):
#             node_before_deletion = node_before_deletion.next

#         node_before_deletion.next = node_before_deletion.next.next

#         return dummy.next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        left, right = dummy, head

        for _ in range(n):
            right = right.next

        while right:
            left = left.next
            right = right.next
        
        left.next = left.next.next

        return dummy.next
