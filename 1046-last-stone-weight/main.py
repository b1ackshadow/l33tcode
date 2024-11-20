from typing import List
import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        self.heap = []
        self.k = 1
        def add(val):
            heapq.heappush(self.heap, -val)

        def remove() -> int:
            return heapq.heappop(self.heap)

        for e in stones:
            add(e)

        while len(self.heap) > 1:
            y, x = -remove(), -remove() # get the actual numbers

            if x == y:
                continue

            # else 

            newY = y - x
            heapq.heappush(self.heap, -newY)

        if len(self.heap) == 0:
            return 0

        return -self.heap[0]



        

s = Solution()

print(s.lastStoneWeight([2,7,4,1,8,1]))
