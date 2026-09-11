# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.recurse(None, head)
    
    def recurse(self, prev, curr):
        if curr == None:
            return prev
        
        next_curr = curr.next 
        curr.next = prev

        return self.recurse(curr, next_curr)
