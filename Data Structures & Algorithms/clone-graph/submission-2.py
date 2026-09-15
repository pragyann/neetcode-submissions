"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        old_to_new = {}

        def clone(node: Node) -> Node:
            if node in old_to_new:
                return old_to_new[node]
            
            node_clone = Node(val=node.val)
            old_to_new[node] = node_clone

            for nei in node.neighbors:
                node_clone.neighbors.append(clone(nei))
            
            return node_clone
        
        return clone(node)

