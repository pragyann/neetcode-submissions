# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next

            tail = tail.next
        
        if list1:
            tail.next = list1
        if list2:
            tail.next = list2
        
        return dummy.next

# class Solution:
#     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
#         if not list1: return list2
#         if not list2: return list1

#         list1P, list2P = list1, list2

#         head = None
#         curr_node = None

#         while list1P and list2P:
#             list1_next, list2_next = list1P.next, list2P.next
#             smaller, greater = None, None
#             if list1P.val < list2P.val:
#                 smaller = list1P
#                 greater = list2P
#             else:
#                 smaller = list2P
#                 greater = list1P

#             if not head:
#                 head = smaller
#                 head.next = greater
#                 curr = head.next
#             else:
#                 curr.next = smaller
#                 curr.next.next = greater           

#             list1P = list1_next
#             list2P = list2_next

#         if list1P: curr_node.next = list1P
#         if list2P: curr_node.next = list2P
        
#         return head
        





            