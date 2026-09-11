class Node:
    def __init__(self, key, val=0, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.count = 0
        self.cache = {}

        self.left = Node("")
        self.right = Node("")

        self.left.next = self.right
        self.right.prev = self.left

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        self.remove(node)
        self.add(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
            self.count -=1

        if self.capacity == self.count:
            node_to_remove = self.left.next

            self.remove(node_to_remove)
            del self.cache[node_to_remove.key]
            self.count -=1
        
        new_node = Node(key, value)
        self.cache[key] = new_node
        self.add(new_node)
        self.count += 1

    def remove(self, node: Node) -> None:
        prev = node.prev
        next = node.next

        prev.next, next.prev = next, prev
    
    # Add the node to the left of the right 
    def add(self, node: Node) -> None:
        prev = self.right.prev
        next = self.right

        prev.next, next.prev = node, node
        node.next, node.prev = next, prev
            