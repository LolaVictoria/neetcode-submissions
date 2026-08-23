class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        #dummy nodes
        self.left = Node(0, 0) #lru
        self.right = Node(0, 0) #mru

        self.left.next = self.right
        self.right.prev = self.left
    
    # Remove a node from the linked list
    def remove(self, node):
        prev = node.prev
        next = node.next

        prev.next = next
        next.prev = prev

    # Add a node right before the MRU dummy
    def insert(self, node):
        prev = self.right.prev

        prev.next = node
        node.prev = prev

        node.next = self.right
        self.right.prev = node
        

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]

            self.remove(node)
            self.insert(node)

            return node.value
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        
        node = Node(key, value)
        self.cache[key] = node
        self.insert(node)

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        
