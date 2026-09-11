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
        p = head
        copy_map = {}
        while p:
            copy_map[p] = Node(p.val)
            p = p.next
        
        for org, copy in copy_map.items():
            if org.next:
                copy.next = copy_map[org.next]
            if org.random:
                copy.random = copy_map[org.random]
            
        return copy_map[head] if head else None
        


