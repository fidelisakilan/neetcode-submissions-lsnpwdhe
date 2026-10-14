class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.left, self.right = Node(-1, -1), Node(-1, -1)
        self.left.next, self.right.prev = self.right, self.left
        self.heap = {}
        
    def add(self, key: int, val: int):
        new_node = Node(key, val)
        self.heap[key] = new_node
        prev, nxt = self.right.prev, self.right
        prev.next = new_node
        nxt.prev = new_node
        new_node.prev = prev
        new_node.next = nxt
    
    def remove(self, key: int):
        node = self.heap[key]
        del self.heap[key]
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
        
    def get(self, key: int) -> int:
        if key not in self.heap:
            return -1
        node = self.heap[key]
        self.remove(key)
        self.add(node.key, node.val)
        return node.val
        

    def put(self, key: int, value: int) -> None:
        if key in self.heap:
            self.remove(key)
        self.add(key, value)
        while len(self.heap) > self.capacity:
            node = self.left.next
            self.remove(node.key)

        
