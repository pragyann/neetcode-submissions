# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # find the midpoint and spli the lists
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next # slow is the last element of the first list
        slow.next = None

        # reverse the second list
        prev = None
        curr = second
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        second = prev # prev will have the start of the new reversed second list

        # merge the lists
        while second: # for even numbered full list, second list will have one less 
            head_next, second_next = head.next, second.next
            head.next = second
            second.next = head_next
            head = head_next
            second = second_next
