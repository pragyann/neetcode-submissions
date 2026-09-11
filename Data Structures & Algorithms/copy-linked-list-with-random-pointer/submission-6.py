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
        copy_map = {None: None}
        while p:
            copy_map[p] = Node(p.val)
            p = p.next

        p = head

        while p:
            copy = copy_map[p]
            copy.next = copy_map[p.next]
            copy.random = copy_map[p.random]

            p = p.next
            
        return copy_map[head] 
        


