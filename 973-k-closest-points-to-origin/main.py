from typing import List
import math
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        self.heap = []
        self.distance_map = {}
        self.k = 1


        def euclidean(x, y) -> float:
            return math.sqrt(x ** 2 + y ** 2)
        
        def add(x, y):
            dist = euclidean(x, y)
            current_dist = self.distance_map.get(dist, [])
            current_dist.append([x,y])
            self.distance_map[dist] = current_dist
            heapq.heappush(self.heap, -dist)

            if len(self.heap) == k + 1:
                dist = heapq.heappop(self.heap)
                try:
                    del self.distance_map[-dist]
                except Exception as e:
                    pass

        for [x,y] in points:
            add(x,y)

        return [point for points in self.distance_map.values() for point in points]


s = Solution()

print(s.kClosest([[1,3],[-2,2]], 1))
print(s.kClosest([[3,3],[5,-1],[-2,4]], 2))
print(s.kClosest([[0,1], [1,0]], 2))

