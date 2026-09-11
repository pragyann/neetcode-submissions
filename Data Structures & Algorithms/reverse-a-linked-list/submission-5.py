# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         prev, curr = None, head

#         while curr:
#             nxt = curr.next
#             curr.next = prev
#             prev = curr
#             curr = nxt
        
#         return prev

# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if not head:
#             return None

#         if not head.next:
#             return head

#         new_head = self.reverseList(head.next)
#         head.next.next = head
#         head.next = None

#         return new_head

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.recurse(None, head)
        
    def recurse(self, prev, curr):
        if not curr:
            return prev
        
        new_next = curr.next
        curr.next = prev

        return self.recurse(curr, new_next)



        