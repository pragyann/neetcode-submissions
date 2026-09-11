# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None

        length = 0

        p = head

        while p:
            p = p.next
            length += 1
        
        index = length - n

        dummy = ListNode()
        dummy.next = head

        node_before_deletion = dummy

        for _ in range(index):
            node_before_deletion = node_before_deletion.next

        node_to_delete = node_before_deletion.next

        if node_to_delete == head:
            head = head.next
            return head

        node_before_deletion.next = node_to_delete.next
        node_to_delete.next = None

        return head
