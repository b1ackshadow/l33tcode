from typing import Dict
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.cap = capacity

    def get(self, key: int) -> int:
        if key in self.cache:
            self.put(key, self.cache[key])
            return self.cache[key]

        return -1
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            del self.cache[key]

        self.cache[key] = value
        if len(self.cache) > self.cap:
            self.cache.popitem(False)

    def __str__(self):
        return str(self.cache)

# Your LRUCache object will be instantiated and called as such:
lRUCache = LRUCache(2);
lRUCache.put(1, 1); 
print(lRUCache)
lRUCache.put(2, 2); 
print(lRUCache.get(1))
print(lRUCache)
lRUCache.put(3, 3); 
print(lRUCache)
lRUCache.get(2);    
print(lRUCache.get(2))
lRUCache.put(4, 4); 
print(lRUCache)
lRUCache.get(1);    
print(lRUCache.get(1))
lRUCache.get(3);    
print(lRUCache.get(3))
print(lRUCache)
lRUCache.get(4);    
print(lRUCache.get(4))
print(lRUCache)
