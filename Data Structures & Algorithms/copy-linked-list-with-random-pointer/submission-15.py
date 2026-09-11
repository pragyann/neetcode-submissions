"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old_to_new = {}

        p = head

        while p:
            old_to_new[hash(p)] = Node(p.val)
            p = p.next
        
        p = head
        dummy = Node(0)
        new_p = dummy
        while p:
            new_p.next = old_to_new[hash(p)]

            if p.next:
                new_p.next.next = old_to_new[hash(p.next)]

            if p.random:
                new_p.next.random = old_to_new[hash(p.random)]
            
            new_p = new_p.next
            p = p.next
        
        return dummy.next
        