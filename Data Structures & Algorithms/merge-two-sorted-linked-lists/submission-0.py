# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list1P, list2P = list1, list2

        if not list1: return list2
        if not list2: return list1

        head = None
        if list1.val < list2.val:
            head = list1
            list1P = list1.next
        else:
            head = list2
            list2P = list2.next

        curr_node = head

        while list1P and list2P:
            if list1P.val < list2P.val:
                curr_node.next = list1P
                list1P = list1P.next
            else:
                curr_node.next = list2P
                list2P = list2P.next

            curr_node = curr_node.next
        
        if list1P:
            curr_node.next = list1P
        if list2P:
            curr_node.next = list2P
        
        return head




            