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

        visited = set()
        old_to_new[node] = Node(val=node.val)
        def clone_each(node):
            if not node:
                return
            
            visited.add(node)
            for nei in node.neighbors:
                if nei not in old_to_new:
                    old_to_new[nei] = Node(val=nei.val)
                old_to_new[node].neighbors.append(old_to_new[nei])
                if nei not in visited:
                    visited.add(nei)
                    clone_each(nei)
        clone_each(node)

        return old_to_new[node]