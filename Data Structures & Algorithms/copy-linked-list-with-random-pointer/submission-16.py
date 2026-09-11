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
        old_to_copy = {None: None}

        # First pass, create copy of each node and build the map
        p = head
        while p:
            old_to_copy[p] = Node(p.val)
            p = p.next
        
        # Second pass, build the random and next pointer links
        p = head
        while p:
            copy = old_to_copy[p]
            copy.next = old_to_copy[p.next]
            copy.random = old_to_copy[p.random]
            p = p.next
        
        return old_to_copy[head]
