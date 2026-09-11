# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        seen = set()

        next_node = head

        while next_node:
            if next_node in seen:
                return True
            seen.add(next_node)
            next_node = next_node.next

        return False

