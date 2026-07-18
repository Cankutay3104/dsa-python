# LeetCode "146. LRU Cache" Solution

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.map = {}
        
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _insert_at_head(self, node):
        first_node = self.head.next
        
        self.head.next = node
        node.prev = self.head
        node.next = first_node
        first_node.prev = node

    def get(self, key):
        if key in self.map:
            node = self.map[key]
            
            self._remove(node)
            self._insert_at_head(node)
            return node.val
        return -1

    def put(self, key, value):
        if key in self.map:
            node = self.map[key]
            node.val = value
            self._remove(node)
            self._insert_at_head(node)
        else:
            if len(self.map) == self.capacity:
                lru_node = self.tail.prev
                self._remove(lru_node)
                del self.map[lru_node.key]
            
            new_node = Node(key, value)
            self.map[key] = new_node
            self._insert_at_head(new_node)