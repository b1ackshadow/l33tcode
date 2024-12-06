from typing import List
from collections import deque

class Solution:

    def build_graph(self, adj_list):
        self.graph = {}

        for each in adj_list:
            u, v = each
            adj = self.graph.get(v, set())
            adj.add(u)
            self.graph[v] = adj

    def find_ready_node(self):
        for i in range(len(self.indegrees)):
            if self.indegrees[i] == 0:
                return i
        return -1

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if numCourses <= 1:
            return list(range(numCourses))

        self.indegrees = [0 for _ in range(numCourses)]
        self.build_graph(prerequisites)
        self.res = []

        for each in prerequisites:
            u, _ = each
            self.indegrees[u] += 1

        queue = deque()

        ready_idx = self.find_ready_node()
        if ready_idx == -1:
            return self.res

        queue.append(ready_idx)
        while queue:
            node = queue.popleft()
            print(f"processing node {node}")
            self.res.append(node)
            self.indegrees[node] = -1

            # dec adjacent node indegrees
            for adj in self.graph.get(node, []):
                self.indegrees[adj] -= 1

            ready_idx = self.find_ready_node()
            if ready_idx != -1:
                queue.append(ready_idx)

        return [] if len(self.res) != numCourses else self.res
        # return all([indegree == -1 for indegree in self.indegrees])

            # 

        



s = Solution()

test = (2, [[1, 0]])
assert s.findOrder(*test) == [0, 1], "1"
test = (4, [[1,0],[2,0],[3,1],[3,2]])
res = s.findOrder(*test) 
assert res == [0,2,1,3] or res == [0,1, 2, 3], f"1 - {res}"

print("Passed all cases")
