# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        p = dummy
        carry = 0
        while l1 or l2:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            s = l1_val + l2_val + carry

            carry = s // 10
            node_value = s % 10 

            new_node = ListNode(node_value)

            p.next = new_node

            p = new_node
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if carry:
            p.next = ListNode(1)
        
        return dummy.next