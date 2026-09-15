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
            
            clonned_node = Node(val=node.val)
            old_to_new[node] = clonned_node

            for nei in node.neighbors:
                clonned_nei = clone(nei)
                clonned_node.neighbors.append(clonned_nei)
            
            return clonned_node
        
        return clone(node)