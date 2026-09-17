class Node:
    def __init__(self, val = 0):
        self.key = None
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity

        self.left, self.right = Node(), Node()
        self.left.next, self.right.prev = self.right, self.left
    
    def size(self):
        return len(self.cache) # O (1)

    def remove_from_list(self, node): 
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev

    # Adds to the left of right
    def add_to_list(self, node):
        prev, next = self.right.prev, self.right
        prev.next, next.prev = node, node
        node.prev, node.next = prev, next

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        self.remove_from_list(node)
        self.add_to_list(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove_from_list(self.cache[key])

        node = Node(value)
        node.key = key
        self.cache[key] = node

        self.add_to_list(node)
        if self.size() > self.capacity:
            del self.cache[self.left.next.key]
            self.remove_from_list(self.left.next)
