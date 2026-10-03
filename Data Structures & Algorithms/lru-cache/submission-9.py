class Node:
    def __init__(self, key, value):
        self.key, self.value = key, value
        self.next, self.prev = None, None



class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next, self.right.prev = self.right, self.left
    
    def insert(self, node: Node):
        prev, nxt = self.right.prev, self.right
        prev.next = node
        nxt.prev = node
        node.prev, node.next = prev, nxt
    
    def delete(self, node: Node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.delete(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.delete(self.cache[key])
            self.cache[key] = Node(key, value)
            self.insert(self.cache[key])
        else:
            self.cache[key] = Node(key, value)
            self.insert(self.cache[key])
        
        if len(self.cache) > self.capacity:
            del self.cache[self.left.next.key]
            self.delete(self.left.next)

        
