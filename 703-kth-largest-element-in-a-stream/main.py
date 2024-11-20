import heapq
from typing import List
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.k = k

        for n in nums:
            self.add(n)


    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val) # convert to max heap
        if len(self.heap) == self.k + 1:
            heapq.heappop(self.heap)
        return self.heap[0]




kthLargest = KthLargest(3, [4, 5, 8, 2])
# print(kthLargest.heap[0])
print(kthLargest.add(3)); # return 4
print(kthLargest.add(5)); # return 5
print(kthLargest.add(10)); # return 5
print(kthLargest.add(9)); # return 8
print(kthLargest.add(4)); # return 8
