from typing import Dict


class Node:
    def __init__(self,key, val,prev = None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:
    

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache: Dict[int, Node] = dict()
        self.size = 0
        self.lru_head = Node(None, None) # null key value init
        self.lru_tail = self.lru_head
        
    def get(self, key: int) -> int:
        # if key in self.cache:
        #     index = self.cache[key]
        #     self.
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
        # no need to check size
            node = self.cache[key]
            node.val = value # updated node

            prev = node.prev
            next = node.next

            prev.next = next

            node.next = None
            self.lru_tail.next = node
            node.prev = self.lru_tail
            self.lru_tail = node
        else:

            self.evict()
            node = Node(key, value)

            self.cache[key] = node
            if self.lru_tail:
                self.lru_tail.next = node
                node.prev = self.lru_tail
                self.lru_tail = node
            self.size += 1

    def evict(self):
        if self.size >= self.cap:
            eviction_candidate = self.lru_head.next
            if eviction_candidate:
                print(f"Evicting {eviction_candidate.key}")
                self.lru_head.next = eviction_candidate.next
                next = eviction_candidate.next
                if next:
                    next.prev = self.lru_head
                del self.cache[eviction_candidate.key]
                self.size -= 1





# Your LRUCache object will be instantiated and called as such:
capacity = 2
obj = LRUCache(capacity)
key = 123; value = 456
obj.put(key,value)
key = 234; value = 567
key = 369; value = 789
param_1 = obj.get(key)
