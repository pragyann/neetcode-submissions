# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head.next:
            return

        l1 = head
        l1_end = None

        slow, fast = head, head

        while fast and fast.next:
            fast = fast.next.next
            if not (fast and fast.next):
                l1_end = slow

            slow = slow.next

        l1_end.next = None

        prev, curr = None, slow

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        l1, l2 = head, prev
        l2_end = None

        while l1 and l2:
            l1_next = l1.next
            l2_next = l2.next

            l1.next = l2
            l2.next = l1_next

            l1 = l1_next
            if not l1:
                l2_end = l2

            l2 = l2_next


        if l2:
            l2_end.next = l2
            






