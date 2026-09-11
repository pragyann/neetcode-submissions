"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        if not head:
            return None
            
        op = head
        new_head = Node(head.val)

        np = new_head

        copy_map = {op: np}

        while op.next:
            new_node = copy_map.get(op.next, Node(op.next.val))
            np.next = new_node

            copy_map[op.next] = np.next

            old_random = op.random

            if old_random:
                if old_random in copy_map:
                    np.random = copy_map[old_random]
                else:
                    new_random = Node(old_random.val)
                    np.random = new_random
                    copy_map[old_random] = new_random

            np = np.next
            op = op.next
        
        
        
        if op.random:
            np.random = copy_map[op.random]
        
        return new_head