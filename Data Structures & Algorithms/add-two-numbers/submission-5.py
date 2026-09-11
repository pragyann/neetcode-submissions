# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode()
        p = dummy

        while l1 or l2 or carry:
            n1 = l1.val if l1 else 0
            n2 = l2.val if l2 else 0
            sum = n1 + n2 + carry

            carry = sum // 10
            sum = sum % 10
            
            new_node = ListNode(sum)
            p.next = new_node
            p = p.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next
